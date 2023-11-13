import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import numpy as np
import scipy 
import os
import sys
import rmsd
from multiprocessing import Manager, Pool, Process
import torchani
import time

from functools import partial
print_flushed = partial(print, flush=True)



class NN(nn.Module):
    def __init__(self, 
            neurons=0,
            optimizer=lambda param: optim.AdamW(param,lr=0.001),
            device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
        super(NN, self).__init__()
        
        self.setDevice(device)
        self.setNormalization()
        if neurons: self.build(neurons, optimizer)
    def build(self, neurons,optimizer):
        self.neurons=neurons
        layers=[]
        for i in range(len(neurons)-2):
            layers.append(nn.Linear(neurons[i],neurons[i+1]))
            # layers.append(nn.BatchNorm1d(neurons[i+1]))
            layers.append(nn.GELU())
            # layers.append(nn.Dropout(p=0.2))
        layers.append(nn.Linear(neurons[i+1],neurons[i+2]))
        self.NN = nn.Sequential(*layers)
        # self.optimizer=optimizer(self.parameters())
    def forward(self, x):
        x = (x-self.mX)/self.sX
        output = self.NN(x)
        output = output*self.sY+self.mY
        return output
    def setNormalization(self, mX=0, sX=1., mY=0., sY=1.):
        self.mX=torch.tensor(mX).float().to(self.device)
        self.sX=torch.tensor(sX).float().to(self.device)
        self.mY=torch.tensor(mY).float().to(self.device)
        self.sY=torch.tensor(sY).float().to(self.device)
    def setDevice(self, device):
        self.device=device
    def predict(self,x):
        x=torch.Tensor(x).to(self.device).requires_grad_(True)
        mp=self(x)
        vp=batch_jacobian(mp,x)[:,:,-1]
        y=torch.cat((mp,vp),dim=1)
        return y
    def save(self,path):
        torch.save({
            'neurons':self.neurons,
            'model_state_dict': self.state_dict(),
            'optimizer_state_dict': self.optimizer.stat_dict(),
            'normalization': {'mX': self.mX, 'sX': self.sX, 'mY':self.mY,'sY':self.sY}
        },path)
    def load(self,path):
        model_dict=torch.load(path)
        self.neurons=model_dict['neurons']
        self.NN=nn.Sequential(*self.layers)
        self.load_state_dict(model_dict['model_state_dict'])
        self.optimizer.load_state_dict(model_dict['optimizer_state_dict'])



def batch_jacobian(y, x):
    y=y.sum(dim=0)
    jac = [torch.autograd.grad(yi, x, retain_graph=True)[0] for yi in y]
    jac = torch.stack(jac, dim=1)
    return jac


device = torch.device('cpu')
ANI1ccx = torchani.models.ANI1ccx(periodic_table_index=True).to(device)

def getANI1ccxPot(xyz,z):
    species=torch.tensor(np.repeat(z[np.newaxis,:],xyz.shape[0],axis=0)).to(device)
    coords=torch.tensor(xyz).to(device).float()
    _, potentials=ANI1ccx((species, coords))
    potentials=potentials.cpu().detach().numpy()
    time.sleep(0.0000001)
    return potentials

refTrio=np.array([[0.,0.,1.],[0.,1.,0.],[1.,0.,0.]],dtype=np.float32)
refTrioV=np.zeros((3,3),dtype=np.float32)
    
# def printer(*args,**kwargs):
#     print(*args,**kwargs)
#     sys.stdout.flush()

def shuffle(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def intermask(s,l):
    x=np.zeros(l*l).astype(bool)
    a=np.arange(l)
    k=0
    for i in range(l):
        b=np.roll(a,-i)
        for j in range(l):
            if a[j] <s and b[j] < s:
                x[k]=True
            else:
                x[k]=False
            k+=1
    return x==1

def findInits(x,tc,tmax,tmin):
    t=x[:,-1]
    t0s=np.append(np.arange(tmin,tmax,tc),tmax)
    inits=[]
    for i in t0s:
        # print('\r( `д´)',i)
        inits.append(x[np.abs(t-i).argmin()])
    return np.array(inits),t0s

def sparseInit(x,y,tc=np.inf,tl=0,tmax=np.inf,tmin=0,step=1):
    # inits,t0s=findInits(x,tc,tmax,tmin)
    step=int(tc/(x[1,-1]-x[0,-1]))+1
    mask=(x[:,-1]<=tmax)*(x[:,-1]>=tmin)
    xx,yy=x[mask],y[mask]
    xout=np.repeat(xx[::step],step,axis=0)[:xx.shape[0]]
    xout[:,-1]=xx[:,-1]-xout[:,-1]
    # print('done')
    return xout,yy
        
def denseInit(x,y,tc=np.inf,tl=0,tmax=np.inf,tmin=0,step=1):
    xout,yout=[],[]
    mask=(x[:,-1]<=tmax)*(x[:,-1]>=tmin)
    xx,yy=x[mask],y[mask]
    for j in range(0,len(xx),step):
        # print("( ﾟ∀。)",j)
        xxx=np.concatenate((xx[:,:-1],np.roll(xx[:,[-1]],-j)-xx[:,[-1]]),axis=1)
        yyy=np.roll(yy,-j,axis=0)
        # mask2=(np.abs(xxx[:,-1])>=tl)*(np.abs(xxx[:,-1])<=tc)
        mask2=(xxx[:,-1]>=tl)*(xxx[:,-1]<=tc)
        xout.append(xxx[mask2])
        yout.append(yyy[mask2])
    xout=np.concatenate(xout)
    yout=np.concatenate(yout)   
    return xout,yout
    

def getData(raw,xlist,ylist,tc,tl=0,tmax=np.inf,tmin=0,step=1,mode='sparse'):
    if xlist[-1] != 't':
        if 't' in xlist:
            xlist.remove('t')
        xlist.append('t')
    x=np.concatenate(tuple(map(lambda x: raw.get(x).reshape(raw.get(x).shape[0],-1),xlist)),axis=1)
    y=np.concatenate(tuple(map(lambda x: raw.get(x).reshape(raw.get(x).shape[0],-1),ylist)),axis=1)
    if mode=='sparse':
        x,y=sparseInit(x,y,tc,tl,tmax,tmin,step=step)
    elif mode=='dense':
        x,y=denseInit(x,y,tc,tl,tmax,tmin,step=step)
    return x,y

def getRecursiveData(data,x_len=50,y_len=1,step=1):
    n=len(data)-x_len*step-y_len*step
    x=np.zeros([n,x_len]+list(data.shape[1:]))
    y=np.zeros([n,y_len]+list(data.shape[1:]))
    for i in range(n):
        for j in range(0,x_len):
            x[i,j]=data[j*step]
        for j in range(0,y_len):
            y[i,j]=data[(x_len+j)*step]
    return x,y

def M2dM(x,y):
    _,w=y.shape
    newY=y.copy()
    newY[:,:w//2]=(y[:,:w//2]-x[:,:w//2])
    return x,newY

def dM2M(x,y):
    _,w=y.shape
    newY=y.copy()
    newY[:,:w//2]=y[:,:w//2]+x[:,:w//2] 
    return x,newY

def M2Vbar(x,y):
    mask=x[:,-1]!=0
    x=x[mask]
    y=y[mask]
    _,w=y.shape
    newY=y.copy()
    newY[:,:w//2]=(y[:,:w//2]-x[:,:w//2])/x[:,[-1]]
    newY[:,w//2:-1]=y[:,w//2:-1]/x[:,[-1]]-(y[:,:w//2]-x[:,:w//2])/x[:,[-1]]/x[:,[-1]]
    return x,newY

def Vbar2M(x,y):
    h,w=y.shape
    newY=y.copy()
    newY[:,:w//2]=y[:,:w//2]*x[:,[-1]]+x[:,:w//2] 
    newY[:,w//2:]=y[:,w//2:]*x[:,[-1]]+y[:,:w//2]
    return x,newY

def logisticateT(x,y,a=1,b=5):
    _,w=y.shape
    newX=x.copy()
    newX[:,-1]=1/(1+a*np.exp(b-x[:,-1]))
    newY=y.copy()
    newY[:,w//2:-1]=y[:,w//2:-1]*(1+a*np.exp(b-x[:,[-1]]))**2/(a*np.exp(b-x[:,[-1]]))
    return newX,newY

def unlogisticateT(x,y,a=1,b=5):
    _,w=y.shape
    newX=x.copy()
    newX[:,-1]=b-np.log((1/x[:,-1]-1)/a)
    newY=y.copy()
    newY[:,w//2:-1]=y[:,w//2:-1]/(1+a*np.exp(b-newX[:,-1]))**2*(a*np.exp(b-newX[:,-1]))
    return newX,newY

def normalizeT(x,y,a=10,b=5,l=0):
    mask=x[:,-1]!=0
    x=x[mask]
    y=y[mask]
    if not l: l=(y.shape[1]-1)//2
    newY=y.copy()
    dM=(y[:,:l]-x[:,:l])
    v=y[:,l:2*l]
    t=x[:,[-1]]
    # ft=(1+a*np.exp(b-x[:,[-1]]))
    # dftdt=-a*np.exp(b-x[:,[-1]])
    ft=1/(1-np.exp(-a*t))
    dftdt=-a*np.exp(-a*t)/(1-np.exp(-a*t))**2
    newY[:,:l]=dM*ft
    newY[:,l:2*l]=v*ft+dftdt*dM
    return x,newY

def unnormalizeT(x,y,a=10,b=5,l=0):
    if not l: l=(y.shape[1])//2
    newY=y.copy()
    M0=x[:,:l]
    t=x[:,[-1]]
    # ft=(1+a*np.exp(b-x[:,[-1]]))
    # dftdt=-a*np.exp(b-x[:,[-1]])
    ft=(1-np.exp(-a*t))
    dftdt=a*np.exp(-a*t)
    NN=y[:,:l]
    dNNdt=y[:,l:2*l]
    newY[:,:l]=NN*ft+M0
    newY[:,l:2*l]=(dNNdt*ft+dftdt*NN)
    return x,newY



# @tf.function
def differentiation(model,xx,x_shift=0,x_scale=1,y_shift=0,l=0):
    pass
    # if not l: l=xx.shape[1]//2
    # xx=tf.cast(xx,tf.float32)
    # xx=(xx-x_shift)/x_scale
    # with tf.GradientTape() as tape:
    #     tape.watch(xx)
    #     x_new = model(xx) + y_shift[:l]
    # v=tape.batch_jacobian(x_new,xx)[:,:l,-1]/x_scale[-1]
    # y=tf.concat([x_new[:,:l],tf.cast(v,tf.float32)],1)
    # return y

def getY(model,x,x_shift=0,x_scale=1,y_shift=0,l=0):
    pass
    # xx=tf.constant(x.reshape(1,-1))
    # y=differentiation(model,xx,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l)[0]
    # return y.numpy()

def recursive(model,x,tc,x_shift=0,x_scale=1,y_shift=0,l=0):
    pass
    if np.abs(x[0,-1])<=tc:
        return getY(model,x,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l)
    else:
        xx=getY(model,np.append(x[0,:-1],tc*x[0,-1]/np.abs(x[0,-1])),x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l)
        xx=np.append(xx,x[0,-1]-tc*x[0,-1]/np.abs(x[0,-1])).reshape(1,-1)
        return recursive(model,xx,tc,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l)


def predict(model,x,tc=np.inf,x_shift=0,x_scale=1,y_shift=0,l=0):
    h,w=x.shape
    out=np.zeros([h,(w-1)])
    for i in range(h):
        out[i]=recursive(model,x[[i]],tc,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l)
    return out

def getMonomial(x):
    return np.exp(-1*x)

def getID(x):
    return 1/x

def r2D(r):
    n=int((1+np.sqrt(1+8*len(r)))/2)
    d=np.array([0 if i==j else r[(2*n-2-min(i,j))*(min(i,j)+1)//2+max(i,j)-n] for i in range(n) for j in range(n)]).reshape(-1,n)
    return d

def getXYZ(r):
    d2=r2D(r)**2
    c=np.identity(d2.shape[0])-np.ones(d2.shape)/d2.shape[0]
    b=-0.5*c.dot(d2.dot(c))
    xyz=(np.sqrt(np.linalg.svd(b)[1])*(np.linalg.svd(b)[0]))[:,:3]
    return xyz

def loadXYZ(fname,dtype=np.array,getsp=True):
    xyz=[]
    sp=[]
    with open(fname) as f:
        for line in f:
            xyz_=[]
            sp_=[]
            natom=int(line)
            f.readline()
            for _ in range(natom):
                if getsp: 
                    _sp_,*_xyz_=f.readline().split()
                    sp_.append(_sp_)
                else: _xyz_=f.readline().split()[-3:]
                xyz_.append(_xyz_)
            xyz.append(np.array(xyz_).astype(float))
            sp.append(np.array(sp_))
    return dtype(xyz),dtype(sp)

def saveXYZs(fname,xyzs,sp,mode='w',msgs=None,scaling=1):
    if type(scaling)==str:
        if scaling.lower()=='b2a': scaling=0.52917720859
        elif scaling.lower()=='a2b': scaling=1/0.52917720859
    with open(fname,mode)as f:
        for xyz in xyzs:
            f.write("%d\n"%sp.shape[0])
            if msgs: f.write(msgs.pop(0)+"\n")
            else: f.write('\n')
            for j in range(sp.shape[0]):
                f.write(sp[j]+' ')
                f.write('%f %f %f\n'%tuple(xyz[j]*scaling))

def saveXYZ(fname,xyz,sp,mode='w',msg='',scaling=1):
    if type(scaling)==str:
        if scaling.lower()=='b2a': scaling=0.52917720859
        elif scaling.lower()=='a2b': scaling=1/0.52917720859
    with open(fname,mode)as f:
        f.write("%d\n"%sp.shape[0])
        f.write(msg+"\n")
        for j in range(sp.shape[0]):
            f.write(sp[j]+' ')
            f.write('%f %f %f\n'%tuple(xyz[j]*scaling))

def getEp(xyz,sp,xyzfile='xyz.xyz',epfile='ep.ep',log='/dev/null'):
    saveXYZ(xyzfile,xyz,sp)
    os.system(f'rm {epfile}')
    os.system(f'/export/home/fcge/deepmd-kit-1.2/bin/python3 ~/MLatom/bin/MLatom.py aiqm1 xyzfile={xyzfile}  yestfile={epfile} > {log}')
    with open(epfile) as f:
        ep=float(f.readline())
    return ep

def calcR(x):
    out=np.array([])
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            out=np.append(out,np.linalg.norm(x[i]-x[j]))
    return out

def getR(x):
    natom=int(x.shape[1])
    n=int(x.shape[0])
    nr=int(natom*(natom-1)/2)
    r=np.zeros([n,nr])
    for i in range(n):
        r[i]=calcR(x[i])
    return r

def calcVR(x,v):
    r=[]
    vr=[]
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            r.append(np.linalg.norm(x[i]-x[j]))
            vr.append((x[i]-x[j]).dot(v[i]-v[j])/r[-1])
    return np.array(r), np.array(vr)

def getVR(x,v):
    natom=int(x.shape[1])
    n=int(x.shape[0])
    nr=int(natom*(natom-1)/2)
    r=np.zeros([n,nr])
    vr=np.zeros([n,nr])
    for i in range(n):
        r[i],vr[i]=calcVR(x[i],v[i])
    return r, vr

def calcV(ad,bd,cd,vad,vbd,vcd,vb,vc):
    return np.linalg.solve(np.array([ad,bd,cd]),np.array([vad,vbd+bd.dot(vb),vcd+cd.dot(vc)]))

def getDirection(a,b=None):
    if b is None:
        return (a)/np.linalg.norm(a)
    else:
        return (b-a)/np.linalg.norm(b-a)

def getNormal(a,b,c):
    n=np.cross(b-a,c-b)
    return n/np.linalg.norm(n)

def getLinM(v,m):
    if m is None:
        m=np.ones(v.shape[-2])
    return np.sum(v*m[:,np.newaxis],axis=-2)#*1822.888515*24.188843265e-3/0.529177210903

def getCoM(xyz,m=None):
    if m is None:
        m=np.ones(xyz.shape[-2])
    return np.sum(xyz*m[:,np.newaxis],axis=-2,keepdims=True)/np.sum(m)

def adjLinM(P,v,m):
    return v-getCoM(v,m)+P/np.sum(m)

def getAngM(xyz,v,m,center=None):
    if center is None:
        centered=xyz-getCoM(xyz,m)
    else:
        centered=xyz-center
    L=np.sum(m[:,np.newaxis]*np.cross(centered,v),axis=-2)
    return L#*1822.888515*24.188843265e-3/0.529177210903

def getMomentOfInertiaTensor(xyz,m,center=None):
    if center is None:
        center=getCoM(xyz,m)
    centered=xyz-center
    if len(xyz.shape)==2:
        I=np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                for k in range(len(m)):
                    I[i,j]+=m[k]*(np.sum(centered[k]**2)-centered[k,i]*centered[k,j]) if i==j else m[k]*(-centered[k,i]*centered[k,j])
    if len(xyz.shape)==3:
        I=np.zeros((xyz.shape[0],3,3))
        for i in range(3):
            for j in range(3):
                for k in range(len(m)):
                    I[:,i,j]+=m[k]*(np.sum(centered[:,k]**2,axis=1)-centered[:,k,i]*centered[:,k,j]) if i==j else m[k]*(-centered[:,k,i]*centered[:,k,j])
    return I

def getAngV(xyz,v,m,center=None):
    L=getAngM(xyz,v,m,center)
    I=getMomentOfInertiaTensor(xyz,m,center)
    omega=np.linalg.inv(I).dot(L)
    return omega

def zeroAngM(xyz,v,m,center=None):
    if center is None:
        center=getCoM(xyz,m)
    omega=getAngV(xyz,v,m,center)
    return v-np.cross(omega,xyz-center)

def adjAngM(L,xyz,v,m,center=None):
    if center is None:
        center=getCoM(xyz,m)
    L0=getAngM(xyz,v,m,center)
    I=getMomentOfInertiaTensor(xyz,m,center)
    omega=np.linalg.inv(I).dot(L-L0)
    return v+np.cross(omega,xyz-center)

def adjV(xyz,v,m,P=np.zeros(3),L=np.zeros(3)):
    center=getCoM(xyz,m)
    L0=getAngM(xyz,v,m,center)
    I=getMomentOfInertiaTensor(xyz,m,center)
    omega=np.linalg.inv(I).dot(L-L0)
    return v+np.cross(omega,xyz-center)-getCoM(v,m)+P/np.sum(m)

def getEk_trans(v,m):
    return np.sum(getLinM(v,m)**2)/np.sum(m)/2/1822.888515

def getEk_rot(xyz,v,m):
    return np.sum(getAngM(xyz,v,m)**2)/np.sum(m*np.sum(xyz**2,axis=1))/2/1822.888515

def getEk_vib(xyz,v,m):
    return getEk(v,m)-getEk_trans(v,m)-getEk_rot(xyz,v,m)

def getEk(v,m):
    return 0.5*np.sum(m[:,np.newaxis]*v**2)/0.529177210903/0.529177210903*1822.888515*24.188843265e-3*24.188843265e-3 

def getEks(v,m):
    return 0.5*np.sum(m[:,np.newaxis]*v**2,axis=(1,2))/0.529177210903/0.529177210903*1822.888515*24.188843265e-3*24.188843265e-3 

# @tf.function(input_signature=[tf.TensorSpec(None, tf.float32),tf.TensorSpec(None, tf.float32)])
# def getEksTF(v,m=None):
#     return tf.numpy_function(getEks,[v,m],tf.float32)

def getOmega(ABC,vABC):
    A,B,C=ABC
    va,vb,vc=vABC
    ab=getDirection(A,B)
    ac=getDirection(A,C)
    bc=getDirection(B,C)
    AB=B-A
    AC=C-A
    BC=C-B
    n=np.cross(ab,ac)
    nn=np.cross(n,ab)
    omegab=np.cross(AB,vb-va)/np.linalg.norm(AB)**2
    omegac=(np.cross(AC.dot(nn)*nn,(vc-va).dot(n)*n-np.cross(omegab,AC).dot(n)*n)/np.linalg.norm(AC.dot(nn)*nn)**2)
    return omegab+omegac

def getV_(r,vr,refid=np.arange(3)):
    xyz=getXYZ(r)
    vrmat=r2D(vr)
    v=np.zeros(xyz.shape)
    n=xyz.shape[0]
    A=xyz[refid[0]]
    B=xyz[refid[1]]
    C=xyz[refid[2]]
    v[refid[1]]=getDirection(A,B)*vrmat[refid[0],refid[1]]
    v[refid[2]]=np.linalg.solve(np.array([getDirection(A,C),getDirection(B,C),np.cross(getDirection(A,C),getDirection(A,B))]),np.array([vrmat[refid[0],refid[2]],vrmat[refid[1],refid[2]]+v[refid[1]].dot(getDirection(B,C)),0]))
    for i in np.arange(n)[~np.in1d(np.arange(n),refid)]:
        v[i]=calcV(getDirection(A,xyz[i]),getDirection(B,xyz[i]),getDirection(C,xyz[i]),vrmat[refid[0],i],vrmat[refid[1],i],vrmat[refid[2],i],v[refid[1]],v[refid[2]])
    return xyz, v

def align(mol,ref):
    Mr=rmsd.kabsch(mol,ref)
    MrM=np.diag([1,1,-1]).dot(rmsd.kabsch(mol,ref))
    if np.mean((mol.dot(Mr)-ref)**2) > np.mean((mol.dot(MrM)-ref)**2):
        return MrM
    else:
        return Mr
    
def getV(r,vr,xyz,v,refid=np.arange(3)):
    xyz_,v_=getV_(r,vr,refid)
    xyz_c=xyz-np.mean(xyz,axis=0)
    Mr=align(xyz_,xyz_c)
    xyz_a=xyz_.dot(Mr)+np.mean(xyz,axis=0)
    v_a=v_.dot(Mr)
    omega=getOmega(xyz_a[refid],v[refid])
    A=xyz_a[refid[0]]
    A=xyz_a[refid[0]]
    va=v[refid[0]]
    return xyz_a,v_a+va+np.cross(omega,xyz_a-A)

def getDistance(xyz,idx=[0,1]):
    xyz=np.concatenate((xyz,refTrio))
    A,B=xyz[idx]
    return np.linalg.norm(B-A)

def getAngle(xyz,idx=[0,1,2]):
    xyz=np.concatenate((xyz,refTrio))
    A,B,C=xyz[idx]
    BA=A-B
    BC=C-B
    theta=np.arccos(np.clip(BA.dot(BC)/np.linalg.norm(BA)/np.linalg.norm(BC),-1,1))
    return theta

def getDihedralAngle(xyz,idx=[2,0,1,5]):
    xyz=np.concatenate((xyz,refTrio))
    A,B,C,D=xyz[idx]
    BA=A-B
    bc=getDirection(B,C)
    CD=D-C
    a,b=BA-BA.dot(bc)*bc,CD-CD.dot(bc)*bc
    theta=np.arccos(np.clip(a.dot(b)/np.linalg.norm(a)/np.linalg.norm(b),-1,1))
    if np.cross(a,b).dot(bc)<0:
        theta=-theta
    return theta

def getDistanceV(xyz,v,idx=[0,1]):
    xyz=np.concatenate((xyz,refTrio))
    v=np.concatenate((v,refTrioV))
    A,B=xyz[idx]
    AB=B-A
    vA,vB=v[idx]
    d=np.linalg.norm(AB)
    vd=(AB).dot(vB-vA)/d
    return d,vd

def getAngleV(xyz,v,idx=[0,1,2]):
    xyz=np.concatenate((xyz,refTrio))
    v=np.concatenate((v,refTrioV))
    A,B,C=xyz[idx]
    BA=A-B
    BC=C-B
    theta=np.arccos(np.clip(BA.dot(BC)/np.linalg.norm(BA)/np.linalg.norm(BC),-1,1))
    vA,vB,vC=v[idx]
    ba=getDirection(B,A)
    bc=getDirection(B,C)
    n=np.cross(bc,ba)/np.linalg.norm(np.cross(bc,ba))
    na=np.cross(ba,n)
    nc=np.cross(bc,n)
    omega=(vC-vB).dot(nc)/np.linalg.norm(BC)-(vA-vB).dot(na)/np.linalg.norm(BA)
    return theta,omega

def getDihedralAngleV(xyz,v,idx=[0,1,2,3]):
    xyz=np.concatenate((xyz,refTrio))
    v=np.concatenate((v,refTrioV))
    A,B,C,D=xyz[idx]
    BA=A-B
    bc=getDirection(B,C)
    CD=D-C
    a,d=BA-BA.dot(bc)*bc,CD-CD.dot(bc)*bc
    theta=np.arccos(np.clip(a.dot(d)/np.linalg.norm(a)/np.linalg.norm(d),-1,1))
    if np.cross(a,d).dot(bc)<0:
        theta=-theta
    na=np.cross(bc,a)/np.linalg.norm(a)
    nd=np.cross(bc,d)/np.linalg.norm(d)
    omega0=getOmega(xyz[idx[-3:]],v[idx[-3:]])
    vA,_,_,vD=v[idx]-v[idx[1]]-np.cross(omega0,xyz[idx]-xyz[idx[1]])
    omega=vD.dot(nd)/np.linalg.norm(d)-vA.dot(na)/np.linalg.norm(a)
    return theta,omega

def getDistanceVA(xyz,v,a,idx=[0,1]):
    xyz=np.concatenate((xyz,refTrio))
    A,B=xyz[idx]
    vA,vB=v[idx]
    aA,aB=a[idx]
    d=np.linalg.norm(B-A)
    vd=(B-A).dot(vB-vA)/d
    ad=((vB-vA).dot(vB-vA)+(B-A).dot(aB-aA))/d-vd**2/d
    return d,vd,ad

def getDihedralAngleVA(xyz,v,acc,idx=[0,1,2,3]):
    xyz=np.concatenate((xyz,refTrio))
    A,B,C,D=xyz[idx]
    BA=A-B
    bc=getDirection(B,C)
    CD=D-C
    a,d=BA-BA.dot(bc)*bc,CD-CD.dot(bc)*bc
    theta=np.arccos(np.clip(a.dot(d)/np.linalg.norm(a)/np.linalg.norm(d),-1,1))
    if np.cross(a,d).dot(bc)<0:
        theta=-theta
    na=np.cross(bc,a)/np.linalg.norm(a)
    nd=np.cross(bc,d)/np.linalg.norm(d)
    omega0=getOmega(xyz[idx[-3:]],v[idx[-3:]])
    vA,_,_,vD=v[idx]-v[idx[1]]-np.cross(omega0,xyz[idx]-xyz[idx[1]])
    omega=vD.dot(nd)/np.linalg.norm(d)-vA.dot(na)/np.linalg.norm(a)
    aA,_,_,aD=acc[idx]-acc[idx[1]]
    alpha=aD.dot(nd)/np.linalg.norm(d)-aA.dot(na)/np.linalg.norm(a)
    return theta,omega,alpha

def getAngleVA(xyz,v,a,idx=[0,1,2]):
    xyz=np.concatenate((xyz,refTrio))
    A,B,C=xyz[idx]
    BA=A-B
    BC=C-B
    theta=np.arccos(BA.dot(BC)/np.linalg.norm(BA)/np.linalg.norm(BC))
    vA,vB,vC=v[idx]
    aA,aB,aC=a[idx]
    ba=getDirection(B,A)
    bc=getDirection(B,C)
    n=np.cross(bc,ba)/np.linalg.norm(np.cross(bc,ba))
    na=np.cross(ba,n)
    nc=np.cross(bc,n)
    omega=(vC-vB).dot(nc)/np.linalg.norm(BC)-(vA-vB).dot(na)/np.linalg.norm(BA)
    alpha=(aC-aB).dot(nc)/np.linalg.norm(BC)-(aA-aB).dot(na)/np.linalg.norm(BA)
    return theta,omega,alpha

def addBackward(x,y):
    l=y.shape[1]//2
    xx=np.copy(x)
    yy=x[:,:-1]
    xx[:,:-1]=np.copy(y)
    xx[:,l:2*l]=-y[:,l:2*l][:]
    return np.concatenate((x,xx),axis=0),np.concatenate((y,yy),axis=0)

def alignVector(a,b):
    a=a/np.linalg.norm(a)
    b=b/np.linalg.norm(b)
    c=a.dot(b)
    v=np.cross(a,b)
    vx=np.array([
        [0,-v[2],v[1]],
        [v[2],0,-v[0]],
        [-v[1],v[0],0]
    ])
    return np.identity(3)+vx+vx.dot(vx)/(1+c)

def rotate3(axis,theta,vector=None):
    M=scipy.linalg.expm(np.cross(np.eye(3),axis/np.linalg.norm(axis)*theta))
    if vector is None:
        return M
    else:
        return M.dot(vector)

def XYZsettleDown(xyz,idx=[0,1,2,3],centre='com',m=None):
    A,B,C,D=xyz[idx]
    xyz=xyz-A
    A,B,C,D=xyz[idx]
    xyz=alignVector(B,[1,0,0]).dot(xyz.T).T
    A,B,C,D=xyz[idx]
    xyz=alignVector(np.cross(B,C),[0,0,1]).dot(xyz.T).T
    A,B,C,D=xyz[idx]
    if D[2]>0:
        xyz=xyz*[1,1,-1]
    if type(centre)==str:
        if centre.lower() == 'com':
            centre=getCoM(xyz,m)
    return xyz-centre

def XYZssettleDown(xyzs,idx=[0,1,2,3],centre=np.array([0,0,0]),m=None):
    settled=np.zeros(xyzs.shape)
    i=0
    for xyz in xyzs:
        settled[i]=XYZsettleDown(xyz,idx=idx,centre=centre,m=m)
        i+=1
    return settled


def XYZsettleDownWithV(xyz,v,idx=[0,1,2,3],centre=None,m=None):
    A,B,C,D=xyz[idx]
    xyz=xyz-A
    A,B,C,D=xyz[idx]
    M=alignVector(B,[1,0,0])
    xyz=M.dot(xyz.T).T
    v=M.dot(v.T).T
    A,B,C,D=xyz[idx]
    M=alignVector(np.cross(B,C),[0,0,1])
    xyz=M.dot(xyz.T).T
    v=M.dot(v.T).T
    A,B,C,D=xyz[idx]
    if centre is None:
        centre=getCoM(xyz,m)
    return xyz-centre,v

def readIC(ic):
    icdict={}
    icdict['idx']=[]
    icdict['d']=[]
    icdict['a']=[]
    icdict['da']=[]
    with open(ic) as f:
        for line in f:
            icdict['idx'].append([int(i)-1 for i in line.split()])
    icdict['d']=[[i[0],i[1]] for i in icdict['idx']]
    icdict['a']=[[i[0],i[1],i[2]] for i in icdict['idx']]
    icdict['da']=[[i[0],i[1],i[2],i[3]] for i in icdict['idx']]
    icdict['mask']=[len(icdict['idx'])*i+j for i in range(3) for j in range(len(icdict['idx'])) if i<j]
    icdict['maskV']=icdict['mask']+[i+len(icdict['mask'])+6 for i in icdict['mask']]+[-1]
    return icdict

def IDescr(xyz,dtype=np.float32):
    n=xyz.shape[-2]
    idescr=np.zeros((xyz.shape[0],n*(n-1)//2),dtype=dtype)
    k=0
    for i in range(n):
        for j in range(i+1,n):
            idescr[:,k]=1/np.linalg.norm(xyz[:,i]-xyz[:,j],axis=1)
            k+=1
    return idescr

# @tf.function(input_signature=[tf.TensorSpec(None, tf.float32)])
# def IDescrTF(xyz):
#     return tf.numpy_function(IDescr,[xyz],tf.float32)



def Describe(XYZ,V,icdict,xyzoffset='CoM',voffset='CoM',m=None,type='gIC'):
    if xyzoffset=='CoM':
        xyzoffset=getCoM(XYZ,m)
    if voffset=='CoM':
        voffset=getCoM(V,m)
    xyz=np.zeros((XYZ.shape[0],XYZ.shape[1]+3,XYZ.shape[2]))
    xyz[:,-3:]=refTrio
    xyz[:,:-3]=XYZ-xyzoffset
    v=np.zeros((XYZ.shape[0],XYZ.shape[1]+3,XYZ.shape[2]))
    v[:,-3:]=refTrioV
    v[:,:-3]=V-voffset
    d,a,da=icdict['d'],icdict['a'],icdict['da']
    l=len(d+a+da)
    x=np.zeros((xyz.shape[0],l*2))
    i=0
    for idx in d:
        x[:,[i]],x[:,[i+l]]=getDistancePara(xyz,v,idx)
        i+=1
    for idx in a:
        x[:,[i]],x[:,[i+l]]=getAnglePara(xyz,v,idx)
        i+=1
    for idx in da:
        x[:,[i]],x[:,[i+l]]=getDihedralPara(xyz,v,idx)
        i+=1
    return x

def getDistancePara(xyz,v,idx=[0,1]):
    A,B=np.transpose(xyz[:,idx],axes=(1,0,2))
    AB=B-A
    vA,vB=np.transpose(v[:,idx],axes=(1,0,2))
    d=normPara(AB)
    vd=dotPara(AB,vB-vA)/d
    return d,vd

def getAnglePara(xyz,v,idx=[0,1,2]):
    A,B,C=np.transpose(xyz[:,idx],axes=(1,0,2))
    BA=A-B
    BC=C-B
    theta=np.arccos(np.clip(dotPara(BA,BC)/normPara(BA)/normPara(BC),-1,1))
    vA,vB,vC=np.transpose(v[:,idx],axes=(1,0,2))
    ba=getDirectionPara(BA)
    bc=getDirectionPara(BC)
    n=np.cross(bc,ba)/normPara(np.cross(bc,ba))
    na=np.cross(ba,n)
    nc=np.cross(bc,n)
    omega=dotPara(vC-vB,nc)/normPara(BC)-dotPara(vA-vB,na)/normPara(BA)
    return theta,omega

def getDihedralPara(xyz,v,idx=[0,1,2,3]):
    A,B,C,D=np.transpose(xyz[:,idx],axes=(1,0,2))
    BA=A-B
    bc=getDirectionPara(C-B)
    CD=D-C
    a,d=BA-dotPara(BA,bc)*bc,CD-dotPara(CD,bc)*bc
    theta=np.arccos(np.clip(dotPara(a,d)/normPara(a)/normPara(d),-1,1))
    theta[dotPara(np.cross(a,d),bc)<0]*=-1
    na=np.cross(bc,a)/normPara(a)
    nd=np.cross(bc,d)/normPara(d)
    omega0=getOmegaPara(xyz[:,idx[-3:]],v[:,idx[-3:]])
    vA,_,_,vD=np.transpose(v[:,idx]-v[:,[idx[1]]]-np.cross(omega0[:,np.newaxis,:],xyz[:,idx]-xyz[:,[idx[1]]]),axes=(1,0,2))
    omega=dotPara(vD,nd)/normPara(d)-dotPara(vA,na)/normPara(a)
    return theta,omega

def unDescribeWithoutV(desc,icidx):
    l=len(icidx)
    xyz=np.repeat(np.concatenate((np.zeros((l,3),dtype=np.float32),refTrio))[np.newaxis],desc.shape[0],axis=0)
    for j in range(l):
        x=getDirectionPara(xyz[:,icidx[j][2]]-xyz[:,icidx[j][1]])
        z=getNormalPara(xyz[:,icidx[j][1]],xyz[:,icidx[j][2]],xyz[:,icidx[j][3]])
        xyz[:,icidx[j][0]]=rotate3Para(-x,desc[:,2*l+j],rotate3Para(z,desc[:,l+j],x*desc[:,[j]]))+xyz[:,icidx[j][1]]
    return xyz[:,:-3]

def unDescribe(desc,icidx):
    l=len(icidx)
    xyz=np.repeat(np.concatenate((np.zeros((l,3),dtype=np.float32),refTrio))[np.newaxis],desc.shape[0],axis=0)
    v=np.repeat(np.concatenate((np.zeros((l,3),dtype=np.float32),refTrioV))[np.newaxis],desc.shape[0],axis=0)
    for j in range(l):
        x=getDirectionPara(xyz[:,icidx[j][2]]-xyz[:,icidx[j][1]])
        z=getNormalPara(xyz[:,icidx[j][1]],xyz[:,icidx[j][2]],xyz[:,icidx[j][3]])
        xyz[:,icidx[j][0]]=rotate3Para(-x,desc[:,2*l+j],rotate3Para(z,desc[:,l+j],x*desc[:,[j]]))+xyz[:,icidx[j][1]]
    for j in range(l):
        A,B,C,D=np.transpose(xyz[:,[icidx[j][0],icidx[j][1],icidx[j][2],icidx[j][3]]],axes=(1,0,2))
        vB,vC,vD=np.transpose(v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],axes=(1,0,2))
        BA=A-B
        BC=C-B
        CD=D-C
        dd=getDirectionPara(BA)
        bc=getDirectionPara(BC)
        na=getDirectionPara(np.cross(bc,dd))
        da=np.cross(dd,na)
        dac=np.cross(bc,na)
        daa=BA-dotPara(BA,bc)*bc
        dad=CD-dotPara(CD,bc)*bc
        dda=np.cross(bc,daa)/normPara(daa)
        ddad=np.cross(bc,dad)/normPara(dad)
        omega=getOmegaPara(xyz[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]])
        v[:,icidx[j][0]]=dd*(desc[:,[3*l+j]]+dotPara(vB,dd))+da*(dotPara(vB,da)+normPara(BA)*(dotPara(vC-vB,dac)/normPara(BC)-desc[:,[4*l+j]]))+dda*(dotPara(vB+np.cross(omega,BA),dda)+normPara(daa)*(dotPara(ddad,(vD-vB)-np.cross(omega,D-B))/normPara(dad)-desc[:,[5*l+j]]))
    return xyz[:,:-3],v[:,:-3]


# def unDescribeParaTF(desc,icidx):
#     l=len(icidx)
#     xyz=np.repeat(np.concatenate((np.zeros((l,3),dtype=np.float32),refTrio))[np.newaxis],desc.shape[0],axis=0)
#     v=np.repeat(np.concatenate((np.zeros((l,3),dtype=np.float32),refTrioV))[np.newaxis],desc.shape[0],axis=0)
#     for j in range(l):
#         x=getDirectionPara(xyz[:,icidx[j][2]]-xyz[:,icidx[j][1]])
#         z=getNormalPara(xyz[:,icidx[j][1]],xyz[:,icidx[j][2]],xyz[:,icidx[j][3]])
#         xyz[:,icidx[j][0]]=rotate3ParaTF(-x,desc[:,2*l+j],rotate3ParaTF(z,desc[:,l+j],x*desc[:,[j]]))+xyz[:,icidx[j][1]]
#     for j in range(l):
#         A,B,C,D=np.transpose(xyz[:,[icidx[j][0],icidx[j][1],icidx[j][2],icidx[j][3]]],axes=(1,0,2))
#         vB,vC,vD=np.transpose(v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],axes=(1,0,2))
#         BA=A-B
#         BC=C-B
#         CD=D-C
#         dd=getDirectionPara(BA)
#         bc=getDirectionPara(BC)
#         na=getDirectionPara(np.cross(bc,dd))
#         da=np.cross(dd,na)
#         dac=np.cross(bc,na)
#         daa=BA-dotPara(BA,bc)*bc
#         dad=CD-dotPara(CD,bc)*bc
#         dda=np.cross(bc,daa)/normPara(daa)
#         ddad=np.cross(bc,dad)/normPara(dad)
#         omega=getOmegaPara(xyz[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]])
#         v[:,icidx[j][0]]=dd*(desc[:,[3*l+j]]+dotPara(vB,dd))+da*(dotPara(vB,da)+normPara(BA)*(dotPara(vC-vB,dac)/normPara(BC)-desc[:,[4*l+j]]))+dda*(dotPara(vB+np.cross(omega,BA),dda)+normPara(daa)*(dotPara(ddad,(vD-vB)-np.cross(omega,D-B))/normPara(dad)-desc[:,[5*l+j]]))
#     return xyz[:,:-3],v[:,:-3]

# def rotate3ParaTF(axis,theta,vector):
#     c=np.cos(theta.astype(np.float64))
#     v=getDirectionPara(axis)*np.sin(theta)[:,np.newaxis]
#     vx=np.zeros((v.shape[0],3,3))
#     vx[:,0,1]=-v[:,2]
#     vx[:,0,2]=v[:,1]
#     vx[:,1,0]=v[:,2]
#     vx[:,1,2]=-v[:,0]
#     vx[:,2,0]=-v[:,1]
#     vx[:,2,1]=v[:,0]
#     return ((np.identity(3)+vx+vx@vx/(1+c)[:,np.newaxis,np.newaxis])@(vector[:,:,np.newaxis]))[:,:,0]

def rotate3Para(axis,theta,vector):
    M=np.array(list(map(scipy.linalg.expm,np.transpose(np.cross(np.eye(3)[:,np.newaxis],axis/normPara(axis)*theta[:,np.newaxis]),axes=(1,0,2)))))
    return np.einsum('ijk,ik->ij',M,vector)

def normPara(a):
    return np.linalg.norm(a,axis=-1)[:,np.newaxis]

def dotPara(a,b):
    return np.einsum('ij,ij->i',a,b)[:,np.newaxis]

def getDirectionPara(a):
    return (a)/normPara(a)

def getNormalPara(a,b,c):
    n=np.cross(b-a,c-b)
    return n/normPara(n)

def getOmegaPara(ABC,vABC):
    A,B,C=np.transpose(ABC,axes=(1,0,2))
    va,vb,vc=np.transpose(vABC,axes=(1,0,2))
    AB=B-A
    AC=C-A
    ab=getDirectionPara(AB)
    ac=getDirectionPara(AC)
    n=np.cross(ab,ac)
    nn=np.cross(n,ab)
    ACnn=dotPara(AC,nn)*nn
    omegab=np.cross(AB,vb-va)/normPara(AB)**2
    omegac=(np.cross(ACnn,dotPara(vc-va,n)*n-dotPara(np.cross(omegab,AC),n)*n)/normPara(ACnn)**2)
    return omegab+omegac

# @tf.function(input_signature=[tf.TensorSpec(None, tf.float32),tf.TensorSpec(None, tf.float32)])
# def getDirectionTF(a,b=None):
#     return tf.numpy_function(getDirection,[a,b],tf.float32)

# @tf.function(input_signature=[tf.TensorSpec(None, tf.float32),tf.TensorSpec(None, tf.int32)])
# def unDescribeTF(desc,icidx):
#     return tf.numpy_function(unDescribeParaTF,[desc,icidx],[tf.float32,tf.float32])

def getMmatrix(descr,m,icdict):
    l=descr.shape[-1]//2
    idx=[i[0] for i in icdict['idx']]
    m=np.repeat([m[idx]],3,axis=0).flatten()
    mm=np.zeros((l,l))

def correctAngle(x,y,idx=[15,16,17,20]):
    mask=(x[:,idx]*y[:,idx] < 0)&(np.abs(x[:,idx])>np.pi/2)&(np.abs(y[:,idx])>np.pi/2)
    y[:,idx]+=(2*np.pi*x[:,idx]/np.abs(x[:,idx]))*mask


def correctAngle_recursive(x,y,idx=[15,16,17,20]):
    for a in idx:
        for i in range(x.shape[0]):
            for j in range(y.shape[1]):
                if x[i,-1,a]*y[i,j,a] < 0 and np.abs(x[i,-1,a])>np.pi/2:
                    y[i,j,a]+=2*np.pi*x[i,-1,a]/np.abs(x[i,-1,a])

def theOppositeWayToCorrectAngle(y,idx=[15,16,17,20]):
    y[:,idx]=(np.pi+y[:,idx])%(2*np.pi)-np.pi

def chimeraPredict(models,x,tc=np.inf,standing=0.5):
    ys=[]
    for model in models:
        y=predict(model,x,tc)[0]
        if np.sum(np.isnan(y)) == 0:
            ys.append(y)
    ys=np.array(ys)
    print(ys.shape)
    h,w=ys.shape
    i=h*standing//1
    l=w//2
    selection=np.tile(np.abs(ys[:,l:]).argsort(axis=0).argsort(axis=0)==i,2)
    return np.array([ys.T[selection.T].T])

def ND(x,dt=1):
    v=[]
    for i in range(len(x)-2):
        v.append((x[i+2]-x[i])/2/dt)
    return np.array(v)

refTrioTorch=torch.tensor(refTrio)
refTrioVTorch=torch.tensor(refTrioV)
def unDescribeTorch(desc,icidx,device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    l=len(icidx)
    xyz=torch.repeat_interleave(torch.cat((torch.zeros((l,3)),refTrioTorch))[None],desc.shape[0],dim=0).to(device)
    v=torch.repeat_interleave(torch.cat((torch.zeros((l,3)),refTrioVTorch))[None],desc.shape[0],dim=0).to(device)
    for j in range(l):
        x=getDirectionParaTorch(xyz[:,icidx[j][2]]-xyz[:,icidx[j][1]])
        z=getNormalParaTorch(xyz[:,icidx[j][1]],xyz[:,icidx[j][2]],xyz[:,icidx[j][3]])
        xyz[:,icidx[j][0]]=rotate3ParaTorch(-x,desc[:,2*l+j],rotate3ParaTorch(z,desc[:,l+j],x*desc[:,[j]]))+xyz[:,icidx[j][1]]
    for j in range(l):
        A,B,C,D=torch.transpose(xyz[:,[icidx[j][0],icidx[j][1],icidx[j][2],icidx[j][3]]],0,1)
        vB,vC,vD=torch.transpose(v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],0,1)
        BA=A-B
        BC=C-B
        CD=D-C
        dd=getDirectionParaTorch(BA)
        bc=getDirectionParaTorch(BC)
        na=getDirectionParaTorch(torch.linalg.cross(bc,dd))
        da=torch.linalg.cross(dd,na)
        dac=torch.linalg.cross(bc,na)
        daa=BA-dotParaTorch(BA,bc)*bc
        dad=CD-dotParaTorch(CD,bc)*bc
        dda=torch.linalg.cross(bc,daa)/normParaTorch(daa)
        ddad=torch.linalg.cross(bc,dad)/normParaTorch(dad)
        omega=getOmegaParaTorch(xyz[:,[icidx[j][1],icidx[j][2],icidx[j][3]]],v[:,[icidx[j][1],icidx[j][2],icidx[j][3]]])
        v[:,icidx[j][0]]=dd*(desc[:,[3*l+j]]+dotParaTorch(vB,dd))+da*(dotParaTorch(vB,da)+normParaTorch(BA)*(dotParaTorch(vC-vB,dac)/normParaTorch(BC)-desc[:,[4*l+j]]))+dda*(dotParaTorch(vB+torch.linalg.cross(omega,BA),dda)+normParaTorch(daa)*(dotParaTorch(ddad,(vD-vB)-torch.linalg.cross(omega,D-B))/normParaTorch(dad)-desc[:,[5*l+j]]))
    return xyz[:,:-3],v[:,:-3]

def unDescribeTorchNoV(desc,icidx,device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    l=len(icidx)
    xyz=torch.repeat_interleave(torch.cat((torch.zeros((l,3)),refTrioTorch))[None],desc.shape[0],dim=0).to(device)
    for j in range(l):
        x=getDirectionParaTorch(xyz[:,icidx[j][2]]-xyz[:,icidx[j][1]])
        z=getNormalParaTorch(xyz[:,icidx[j][1]],xyz[:,icidx[j][2]],xyz[:,icidx[j][3]])
        xyz[:,icidx[j][0]]=rotate3ParaTorch(-x,desc[:,2*l+j],rotate3ParaTorch(z,desc[:,l+j],x*desc[:,[j]],device=device),device=device)+xyz[:,icidx[j][1]]
    return xyz[:,:-3]

def rotate3ParaTorch(axis,theta,vector,device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    M=torch.linalg.matrix_exp(torch.transpose(torch.linalg.cross(torch.eye(3).to(device)[:,None],normalize(axis)*theta[:,None]),0,1))
    return torch.einsum('ijk,ik->ij',M,vector)

def normParaTorch(x):
    return torch.norm(x,dim=-1,keepdim=True)

def dotParaTorch(a,b):
    return torch.sum(a*b,dim=-1,keepdim=True)

def normalize(x):
    return x/normParaTorch(x)

def getDirectionParaTorch(a):
    return (a)/normParaTorch(a)

def getNormalParaTorch(a,b,c):
    n=torch.linalg.cross(b-a,c-b)
    return n/normParaTorch(n)

def getOmegaParaTorch(ABC,vABC):
    A,B,C=torch.transpose(ABC,0,1)
    va,vb,vc=torch.transpose(vABC,0,1)
    AB=B-A
    AC=C-A
    ab=normalize(AB)
    ac=normalize(AC)
    n=torch.linalg.cross(ab,ac)
    nn=torch.linalg.cross(n,ab)
    ACnn=dotParaTorch(AC,nn)*nn
    omegab=torch.linalg.cross(AB,vb-va)/normParaTorch(AB)**2
    omegac=(torch.linalg.cross(ACnn,dotParaTorch(vc-va,n)*n-dotParaTorch(torch.linalg.cross(omegab,AC),n)*n)/normParaTorch(ACnn)**2)
    return omegab+omegac

def getEkTorch(v,m):
    return 0.5*torch.sum(m[:,None]*v**2,dim=(-2,-1))/0.529177210903/0.529177210903*1822.888515*24.188843265e-3*24.188843265e-3 

def DescribeTorch(XYZ,d,a,da,xyzoffset='CoM',voffset='CoM',m=None):
    if xyzoffset=='CoM':
        xyzoffset=getCoMtorch(XYZ,m)
    xyz=torch.zeros((XYZ.shape[0],XYZ.shape[1]+3,XYZ.shape[2]))
    xyz[:,-3:]=refTrioTorch
    xyz[:,:-3]=XYZ-xyzoffset
    # d,a,da=icdict['d'],icdict['a'],icdict['da']
    l=len(a)*3
    x=torch.zeros((xyz.shape[0],l))
    i=0
    for idx in d:
        x[:,[i]]=getDistanceTorch(xyz,idx)
        i+=1
    for idx in a:
        x[:,[i]]=getAngleTorch(xyz,idx)
        i+=1
    for idx in da:
        x[:,[i]]=getDihedralTorch(xyz,idx)
        i+=1
    return x

def getCoMtorch(xyz,m=None):
    if m is None:
        m=torch.ones(xyz.shape[-2])
    return torch.sum(xyz*m[:,None],dim=-2,keepdim=True)/torch.sum(m)

def getDistanceTorch(xyz,idx=[0,1]):
    A,B=torch.transpose(xyz[:,idx],0,1)
    AB=B-A
    d=normParaTorch(AB)
    return d

def getAngleTorch(xyz,idx=[0,1,2]):
    A,B,C=torch.transpose(xyz[:,idx],0,1)
    BA=A-B
    BC=C-B
    theta=torch.arccos(torch.clamp(dotParaTorch(BA,BC)/normParaTorch(BA)/normParaTorch(BC),-1,1))
    return theta

def getDihedralTorch(xyz,idx=[0,1,2,3]):
    A,B,C,D=torch.transpose(xyz[:,idx],0,1)
    BA=A-B
    bc=normalize(C-B)
    CD=D-C
    a,d=BA-dotParaTorch(BA,bc)*bc,CD-dotParaTorch(CD,bc)*bc
    theta=torch.arccos(torch.clamp(dotParaTorch(a,d)/normParaTorch(a)/normParaTorch(d),-1,1))
    theta[dotParaTorch(torch.linalg.cross(a,d),bc)<0]*=-1
    return theta

def getGradIC(gradXYZ,ic,icdict):
    ic=torch.tensor(ic).requires_grad_(True)
    gradXYZ=torch.flatten(torch.tensor(gradXYZ),start_dim=1)[...,None]
    xyz=torch.flatten(torch.unDescribeTorchNoV(ic,torch.tensor(icdict['idx']),device=torch.device('cpu')),start_dim=1)
    jac=batch_jacobian(xyz,ic)
    gradic=torch.sum(gradXYZ*jac,dim=1)
    return gradic

def getAngMtorch(xyz,v,m,center=None):
    if center is None:
        centered=xyz-torch.expand_dims(getCoM(xyz,m),dim=-2)
    else:
        centered=xyz-center
    L=torch.sum(m[:,None]*torch.linalg.cross(centered,v),dim=-2)
    return L

def getMomentOfInertiaTensorTorch(xyz,m,center=None,device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    if center is None:
        center=getCoM(xyz,m)
    centered=xyz-center
    if len(xyz.shape)==2:
        I=torch.zeros((3,3)).to(device)
        for i in range(3):
            for j in range(3):
                for k in range(len(m)):
                    I[i,j]+=m[k]*(torch.sum(centered[k]**2)-centered[k,i]*centered[k,j]) if i==j else m[k]*(-centered[k,i]*centered[k,j])
    if len(xyz.shape)==3:
        I=torch.zeros((xyz.shape[0],3,3)).to(device)
        for i in range(3):
            for j in range(3):
                for k in range(len(m)):
                    I[:,i,j]+=m[k]*(torch.sum(centered[:,k]**2,dim=1)-centered[:,k,i]*centered[:,k,j]) if i==j else m[k]*(-centered[:,k,i]*centered[:,k,j])
    return I

def adjVtorch(xyz,v,m,device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
    center=getCoMtorch(xyz,m)
    L0=getAngMtorch(xyz,v,m,center)
    I=getMomentOfInertiaTensorTorch(xyz,m,center,device)
    omega=torch.linalg.inv(I)@L0[...,None]
    return v-torch.linalg.cross(omega.transpose(-2,-1),xyz-center)-getCoMtorch(v,m)