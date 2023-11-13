from gettext import find
from .utils import *
from .functions4Dtf import *
import sys
import time
import json
from .args_class import ArgsBase
from pyh5md import File, element
from . import stopper

class Args(ArgsBase):
    def __init__(self):
        super().__init__()
        self.add_default_dict_args([
            'create4Dmodel','use4Dmodel','estAcc4Dmodel','MLmodelIn','reactionPath','MD','activeLearning'
            ],
            bool
        )
        self.add_default_dict_args([
            'trajsList',
            'trajEpot',
            'ICidx',
            'mlmodelin',
            'mlmodelsin'
            ],
            ""
        )        
        self.add_dict_args({
            'mlmodelout': "4D_model",
            'nthreads': None,
            'initXYZ':'',
            'initVXYZ':'',
            'trun':1000,
            'finalXYZ':'',
            'initVout':'',
            'reactionTime':10,
            'trajXYZout':'traj.xyz',
            'trajVXYZout':'traj.vxyz',
            'trajTime':'traj.t',
            'trajH5MDout':'traj.h5',
            'trajEpot':'traj.epot',
            'trajEkin':'traj.ekin',
            'trajEtot':'traj.etot',
            'trajDescr':'traj.y',
            'tc':10,
            'tSegm':'tc',
            'dt':'tc',
            'Trajs':[]
        })
        self.parse_input_content([
            "FourD.ICdict=0",
            'FourD.tmax=0',
            'FourD.use3D=1',
            'FourD.reuseData=0',
            'FourD.reuse3D=0',
            'FourD.reuse4D=0',
            'FourD.tc=0',
            'Nsubtrain=0.9',
            'Nvalidate=0.05',
            'NNvalidate=0',
            'NNsubtrain=0',
            'FourD.initFreq=tc',
            'FourD.batchSize3D=16',
            'FourD.batchSize4D=16',
            'FourD.maxEpoch3D=4096',
            'FourD.maxEpoch4D=4096',
            'FourD.MD.subDirOut=4DMD',
            'FourD.reactionPath.subDirOut=4Dreaction',
            "FourD.m2vbar=0",
            "FourD.m2dm=0",
            "FourD.logisticateT=0",
            "FourD.normalizeT=1",
            'FourD.Descriptor=ic',
            'FourD.Descriptor3D=0',
            'FourD.xList=Descriptor',
            'FourD.yList=Descriptor,ep',
            'FourD.monarchWings=0',
            'FourD.adaptSeg=0',
            'FourD.forceEtot=0',
            'FourD.learnSeg=0',
            'FourD.checkEk=0',
            'FourD.checkV0=0',
            ])
        self.meta={
            "descriptor":{},
            "data":{},
            "3Dmodel":{},
            "4Dmodel":{}
        }
    def parse(self, argsraw):
        self.args2pass=argsraw
        self.parse_input_content(argsraw)
        self.argProcess()

    def argProcess(self):
        if self.MLmodelsIn:
            self.MLmodelIn=self.MLmodelsIn.split(',')[0]
        if self.MLmodelIn and not self.activeLearning:
            with open(f'{self.MLmodelIn}/meta.json') as f: self.meta=json.load(f)
            self.FourD.tc=self.meta['4Dmodel']['Tc']
            self.FourD.Descriptor=self.meta['descriptor']['type']
            self.FourD.ICdict=self.meta['descriptor']['ICdict']
            self.FourD.M2dM=self.meta['descriptor']['M2dM']
            self.FourD.M2Vbar=self.meta['descriptor']['M2Vbar']
            self.FourD.logisticateT=self.meta['descriptor']['logisticateT']
            self.FourD.normalizeT=self.meta['descriptor']['normalizeT']
            try:
                self.FourD.Descriptor3D=self.meta['descriptor3D']['type']
            except:
                pass
            # (f'{self.MLmodelIn}/ICidx')
        # if not self.FourD.Descriptor3D:
        #     self.FourD.Descriptor3D=self.FourD.Descriptor
        if not self.FourD.tc: self.FourD.tc=self.tc
        if self.FourD.initFreq=='tc':
            self.FourD.initFreq=self.FourD.tc
        self.ICidx=self.ICidx.split(',')
        if len(self.ICidx)==1:
            self.ICidx=self.ICidx*4
        if self.FourD.Descriptor.lower()=='ic' and not self.FourD.ICdict: self.FourD.ICdict=readIC(self.ICidx[0]) 
        else: self.FourD.ICdict={}
        if self.tSegm=='tc':
            self.tSegm=self.FourD.tc
        if self.dt=='tc':
            self.dt=self.FourD.tc
        
        if self.trajsList:
            with open(self.trajsList) as f:
                for line in f:
                    self.Trajs.append(line.strip())
        elif self.Trajs:
            self.Trajs=self.Trajs.split(',')

        if not self.nthreads:
            self.nthreads=os.cpu_count()

        if self.create4Dmodel:
            if self.FourD.reuseData or self.FourD.reuse3D or self.FourD.reuse4D:
                with open(f'{self.MLmodelOut}/meta.json') as f:
                    self.meta=json.load(f)
            else: 
                os.system(f'mkdir {self.mlmodelout}')
               
            self.writeMeta()

    def writeMeta(self):
        if not self.FourD.reuseData:
            self.meta['descriptor']['type']=self.FourD.Descriptor
            self.meta['descriptor']['xList']=self.FourD.xList.split(',')
            self.meta['descriptor']['yList']=self.FourD.yList.split(',')
            self.meta['descriptor']['ICdict']=dict(self.FourD.ICdict)
            self.meta['descriptor']['3D']=self.FourD.Descriptor3D
            self.meta['data']['trajs']=self.Trajs
            self.meta['data']['Nsubtrain']=self.Nsubtrain
            self.meta['data']['Nvalidate']=self.Nvalidate
            self.meta['data']['Tmax']=self.FourD.tmax
        if not self.FourD.reuse3D:
            self.meta['3Dmodel']['use']=self.FourD.use3D
            if self.meta['3Dmodel']['use']: self.meta['3Dmodel']['batchSize']=self.FourD.batchSize3D
        if not self.FourD.reuse4D:
            self.meta['4Dmodel']['batchSize']=self.FourD.batchSize4D
            self.meta['4Dmodel']['Tc']=self.FourD.tc
        self.meta['descriptor']['M2Vbar']=self.FourD.M2Vbar
        self.meta['descriptor']['M2dM']=self.FourD.M2dM
        self.meta['descriptor']['logisticateT']=self.FourD.logisticateT
        self.meta['descriptor']['normalizeT']=self.FourD.normalizeT

        with open(f'{self.mlmodelout}/meta.json','w') as f:
            # def printtype(d,i=""):
            #     for k,v in d.items():
            #         if type(v)==dict:
            #             print(i,k,type(v))
            #             printtype(v,i+"    ")
            #         elif type(v)==list:
            #             print(i,k,[type(j) for j in v])
            #         else: print(i,k,type(v))
            # printtype(self.meta)
            json.dump(self.meta,f,indent=4)
                
            
class FourDcls(object):
    def __init__(self, args4D,devices=None,msg='') -> None:
        self.args = Args()
        self.args.parse(args4D)
        self.model3D=None
        self.model=None
        self.x=None
        self.y=None
        self.xEx=None
        self.yEx=None
        
        self.x3D=None
        self.y3D=None
        self.xEx3D=None
        self.yEx3D=None
        self.masses=None
        
        self.loss3D=np.inf
        self.loss4D=np.inf
        self.losses4D=None

        self.epoch3D=0
        self.epoch4D=0

        self.normalizeTfactor=0.32
        # self.xlist=['Descriptor','ep','ek']
        
        self.msg=msg
        # if type(devices) == str:
        #     self.strategy = tf.distribute.OneDeviceStrategy(devices)
        # else:
        self.strategy = tf.distribute.MirroredStrategy(devices)
        

        self.init_lr=0.001
        self.decay_steps=8192
        self.decay_rate=0.99
        self.lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=self.init_lr,
            decay_steps=self.decay_steps,
            decay_rate=self.decay_rate)

        if self.args.MLmodelIn:
            self.masse=self.args.meta['masses']
            if self.args.meta['3Dmodel']['use']:
                self.model3D= tf.keras.models.load_model(f'{self.args.mlmodelin}/3D_model',compile=False)  
                self.epoch3D=self.args.meta['3Dmodel']['Epoch']
                self.loss3D=self.args.meta['3Dmodel']['loss']
            self.model=tf.keras.models.load_model(f'{self.args.mlmodelin}/4D_model',compile=False)
            self.epoch4D=self.args.meta['4Dmodel']['Epoch']
            self.losses4D=tuple(self.args.meta['4Dmodel']['losses'])
            self.loss4D=self.losses4D[-1]

        if self.args.MLmodelsIn:
            self.model3Ds=[]
            self.models=[]
            for model in self.args.MLmodelsIn.split(','):
                self.model3Ds.append(tf.keras.models.load_model(f'{model}/3D_model',compile=False))
                self.models.append(tf.keras.models.load_model(f'{model}/4D_model',compile=False))
            self.model3D=lambda x: tf.reduce_mean([m3D(x) for m3D in self.model3Ds],axis=0)

    
    def prepareData(self):
        args=self.args
        global getDataFromTraj

        def getDataFromTraj(traj):
            if traj[-4:]=='.npz':
                dataset=dict(np.load(traj))
            elif traj[-3:]=='.h5':
                with File(traj,'r') as f:
                    dataset={}
                    dataset['xyz']=f['particles/all/position/value'][()]
                    dataset['t']=f['particles/all/position/time'][()].reshape(-1,1)
                    dataset['v']=f['particles/all/velocities/value'][()]
                    dataset['ep']=f['observables/potential_energy/value'][()].reshape(-1,1)
                    dataset['ek']=f['observables/kinetic_energy/value'][()].reshape(-1,1)
                    steps=min(len(dataset['xyz']),len(dataset['v']),len(dataset['ep']))
                    for k,v in dataset.items():
                        dataset[k]=v[:steps]
            else:
                print('unknown traj file type')
                return
            
            if args.FourD.tmax:
                tmax=args.FourD.tmax
            else:
                tmax=np.max(dataset['t'])
            
            mask=dataset['t'][:,0]<=tmax
            for k,v in dataset.items():
                try: 
                    dataset[k]=v[mask]
                except: 
                    # print(f" problem with {traj}'s {k}")
                    pass
            
            if 'et' in args.FourD.xlist+args.FourD.ylist:
                dataset['et']=dataset['ek']+dataset['ep']
            if 'deltaE' in args.FourD.xlist+args.FourD.ylist:
                dataset['deltaE']=np.zeros_like(dataset['ek'])
            if args.FourD.Descriptor.lower()=='ic':
                dataset['Descriptor']=Describe(dataset['xyz'],dataset['v'],args.FourD.ICdict,m=self.masses)
            elif args.FourD.Descriptor.lower()=='xyz':
                dataset['Descriptor']=np.concatenate((dataset['xyz'],dataset['v']),axis=1).reshape(dataset['xyz'].shape[0],-1)
            x,y=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*args.Nsubtrain,0,step=1)
            # xEx,yEx=getData(dataset,xlist,ylist,args.FourD.tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
            xEx,yEx=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
            if 'deltaE' in args.FourD.xlist+args.FourD.ylist:
                ek0=getEks(dataset['v'],dataset['m'][0])
                dataset['v']+=np.random.normal(0,0.01,dataset['v'].shape)
                ek1=getEks(dataset['v'],dataset['m'][0])
                dataset['deltaE']=ek1-ek0
                xx,yy=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*args.Nsubtrain,0,step=1)
                xxEx,yyEx=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
                x=np.concatenate((x,xx),axis=0)
                y=np.concatenate((y,yy),axis=0)
                xEx=np.concatenate((xEx,xxEx),axis=0)
                yEx=np.concatenate((yEx,yyEx),axis=0)
            if not args.FourD.Descriptor3D:
                x3D=dataset['Descriptor'][:,:dataset['Descriptor'].shape[1]//2]
            elif args.FourD.Descriptor3D.lower()=='id':
                x3D=IDescr(dataset['xyz'])
            y3D=dataset['ep']


            
            print('described')
            xs[traj]=x
            ys[traj]=y
            xExs[traj]=xEx
            yExs[traj]=yEx
            x3Ds[traj]=x3D
            y3Ds[traj]=y3D

        if args.FourD.reuseData:
            x=np.load(f'{args.mlmodelout}/x.npy')
            y=np.load(f'{args.mlmodelout}/y.npy')
            xEx=np.load(f'{args.mlmodelout}/xEx.npy')
            yEx=np.load(f'{args.mlmodelout}/yEx.npy')
            x3D=np.load(f'{args.mlmodelout}/x3D.npy')
            y3D=np.load(f'{args.mlmodelout}/y3D.npy')
            
        else:
            if args.Trajs[0][-4:]=='.npz':
                self.masses=dict(np.load(args.Trajs[0]))['m'][0]
            elif args.Trajs[0][-3:]=='.h5':
                with File(args.Trajs[0],'r') as f:
                    self.masses=f['particles/all/mass'][()]
            args.meta['masses']=list(self.masses.astype(float))
            args.meta['descriptor']['length']=len(args.meta['masses'])*6
            args.writeMeta()

            manager = Manager()
            xs=manager.dict()
            ys=manager.dict()
            xExs=manager.dict()
            yExs=manager.dict()
            x3Ds=manager.dict()
            y3Ds=manager.dict()

            print(' preparing data...')
            pool = Pool(args.nthreads)
            pool.map(getDataFromTraj,args.Trajs)
            pool.close()
            x=np.concatenate([xs[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            y=np.concatenate([ys[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            xEx=np.concatenate([xExs[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            yEx=np.concatenate([yExs[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            x3D=np.concatenate([x3Ds[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            y3D=np.concatenate([y3Ds[traj] for traj in args.Trajs], axis=0).astype(np.float32)
            np.save(f'{args.mlmodelout}/x.npy',x)
            np.save(f'{args.mlmodelout}/y.npy',y)
            np.save(f'{args.mlmodelout}/xEx.npy',xEx)
            np.save(f'{args.mlmodelout}/yEx.npy',yEx)
            np.save(f'{args.mlmodelout}/x3D.npy',x3D)
            np.save(f'{args.mlmodelout}/y3D.npy',y3D)


        x,y=shuffle(x,y)
        xEx,yEx=shuffle(xEx,yEx)
        x3D,y3D=shuffle(x3D,y3D)

        if args.NNvalidate:
            xEx,yEx=xEx[:args.NNvalidate],yEx[:args.NNvalidate]
        if args.NNsubtrain:
            x,y=x[:args.NNsubtrain],y[:args.NNsubtrain]

        l=args.meta['descriptor']['length']//2

        xEx3D=x3D[y.shape[0]:]
        yEx3D=y3D[y.shape[0]:]
        x3D=x3D[:y.shape[0]]
        y3D=y3D[:y.shape[0]]
        
        if args.FourD.reuse3D:
            m_shift=args.meta['3Dmodel']['m_shift']
            m_scale=args.meta['3Dmodel']['m_scale']
            ep_shift=args.meta['3Dmodel']['ep_shift']
            ep_scale=args.meta['3Dmodel']['ep_scale']
        else:
            m_shift=np.mean(x3D,axis=0)
            m_scale=np.std(x3D,axis=0)
            # m_shift=np.zeros_like(m_shift)
            # m_scale=np.ones_like(m_scale)
            ep_shift=np.mean(y3D)
            ep_scale=np.std(y3D)
            args.meta['3Dmodel']['m_shift']=list(m_shift.astype(float))
            args.meta['3Dmodel']['m_scale']=list(m_scale.astype(float))
            args.meta['3Dmodel']['ep_shift']=float(ep_shift)
            args.meta['3Dmodel']['ep_scale']=float(ep_scale)
            args.writeMeta()

        x3D-=m_shift
        x3D/=m_scale
        y3D-=ep_shift
        y3D/=ep_scale
        xEx3D-=m_shift
        xEx3D/=m_scale
        yEx3D-=ep_shift
        yEx3D/=ep_scale


        if args.FourD.Descriptor.lower()=='ic':
            la=int(l/3)
            ld=la

            print("     correcting angles...")
            correctAngle(x,y,idx=list(range(ld,l)))
            correctAngle(xEx,yEx,idx=list(range(ld,l)))
            
        if args.FourD.normalizeT:
            print("     normalized by time")
            x,y=normalizeT(x,y,l=l,a=self.normalizeTfactor)
            xEx,yEx=normalizeT(xEx,yEx,l=l,a=self.normalizeTfactor)

        elif args.FourD.m2vbar:
            print('     learning average velocities of descriptors')
            x,y=M2Vbar(x,y)
            xEx,yEx=M2Vbar(xEx,yEx)

        elif args.FourD.m2dm:
            print('     learning differences of descriptors')
            x,y=M2dM(x,y)
            xEx,yEx=M2dM(xEx,yEx)

        elif args.FourD.logisticatet:
            print("     time normalized with logistic function")
            x,y=logisticateT(x,y)
            xEx,yEx=logisticateT(xEx,yEx)
        if args.FourD.reuse4D:
            x_shift=args.meta['4Dmodel']['x_shift']
            x_scale=args.meta['4Dmodel']['x_scale']
            y_shift=args.meta['4Dmodel']['y_shift']
        else:
            x_shift=np.mean(x,axis=0)
            x_scale=np.std(x,axis=0)
            y_shift=np.mean(y,axis=0)
            # if args.FourD.M2dM or args.FourD.normalizeT:
            #     x_shift[:]=0
            #     x_scale[:]=1
            #     y_shift[:]=0
            
            x_shift[:]=0
            x_scale[:]=1
            y_shift[:]=0
            args.meta['4Dmodel']['x_shift']=list(x_shift.astype(float))
            args.meta['4Dmodel']['x_scale']=list(x_scale.astype(float))
            args.meta['4Dmodel']['y_shift']=list(y_shift.astype(float))
            args.writeMeta()

        x-=x_shift
        x/=x_scale
        y-=y_shift
        xEx-=x_shift
        xEx/=x_scale
        yEx-=y_shift

        
        # np.save('4Dtest/xx.npy',xEx)
        # np.save('4Dtest/yy.npy',yEx)


        self.m_shift=m_shift
        self.m_scale=m_scale
        self.ep_shift=ep_shift
        self.ep_scale=ep_scale
        self.x_shift=x_shift
        self.x_scale=x_scale
        self.y_shift=y_shift

        self.x,self.y=x,y
        self.xEx,self.yEx=xEx,yEx
        self.x3D,self.y3D=x3D,y3D
        self.xEx3D,self.yEx3D=xEx3D,yEx3D

    def appendData(self,traj):
        args=self.args
        l=args.meta['descriptor']['length']//2
        m_shift=self.m_shift
        m_scale=self.m_scale
        ep_shift=self.ep_shift
        ep_scale=self.ep_scale
        x_shift=self.x_shift
        x_scale=self.x_scale
        y_shift=self.y_shift

        if traj[-4:]=='.npz':
            dataset=dict(np.load(traj))
        elif traj[-3:]=='.h5':
            with File(traj,'r') as f:
                dataset={}
                dataset['xyz']=f['particles/all/position/value'][()]
                dataset['t']=f['particles/all/position/time'][()]
                dataset['v']=f['particles/all/velocities/value'][()]
                dataset['ep']=f['observables/potential_energy/value'][()]
                dataset['ek']=f['observables/kinetic_energy/value'][()]
                steps=min(len(dataset['xyz']),len(dataset['v']),len(dataset['ep']))
                for k,v in dataset.items():
                    dataset[k]=v[:steps]
        else:
            print('unknown traj file type')
            return
        if args.FourD.Descriptor.lower()=='ic':
            dataset['Descriptor']=Describe(dataset['xyz'],dataset['v'],args.FourD.ICdict,m=self.masses)
        elif args.FourD.Descriptor.lower()=='xyz':
            dataset['Descriptor']=np.concatenate((dataset['xyz'],dataset['v']),axis=1).reshape(dataset['xyz'].shape[0],-1)
        tmax=np.max(dataset['t'])
        x,y=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*args.Nsubtrain,0,step=1,mode='dense')
        xEx,yEx=getData(dataset,self.xlist,self.ylist,args.FourD.tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1,mode='dense')
        
        l=args.meta['descriptor']['length']//2
        ya=np.concatenate((y,yEx))
        ya,_=shuffle(ya,ya)
        x3D=ya[:y.shape[0],:l]
        y3D=ya[:y.shape[0],[-1]]
        xEx3D=ya[y.shape[0]:,:l]
        yEx3D=ya[y.shape[0]:,[-1]]
        x3D-=m_shift
        x3D/=m_scale
        y3D-=ep_shift
        y3D/=ep_scale
        xEx3D-=m_shift
        xEx3D/=m_scale
        yEx3D-=ep_shift
        yEx3D/=ep_scale

        if args.FourD.Descriptor.lower()=='ic':
            la=int(l/3)
            ld=la

            print("     correcting angles...")
            correctAngle(x,y,idx=list(range(ld,l)))
            correctAngle(xEx,yEx,idx=list(range(ld,l)))
            
        if args.FourD.normalizeT:
            print("     normalized by time")
            x,y=normalizeT(x,y,l=l,a=self.normalizeTfactor)
            xEx,yEx=normalizeT(xEx,yEx,l=l,a=self.normalizeTfactor)

        elif args.FourD.m2vbar:
            print('     learning average velocities of descriptors')
            x,y=M2Vbar(x,y)
            xEx,yEx=M2Vbar(xEx,yEx)

        elif args.FourD.m2dm:
            print('     learning differences of descriptors')
            x,y=M2dM(x,y)
            xEx,yEx=M2dM(xEx,yEx)

        elif args.FourD.logisticatet:
            print("     time normalized with logistic function")
            x,y=logisticateT(x,y)
            xEx,yEx=logisticateT(xEx,yEx)

        x-=x_shift
        x/=x_scale
        y-=y_shift
        xEx-=x_shift
        xEx/=x_scale
        yEx-=y_shift

        x=np.concatenate((self.x,x)).astype(np.float32)
        xEx=np.concatenate((self.xEx,xEx)).astype(np.float32)
        x3D=np.concatenate((self.x3D,x3D)).astype(np.float32)
        xEx3D=np.concatenate((self.xEx3D,xEx3D)).astype(np.float32)
        y=np.concatenate((self.y,y)).astype(np.float32)
        yEx=np.concatenate((self.yEx,yEx)).astype(np.float32)
        y3D=np.concatenate((self.y3D,y3D)).astype(np.float32)
        yEx3D=np.concatenate((self.yEx3D,yEx3D)).astype(np.float32)

        x,y=shuffle(x,y)
        xEx,yEx=shuffle(xEx,yEx)
        x3D,y3D=shuffle(x3D,y3D)
        xEx3D,yEx3D=shuffle(xEx3D,yEx3D)


        self.x,self.y=x,y
        self.xEx,self.yEx=xEx,yEx
        self.x3D,self.y3D=x3D,y3D
        self.xEx3D,self.yEx3D=xEx3D,yEx3D


    def create3Dmodel(self):
        args=self.args
            
        with self.strategy.scope():
            if args.FourD.reuse3D:
                self.model3D=tf.keras.models.load_model(f'{args.mlmodelout}/3D_model',compile=False)  
                self.epoch3D=self.args.meta['3Dmodel']['Epoch']
                self.loss3D=self.args.meta['3Dmodel']['loss']
                if self.epoch3D + 2 > args.FourD.maxEpoch3D:
                    return
            else:
                self.model3D = tf.keras.Sequential([
                    tf.keras.layers.Flatten(),
                    tf.keras.layers.Dense(512, activation=gelu),
                    tf.keras.layers.Dense(256, activation=gelu),
                    tf.keras.layers.Dense(128, activation=gelu),
                    tf.keras.layers.Dense(64, activation=gelu),
                    tf.keras.layers.Dense(1,activation='linear')
                ])
        
        self.train3D()

    def train3D(self):
        args=self.args
        ntrain=self.x3D.shape[0]
        m_shift=self.m_shift
        m_scale=self.m_scale
        ep_shift=self.ep_shift
        ep_scale=self.ep_scale
        
        with self.strategy.scope():
            self.optimizer3D = tf.keras.optimizers.Adam(learning_rate=self.lr_schedule)

        training_set3D = tf.data.Dataset.from_tensor_slices((self.x3D, self.y3D)).shuffle(256).batch(args.FourD.batchSize3D)
        dist_training_set3D=self.strategy.experimental_distribute_dataset(training_set3D)
        test_set3D = tf.data.Dataset.from_tensor_slices((self.xEx3D, self.yEx3D)).shuffle(256).batch(args.FourD.batchSize3D)
        

        @tf.function
        def loss_3D(model,xx,yy):
            return tf.sqrt(tf.reduce_mean(tf.math.square(model(xx)-yy)))
            
        # @tf.function
        def validate_3D(model,dataset):
            se=0.0
            count=0
            for data in dataset:
                se+=tf.square(loss_3D(model,*data))*data[0].shape[0]
                count+=data[0].shape[0]
            return tf.sqrt(se/count)
        
        # global bestloss, bestlosses

        @tf.function
        def training_step3D(data):
            xx,yy=data
            with tf.GradientTape() as tape:
                tape.watch(xx)
                loss=loss_3D(self.model3D,xx,yy)
            grad = tape.gradient(loss, self.model3D.trainable_variables)
            self.optimizer3D.apply_gradients(zip(grad, self.model3D.trainable_variables))
            return loss
        @tf.function
        def dist_training_step3D(dist_inputs):
            per_replica_losses = self.strategy.run(training_step3D, args=(dist_inputs,))
            return self.strategy.reduce(tf.distribute.ReduceOp.MEAN, per_replica_losses,axis=None)

        def train(training_set):
            print('----------------------------------------------------')
            epoch_start= time.time()
            for step, data in enumerate(training_set):
                # step_start = time.time()
                loss_train=dist_training_step3D(data)

            # train_loss=validate_3D(self.model3D,training_set3D)*ep_scale
            ex_loss=validate_3D(self.model3D,test_set3D)*ep_scale
            # print(self.optimizer3D._decayed_lr(tf.float32).numpy())
            # ex_loss1=validate_3D(model3D,test_set3D1)*ep_scale
            if ex_loss < self.loss3D:
                self.model3D.save(f'{args.mlmodelout}/3D_model')
                self.loss3D=ex_loss
                args.meta['3Dmodel']['Epoch']=self.epoch3D
                args.meta['3Dmodel']['loss']=self.loss3D.numpy().astype(float)
                args.writeMeta()

            
            now=time.time()
            t_epoch=now-epoch_start
            print('\repoch %-6d %5d/%-5d         t_epoch: %10.1f       ' % (self.epoch3D,step,ntrain//args.FourD.batchSize3D,t_epoch))
            # print('train:     %-10.6f'% train_loss)
            print('validate:  %-10.6f'% ex_loss)
            # print('validate:  %-10.6f'% ex_loss1)            
            print('best:      %-10.6f'% self.loss3D)
            sys.stdout.flush()
            self.epoch3D+=1
        
        print(' training 3D model')        
        print("     Ntrain: ",self.y3D.shape[0])

        while True:
            train(dist_training_set3D)
            if self.epoch3D >= args.FourD.maxEpoch3D: 
                break

        print(' 3D model trained')

    def create4Dmodel(self):
        args=self.args
        
        self.xlist=self.args.meta['descriptor']['xList']
        self.ylist=self.args.meta['descriptor']['yList']

        self.prepareData()
        
        l=args.meta['descriptor']['length']//2

        if args.FourD.use3D:
            self.create3Dmodel()
        with self.strategy.scope():
            if args.FourD.reuse4D:
                self.model=tf.keras.models.load_model(f'{args.mlmodelout}/4D_model',compile=False)
                self.epoch4D=self.args.meta['4Dmodel']['Epoch']
                self.losses4D=tuple(self.args.meta['4Dmodel']['losses'])
                self.loss4D=self.losses4D[-1]
                if self.epoch4D + 2 > args.FourD.maxEpoch4D:
                    return
            else:
                self.model = tf.keras.Sequential([
                    tf.keras.layers.Flatten(),
                    tf.keras.layers.Dense(1024, activation=gelu),
                    tf.keras.layers.Dense(512, activation=gelu),
                    tf.keras.layers.Dense(256, activation=gelu),
                    tf.keras.layers.Dense(128, activation=gelu),
                    tf.keras.layers.Dense(64, activation=gelu),
                    tf.keras.layers.Dense(l,activation='linear')
                ])
        
        self.train4D()

    def train4D(self):
        args=self.args
        l=args.meta['descriptor']['length']//2
        if args.FourD.Descriptor.lower()=='ic':
            icidx=tf.constant(args.meta["descriptor"]["ICdict"]['idx'],dtype=tf.int32)
        m=tf.constant(args.meta['masses'],dtype=tf.float32)
        ntrain=self.x.shape[0]
        m_shift=self.m_shift
        m_scale=self.m_scale
        ep_shift=self.ep_shift
        ep_scale=self.ep_scale
        x_shift=self.x_shift
        x_scale=self.x_scale
        y_shift=self.y_shift

        with self.strategy.scope():
            self.optimizer = tf.keras.optimizers.Adam(learning_rate=self.lr_schedule)
        
        training_set = tf.data.Dataset.from_tensor_slices((self.x, self.y)).shuffle(256).batch(args.FourD.batchSize4D)
        test_set = tf.data.Dataset.from_tensor_slices((self.xEx, self.yEx)).shuffle(256).batch(args.FourD.batchSize4D)
        dist_training_set=self.strategy.experimental_distribute_dataset(training_set)

        @tf.function
        def loss_fn_ic(model,x,y,model3D=None):   
            ekloss=0
            eploss=0
            w=1

            with tf.GradientTape()as tape:
                tape.watch(x)
                yest=model(x)+y_shift[:l]
            vp=tape.batch_jacobian(yest,x)[:,:l,-1]/x_scale[-1]
            yy=y+y_shift
            mp=yest[:,:l]
            vt=yy[:,l:2*l]
            mt=yy[:,:l]

            if args.FourD.checkV0:
                x0=tf.concat((x[:,:-1],x[:,-1:]*0),axis=1)
                v0p=(model(x0)+y_shift[:l])*10
                v0t=x0[:,l:2*l]
                v0loss=tf.sqrt(tf.reduce_mean(tf.square(v0t-v0p)*w))
                ekloss+=v0loss

            if args.FourD.normalizeT:
                xx=x*x_scale+x_shift
                t=xx[:,-1][:,tf.newaxis]
                a=self.normalizeTfactor
                ft=(1-tf.exp(-(t/a)**2))
                dftdt=2*t/a**2*tf.exp(-(t/a)**2)
                mpic=mp*ft+xx[:,:l]+xx[:,l:2*l]*t*(1-ft)
                mtic=mt*ft+xx[:,:l]+xx[:,l:2*l]*t*(1-ft)
                if args.FourD.checkEk:
                    vpic=vp*ft+dftdt*mp+xx[:,l:2*l]*(1-dftdt*t-ft)
                    vpic=vt*ft+dftdt*mp+xx[:,l:2*l]*(1-dftdt*t-ft)
                # ft=1-tf.exp(-10*t)
                # dftdt=10*tf.exp(-10*t)
                # # mpic=mp*(1-tf.exp(-tf.square(t)))+xx[:,:l]+xx[:,l:2*l]*t
                # # mtic=mt*(1-tf.exp(-tf.square(t)))+xx[:,:l]+xx[:,l:2*l]*t
                # mpic=mp*ft+xx[:,:l]
                # mtic=mt*ft+xx[:,:l]
                # if args.FourD.checkEk:
                #     vpic=vp*ft+dftdt*mp
                #     vtic=vt*ft+dftdt*mt
                w=tf.exp(-t)+tf.exp(t-args.tc)+1
            else:
                mpic=mp
                mtic=mt
                vpic=vp
                vtic=vp

            if args.FourD.checkEk:
                mpxyz,vpxyz=unDescribeTF(tf.concat((mpic,vpic),1),icidx)
                mtxyz,vtxyz=unDescribeTF(tf.concat((mtic,vtic),1),icidx)
                Ekp=getEksTF(vpxyz,m)
                Ekt=yy[:,-2] if 'ek' in args.FourD.ylist else getEksTF(vtxyz,m)
                ekloss+=tf.sqrt(tf.reduce_mean(tf.square(Ekp-Ekt)*w))

            # deltaE=tf.exp(-10*tf.abs(xx[:,-2][:,tf.newaxis]))
            # w=xx[:,-1][:,tf.newaxis]/10*(tf.sqrt(deltaE)-deltaE)+deltaE

            if model3D:
                epest=model3D(((tf.math.floormod(mpic+semidivisor,2*semidivisor)-semidivisor)-m_shift)/m_scale)
                epref=model3D(((tf.math.floormod(mtic+semidivisor,2*semidivisor)-semidivisor)-m_shift)/m_scale)
                eperr=(epest-epref)*ep_scale
                eploss=tf.sqrt(tf.reduce_mean(tf.square(eperr)*w))


            mloss=tf.sqrt(tf.reduce_mean(tf.square(mt-mp)*w,axis=0))
            vloss=tf.sqrt(tf.reduce_mean(tf.square(vt-vp)*w,axis=0))
            Dloss=tf.reduce_mean(mloss[:ld])
            Aloss=tf.reduce_mean(mloss[ld:ld+la])
            DAloss=tf.reduce_mean(mloss[ld+la:])
            vDloss=tf.reduce_mean(vloss[:ld])
            vAloss=tf.reduce_mean(vloss[ld:ld+la])
            vDAloss=tf.reduce_mean(vloss[ld+la:])

            loss=1.0*Dloss+2.0*Aloss+4.0*DAloss+16.0*vDloss+20.0*vAloss+24.0*vDAloss+1.0*eploss+16*ekloss
            return Dloss,Aloss,DAloss,eploss,vDloss,vAloss,vDAloss,ekloss,loss

        @tf.function
        def loss_fn_xyz(model,x,y,model3D=None):
            with tf.GradientTape()as tape:
                tape.watch(x)
                yest=model(x)+y_shift[:l]
            vp=tape.batch_jacobian(yest,x)[:,:,-1]/x_scale[-1]
            yy=y+y_shift
            mp=yest[:,:l]
            vt=yy[:,l:2*l]
            mt=yy[:,:l]
            mloss=tf.sqrt(tf.reduce_mean(tf.square(mt-mp)))
            vloss=tf.sqrt(tf.reduce_mean(tf.square(vt-vp)))

            ekloss=0
            eploss=0

            if args.FourD.normalizeT:
                xx=x*x_scale+x_shift
                t=xx[:,-1][:,tf.newaxis]
                ft=1-tf.exp(-10*t)
                dftdt=10*tf.exp(-10*t)
                mpxyz=mp*ft+xx[:,:l]
                if args.FourD.checkEk:
                    vpxyz=vp*ft+dftdt*mp
            else:
                mpxyz=mp
                vpxyz=vp

            mpxyz=tf.reshape(mpxyz,[mpxyz.shape[0],-1,3])
            vpxyz=tf.reshape(vpxyz,[vpxyz.shape[0],-1,3])

            if model3D:
                x3D=((IDescrTF(mpxyz)-m_shift)/m_scale)
                eploss=tf.sqrt(tf.reduce_mean(tf.square(model3D(x3D)*ep_scale+ep_shift-yy[:,-1:])))
            if args.FourD.checkEk:
                vtxyz=tf.reshape(vt,[vt.shape[0],-1,3])
                Ekp=getEksTF(vpxyz,m)
                Ekt=yy[:,-2] if 'ek' in args.FourD.ylist else getEksTF(vtxyz,m)
                ekloss=tf.sqrt(tf.reduce_mean(tf.square(Ekp-Ekt)))
            

            loss=1.0*mloss+8.0*vloss+1.0*eploss+1.0*ekloss
            return mloss,vloss,eploss,ekloss,loss

        if args.FourD.Descriptor.lower()=='ic':
            la=l//3
            ld=la
            lda=la
            semidivisor=tf.constant([100]*ld+[np.pi]*(la+lda))
            loss_fn=loss_fn_ic
        elif args.FourD.Descriptor.lower()=='xyz':
            loss_fn=loss_fn_xyz

        def validate(model,dataset):
            se=np.zeros(9 if args.FourD.Descriptor.lower()=='ic' else 5)
            count=0
            for data in dataset:
                n=data[0].shape[0]
                se+=np.square(loss_fn(model,*data,model3D=self.model3D if args.FourD.use3D else None))*n
                count+=n
            return tuple(np.sqrt(se/count))

        @tf.function
        def training_step(data):
            xx,yy=data
            with tf.GradientTape() as tape:
                tape.watch(xx)
                losses=loss_fn(self.model,xx,yy,model3D=self.model3D if args.FourD.use3D else None)
                loss=losses[-1]
            grad = tape.gradient(loss, self.model.trainable_variables)
            self.optimizer.apply_gradients(zip(grad, self.model.trainable_variables))
            return losses

        @tf.function
        def dist_training_step(dist_inputs):
            per_replica_losses = self.strategy.run(training_step, args=(dist_inputs,))
            return self.strategy.reduce(tf.distribute.ReduceOp.MEAN, per_replica_losses,axis=None)

        def train(training_data):
            print('----------------------------------------------------')
            epoch_start= time.time()
            for step, data in enumerate(training_data):
                losses=dist_training_step(data)

            train_losses=validate(self.model,training_set)
            ex_losses=validate(self.model,test_set)
            if ex_losses[-1] < self.loss4D:
                self.model.save(f'{args.mlmodelout}/4D_model')
                self.loss4D=ex_losses[-1]
                self.losses4D=ex_losses
                args.meta['4Dmodel']['Epoch']=self.epoch4D
                args.meta['4Dmodel']['losses']=[loss.astype(float) for loss in self.losses4D]
                args.writeMeta()

            # print(self.optimizer._decayed_lr(tf.float32))
            # print(self.losses4D)
            now=time.time()
            t_epoch=now-epoch_start
            print('\repoch %-6d %5d/%-5d         t_epoch: %10.1f       ' % (self.epoch4D,step,ntrain//args.FourD.batchSize4D,t_epoch))
            if args.FourD.Descriptor.lower()=='ic':
                print('%-10s %-10s %-10s %-10s %-10s'% (self.msg,"D","A","DA","Ep/Ek"))
                print('train:     %-10.6f %-10.6f %-10.6f %-10.6f\n  d/dt     %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% train_losses)
                print('validate:  %-10.6f %-10.6f %-10.6f %-10.6f\n  d/dt     %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% ex_losses)            
                print('best:      %-10.6f %-10.6f %-10.6f %-10.6f\n  d/dt     %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% self.losses4D)
            elif args.FourD.Descriptor.lower()=='xyz':
                print('           %-10s %-10s %-10s %-10s'% ("M","v","Ep","Ek"))
                # print('train:     %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% train_losses)   
                print('validate:  %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% ex_losses)            
                print('best:      %-10.6f %-10.6f %-10.6f %-10.6f\n                                 Loss       %-10.6f'% self.losses4D)
            sys.stdout.flush()
            self.epoch4D+=1
            
        
        print('training 4D model')
        print("     Ntrain: ",self.y.shape[0])
        while True:
            train(dist_training_set)
            if self.epoch4D >= args.FourD.maxEpoch4D: 
                break
        print('4D model trained')

    def use4Dmodel(self):
        args=self.args
        
        icdict=args.meta["descriptor"]["ICdict"]
        m=np.array(args.meta['masses'])
        if self.model3D:
            m_shift=args.meta['3Dmodel']['m_shift']
            m_scale=args.meta['3Dmodel']['m_scale']
            ep_shift=args.meta['3Dmodel']['ep_shift']
            ep_scale=args.meta['3Dmodel']['ep_scale']

        x_shift=np.array(args.meta['4Dmodel']['x_shift']).astype(np.float32)
        x_scale=np.array(args.meta['4Dmodel']['x_scale']).astype(np.float32)
        y_shift=np.array(args.meta['4Dmodel']['y_shift']).astype(np.float32)

        l=args.meta['descriptor']['length']//2
        la=l//3
        ld=la
        lda=la
        # path=args.FourD.MD.dirOut
        # os.system(f'mkdir {path}')

        tm=args.trun

        
        MaxSegm=args.tSegm
        dt=args.dt

        xyzs,sps =loadXYZ(args.initXYZ,list)
        vs, _ = loadXYZ(args.initVXYZ,list,getsp=False)

        i=0
        xyzoffset=getCoM(xyzs[i],m)
        voffset=getCoM(vs[i],m)
        x0=Describe(xyzs[i][np.newaxis],vs[i][np.newaxis],icdict,m=m).astype(np.float32)
        ts=np.arange(0,tm,dt)+dt
        ts[-1]=tm
        t0=0
        
        # x=np.concatenate((descr[[i]],np.array([[0]])),axis=1).astype(np.float32)
        # yfile=f'{path}/traj{i}.y'
        xyzfile=args.trajXYZout
        vxyzfile=args.trajVXYZout
        tfile=args.trajTime
        ft=open(args.trajTime,'w')
        fek=open(args.trajEkin,'w')
        fy=open(args.trajDescr,'w')
        fep=open(args.trajEpot,'w')
        fet=open(args.trajEtot,'w')

        ek=getEk(vs[i],m)[np.newaxis]
        if self.model3D:
            ep=self.model3D((x0[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
        else:
            ep=np.zeros_like(ek)
        etot=(ep+ek)[0]
        P0=getLinM(vs[i],m)
        L0=getAngM(xyzs[i],vs[i],m)
        Eerror=0
        np.savetxt(fek,ek)
        np.savetxt(fep,ep)
        np.savetxt(fet,(ep+ek))
        np.savetxt(fy,x0)
        saveXYZ(xyzfile,xyzs[i],sps[i],'w',msg=f't=0.0fs')
        saveXYZ(vxyzfile,vs[i],sps[i],'w',msg=f't=0.0fs')
        
        with open(tfile,'w') as f:
            f.write('0.0\n')

        def getY(x, model):
            y=differentiation(model,x,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l).numpy()
            # print(x[[-1]])
            # print(differentiation(model,x[[-1]],x_shift=x_shift,x_scale=x_scale,y_shift=y_shift,l=l).numpy())
            # print(y[-1])
            if np.sum(np.isnan(y)) > 0:
                stopper.stopMLatom('prediction failed')
                
            if args.FourD.normalizeT:
                x,y=unnormalizeT(x,y,l=l,a=self.normalizeTfactor)
            elif args.FourD.m2vbar:
                x,y=Vbar2M(x,y)
            elif args.FourD.m2dm:
                x,y=dM2M(x,y)
            elif args.FourD.logisticatet:
                x,y=unlogisticateT(x,y)
            theOppositeWayToCorrectAngle(y,idx=list(range(ld,l)))
            return y
        
        def getAll(x, model):
            y=getY(x, model)
            xyz,v=unDescribe(y,icdict['idx'])
            xyz=xyz+xyzoffset[np.newaxis,:]+voffset[np.newaxis,:]*(t[:,np.newaxis,np.newaxis]+t0)
            v=v-getCoM(v,m)[:,np.newaxis,:]+voffset[np.newaxis,:]
            # x0=y[[-1]]
            for i in range(len(v)):
                v[i]=adjV(xyz[i],v[i],m,P0,L0)
                # x0=Describe(xyz[[-1]],v[[-1]],icdict,m=m).astype(np.float32)
            ek=getEks(v,m)
            ep=np.zeros_like(ek)
            if self.model3D:
                ep=self.model3D((y[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
            
            if args.FourD.forceEtot:
                v=v*np.sqrt((etot-ep)/ek)[:,np.newaxis,np.newaxis]
                ek=getEks(v,m)
                # x0=Describe(xyz[[-1]],v[[-1]],icdict,m=m).astype(np.float32)

            Eerror=(ep+ek)-etot
            
            return y, xyz, v, ek ,ep, Eerror#, x0

        def monarchWings(x0):
            t=np.append((np.arange(90)+10)/10,10.)
            # t=np.append((np.arange(100))/10,10.)
            # t=(np.arange(61)+20)/10.
            x=np.concatenate((np.repeat(x0,len(t),axis=0),t[:,np.newaxis]),axis=1)
            y=getY(x, self.model)
            x[:-1]=np.concatenate((y[:-1],(t[-1]-t[:-1])[:,np.newaxis]),axis=1)
            # print(x[:,[0,-1]])
            y[:-1]=getY(x[:-1], self.model)

            xyz,v=unDescribe(y,icdict['idx'])
            # xyz=xyz+xyzoffset[np.newaxis,:]+voffset[np.newaxis,:]*(t[:,np.newaxis,np.newaxis]+t0)
            v=v-getCoM(v,m)[:,np.newaxis,:]+voffset[np.newaxis,:]
            ek=getEks(v,m)
            ep=self.model3D((y[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
            et=ek+ep
            eterr=np.abs(et-etot)
            # print(np.min(eterr)*627.5,eterr[np.argmin(eterr)],ek[np.argmin(eterr)],ep[np.argmin(eterr)],etot,t[np.argmin(eterr)])
            print(np.min(eterr)*627.5,t[np.argmin(eterr)])
            return x[np.argmin(eterr),:-1], t[np.argmin(eterr)]

        def findRoot(x0,t0,tt,y0=None,threshold=0.001/627.5,i=0):
            print('finding root between %.4f and %.4f'% (t0,tt))
            i+=1
            tm=(t0+tt)/2
            ts=[[tm]] if y0 else [[t0],[tm]] 
            # ts=[[t0],[tm],[tt]]
            x=np.concatenate((np.repeat(x0,len(ts),axis=0),ts),axis=1)
            y=getY(x, self.model)
            _,v=unDescribe(y,icdict['idx'])
            v=v-getCoM(v,m)[:,np.newaxis,:]+voffset[np.newaxis,:]
            ek=getEks(v,m)
            ep=self.model3D((y[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
            et=ek+ep
            eterr=et-etot
            if np.abs(eterr[-1])<threshold or i>8:
                return tm 
            y0=y0 if y0 else eterr[0]
            # print(y0*eterr[-1]<0,y0*eterr[-2]<0)
            if y0*eterr[-1]<0:
                return findRoot(x0,t0,tm,y0,i=i)
            else:
                return findRoot(x0,tm,tt,eterr[-1],i=i)

        def findNextT0(x0):
            t=np.append((np.arange(90)+10)/10,10.)
            # t=np.append((np.arange(100))/10,10.)
            x=np.concatenate((np.repeat(x0,len(t),axis=0),t[:,np.newaxis]),axis=1)
            y=getY(x, self.model)

            xyz,v=unDescribe(y,icdict['idx'])
            xyz=xyz+xyzoffset[np.newaxis,:]+voffset[np.newaxis,:]*(t[:,np.newaxis,np.newaxis]+t0)
            v=v-getCoM(v,m)[:,np.newaxis,:]+voffset[np.newaxis,:]
            ek=getEks(v,m)
            ep=self.model3D((y[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
            et=ek+ep
            eterr=et-etot
            # print(eterr)
            for i in range(len(eterr)-1,0,-1):
                if eterr[i]*eterr[i-1]<0:
                    print(eterr[i-1],eterr[i])
                    return findRoot(x0,t[i-1],t[i],eterr[i-1])
            # print(np.min(eterr)*627.5,eterr[np.argmin(eterr)],ek[np.argmin(eterr)],ep[np.argmin(eterr)],etot,t[np.argmin(eterr)])
            print(' root not found, using point with least Etot error for the next step...')
            # print(np.min(eterr)*627.5,t[np.argmin(eterr)])
            return t[np.argmin(np.abs(eterr))]

        def saveResult(result,tstamps):
            y, xyz, v, ek ,ep, _ =result
            np.savetxt(fep,ep)
            np.savetxt(fet,(ep+ek))
            saveXYZs(xyzfile,xyz,sps[i],'a',msgs=tstamps)
            saveXYZs(vxyzfile,v,sps[i],'a',msgs=tstamps)

            np.savetxt(fek,ek)
            np.savetxt(fy,y)
            for tstamp in tstamps:
                ft.write(tstamp+'\n')
            return

        Segms=[]
        pdict={0:0}
        tbreak=0
        threshold=1
        while t0 < tm:
            if args.FourD.adaptSeg:
                tSegm=findNextT0(x0)
            else:
                tSegm=args.tSegm

            if t0 not in pdict.keys(): pdict[t0]=0
            if t0 > tbreak: threshold=10
            # t=np.append(ts[(ts>t0+0.000001)&(ts<t0+tSegm+0.000001)]-t0,tSegm)
            t=ts[(ts>t0+0.000001)&(ts<t0+tSegm+0.000001)]-t0
            x=np.concatenate((np.repeat(x0,len(t),axis=0),t[:,np.newaxis]),axis=1)
            xSegm=np.concatenate((x0,[[tSegm]]),axis=1)
            # x=np.concatenate((np.repeat(x0,len(t),axis=0),deltaE*np.ones_like(t[:,np.newaxis]),t[:,np.newaxis]),axis=1)
            
            if args.FourD.monarchWings:
                xx, tt= monarchWings(x0)
                x[x[:,-1]>tt+0.001,:-1]=xx
                x[x[:,-1]>tt+0.001,-1]-=tt
            # print(xx[0],tt)
            # print(x[:,[0,-1]])

            if self.args.MLmodelsIn:
                results=[]
                for model in self.models:
                    results.append(getAll(xSegm, model))
                Eerrors=np.abs([result[-1][-1] for result in results])
                sort=np.argsort(Eerrors)
                print(sort[pdict[t0]])
                self.model=self.models[sort[pdict[t0]]]
                x0, *_, Eerror=results[sort[pdict[t0]]]
                if np.abs(Eerror[-1])*627.5>threshold or pdict[t0]>=len(sort)-1:
                    print(t0,pdict[t0],len(Segms))
                    tbreak=max(t0,tbreak)
                    if len(Segms)>1:
                        Segms.pop(-1)
                        t0-=tSegm
                        x0=Segms[-1][-1]
                        pdict[t0]+=1
                    else:
                        threshold*=2
                        pdict[t0]=0
                    for k in pdict.keys():
                        if k>t0:
                            pdict[k]=0
                    continue

            else:
                x0, *_, Eerror =getAll(xSegm, self.model)
            Segms.append([getAll(x, self.model),['%.3f fs %s' % (i, 'model'+str(sort[pdict[t0]]) if self.args.MLmodelsIn else '') for i in t+t0],x0])
            if len(Segms)>10:
                saveResult(*Segms[0][:-1])
                Segms.pop(0)
            
            print(' %.2f-%.2f fs'% (t0,t0+tSegm))
            print(f'Etot error: {(Eerror[-1])*627.5} kcal/mol')
            
            sys.stdout.flush()
            t0+=tSegm
        
        for Segm in Segms:
            saveResult(*Segm[:-1])

        ft.close()
        fek.close()
        fy.close()
        fep.close()
        fet.close()
        # xyz_ref,_=loadXYZ('../testing/traj.xyz')
        # v_ref,_=loadXYZ('../testing/traj.vxyz',getsp=False)
        # y_ref=Describe(xyz_ref,v_ref,icdict,m=m)
        # ep_ref=self.model3D((y_ref[:,:l]-m_shift)/m_scale).numpy().flatten()*ep_scale+ep_shift
        # np.savetxt('../testing/traj.ep3D',ep_ref)
        # return xyz[-1],v[-1],y[-1],sps[i],ek[[0,-1]],ep[[0,-1]] if self.model3D else None
            

        # h5file=File(args.trajH5MDout,'w')
        # part=h5file.particles_group('all')
        # part.create_box(dimension=3, boundary=['none','none','none'])
        # part_pos=element(part,'position',store='time',shape=xyzs[i].shape,dtype=np.float32, time=True)
        # part_descr=element(part,'descriptor',store='time',shape=descr.shape,dtype=np.float32, time=True)
        # part_pos.append(xyzs[i],0,0.0)
        # part_descr.append(descr,0,0.0)
        # h5file.observables = h5file.require_group('observables')
        # element(part, 'names', data=np.array([bytes('%-2s'%name,'utf-8')for name in sps[i]]), store='fixed')
        # h5file.close()
    def estAcc4Dmodel(self):
        pass
        
    def activeLearning(self):
        args=self.args
        os.system(f'mkdir {args.MLmodelOut}')
        if not os.path.isdir(f'{args.MLmodelOut}/4DMD'): os.system(f'mkdir {args.MLmodelOut}/4DMD')
        os.system(f'cp {args.initxyz} {args.MLmodelOut}/4DMD/init.xyz')
        os.system(f'cp {args.initvxyz} {args.MLmodelOut}/4DMD/init.vxyz')

        Nmodel=len(args.ICidx)
        gpus=[x.name.split(':',1)[1] for x in  tf.config.get_visible_devices(device_type='GPU')]

        models=[]
        for i in range(Nmodel):
            newargs=addReplaceArg('activeLearning','create4Dmodel',args.args2pass)
            newargs=addReplaceArg('ICidx',f'ICidx={args.ICidx[i]}',newargs)
            newargs=addReplaceArg('MLmodelOut',f'MLmodelOut={args.MLmodelOut}/ALmodel{i}',newargs)
            newargs=addReplaceArg('initXYZ',f'initXYZ={args.MLmodelOut}/4DMD/init.xyz',newargs)
            newargs=addReplaceArg('initVXYZ',f'initVXYZ={args.MLmodelOut}/4DMD/init.vxyz',newargs)
            newargs=addReplaceArg('trajXYZout',f'trajXYZout={args.MLmodelOut}/ALmodel{i}/traj.xyz',newargs)
            newargs=addReplaceArg('trajVXYZout',f'trajVXYZout={args.MLmodelOut}/ALmodel{i}/traj.vxyz',newargs)
            newargs=addReplaceArg('trajTime',f'trajTime={args.MLmodelOut}/ALmodel{i}/traj.t',newargs)
            newargs=addReplaceArg('trajEpot',f'trajEpot={args.MLmodelOut}/ALmodel{i}/traj.epot',newargs)
            newargs=addReplaceArg('trajEkin',f'trajEkin={args.MLmodelOut}/ALmodel{i}/traj.ekin',newargs)
            newargs=addReplaceArg('trajEtot',f'trajEtot={args.MLmodelOut}/ALmodel{i}/traj.etot',newargs)
            newargs=addReplaceArg('trajH5MDout',f'trajH5MDout={args.MLmodelOut}/ALmodel{i}/traj.h5',newargs)
            
            models.append(FourDcls(newargs,devices=[gpus[i]] if gpus else None, msg=f'AL_{i}'))
            # models.append(FourDcls(newargs))
        
        # global create4DAL

        # def create4DAL(model):
        #     model.create4Dmodel()

        # pool=Pool(Nmodel)
        # pool.map(create4DAL,[models[i] for i in range(Nmodel)])
        # pool.close()
        for i in range(Nmodel):
            if i>0 and args.ICidx[i]==args.ICidx[-1] and not args.FourD.reuse3D and not args.FourD.reuse4D:
                os.system(f'rm -rf {args.MLmodelOut}/ALmodel{i}; cp -r {args.MLmodelOut}/ALmodel{i-1} {args.MLmodelOut}/ALmodel{i}')
                newargs=addReplaceArg('FourD.reuseData','FourD.reuseData=1',newargs)
            print(f" training ALmodel{i}...")
            models[i].create4Dmodel()

        # processes=[]
        # for i in range(Nmodel):
        #     p = Process(target = models[i].create4Dmodel)
        #     p.start()
        #     processes.append(p)
            
        # for p in processes:
        #     p.join()

        self.Niter=0
        self.Nretrain=0
        while True:
            path=f'{args.MLmodelOut}/4DMD/{self.Niter}_{self.Nretrain}'
            os.system(f'mkdir {path}')
            xyzts=[]
            vts=[]
            yts=[]
            deltaE=[]
            for i in range(Nmodel):
                print(f" running 4DMD with ALmodel{i}...")
                xyzt,vt,yt,sp,ek,ep=models[i].use4Dmodel()
                os.system(f'mkdir {path}/{i}')
                os.system(f'cp {args.MLmodelOut}/ALmodel{i}/traj.* {path}/{i}')
                xyzts.append(xyzt)
                vts.append(vt)
                yts.append(yt)
                deltaE.append(np.abs((ek+ep)[1]-(ek+ep)[0]))
            # print(np.array(xyzts))
            sdxyz=np.std(np.array(xyzts),axis=0)
            sdv=np.std(np.array(vts),axis=0)
            sdy=np.std(np.array(yts),axis=0)
            print(f' SD of finial geometries:\n{sdxyz}')
            print(f' SD of finial velocities:\n{sdv}')
            print(f' SD of finial descriptors:\n{sdy.reshape(2,3,-1).transpose(0,2,1)}')
            print(f' energy shift {(ek+ep)[1]-(ek+ep)[0]}')
            # sd=np.mean(sdxyz)+np.mean(sdv)
            sd=np.mean(sdxyz)
            print(f' score of SD: {sd}')
            sys.stdout.flush()
            if sd >0.1 or np.isnan(sd) or np.max(deltaE)>0.01:
                if not self.Nretrain:
                    newtraj=self.run3DMD()
                for i in range(Nmodel):
                    models[i].appendData(newtraj)
                    print(f' retraining ALmodel{i}...')
                    models[i].train3D()
                    models[i].train4D()
                self.Nretrain+=1
                continue
            else:
                xyz0=np.mean(np.array(xyzts),axis=0)
                v0=np.mean(np.array(vts),axis=0)
                saveXYZ(f'{args.MLmodelOut}/4DMD/init.xyz',xyz0,sp)
                saveXYZ(f'{args.MLmodelOut}/4DMD/init.vxyz',v0,sp)
                self.Nretrain=0
                self.Niter+=1
    
    def run3DMD(self):
        import ThreeDMD
        args=self.args
        if not os.path.isdir(f'{args.MLmodelOut}/3DMD'): os.system(f'mkdir {args.MLmodelOut}/3DMD')
        path=f'{args.MLmodelOut}/3DMD/{self.Niter}'
        os.system(f'mkdir {path}')
        os.system(f'cp {args.MLmodelOut}/4DMD/init.xyz {path}/init.xyz')
        os.system(f'cp {args.MLmodelOut}/4DMD/init.vxyz {path}/init.vxyz')
        args3D=addReplaceArg('activeLearning','create4Dmodel',args.args2pass)
        args3D=addReplaceArg('device',f'device=cpu',args3D)
        args3D=addReplaceArg('initXYZ',f'initXYZ={path}/init.xyz',args3D)
        args3D=addReplaceArg('initVXYZ',f'initVXYZ={path}/init.vxyz',args3D)
        args3D=addReplaceArg('trajXYZout',f'trajXYZout={path}/traj.xyz',args3D)
        args3D=addReplaceArg('trajVXYZout',f'trajVXYZout={path}/traj.vxyz',args3D)
        args3D=addReplaceArg('trajTime',f'trajTime={path}/traj.t',args3D)
        args3D=addReplaceArg('trajEpot',f'trajEpot={path}/traj.epot',args3D)
        args3D=addReplaceArg('trajEkin',f'trajEkin={path}/traj.ekin',args3D)
        args3D=addReplaceArg('trajEtot',f'trajEtot={path}/traj.etot',args3D)
        args3D=addReplaceArg('trajH5MDout',f'trajH5MDout={path}/traj.h5',args3D)
        print(" models didn't agree with each other, runing 3DMD...")
        ThreeDMD.ThreeDcls.dynamics(args3D)
        return f'{path}/traj.h5'

    def reactionPath(self):
        args=self.args
        from scipy.optimize import dual_annealing
        
        icdict=args.meta["descriptor"]["ICdict"]
        # model=tf.keras.models.load_model(f'{args.mlmodelin}/4D_model',compile=False)
        # model3D=tf.keras.models.load_model(f'{args.mlmodelin}/3D_model',compile=False)

        m_shift,m_scale,ep_shift=np.load(f'{args.mlmodelin}/norm_factors_3D.npy',allow_pickle=True)
        x_shift,x_scale,y_shift=np.load(f'{args.mlmodelin}/norm_factors_4D.npy',allow_pickle=True)

        l=args.meta['descriptor']['length']//2
        la=int(l/3)
        ld=la
        lda=la
        
        path=args.FourD.reactionPath.dirOut
        os.system(f'mkdir {path}')
        step=0.5

        def findInit(xyz0,xyzt,t,v0=np.zeros(27),vt=np.zeros(27)):
            semidivisor=np.array([100]*ld+[np.pi]*(ld+lda))
            m0=DescribeWithoutV(xyz0[np.newaxis],icdict)
            descrt=DescribeWithoutV(xyzt[np.newaxis],icdict)
            xyzref=XYZsettleDown(xyzt,centre=[0,0,0])[np.newaxis]
            # ept=(model3D(((np.mod(descrt+semidivisor,2*semidivisor)-semidivisor)-m_shift)/m_scale)+ep_shift)[-1,0]
            ep0=(self.model3D(((np.mod(m0+semidivisor,2*semidivisor)-semidivisor)-m_shift)/m_scale)+ep_shift)[-1,0]
            global best
            best=np.inf,np.inf
            def getDifference(v0):
                x=np.concatenate((np.repeat(Describe(xyz0[np.newaxis],100*v0.reshape(1,9,3),icdict),int(t/step),axis=0),((np.arange(int(t/step))+1)*step)[:,np.newaxis]),axis=1)
                x=np.append(x,np.concatenate((Describe(xyz0[np.newaxis],100*v0.reshape(-1,3)[np.newaxis],icdict),np.array([[t]])),axis=1),axis=0)
                y=predict(self.model,x,tc=args.FourD.tc,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift)
                theOppositeWayToCorrectAngle(y,idx=list(range(ld,l)))
                xyzest,_=unDescribe(y,icdict['idx'])[[-1]]
                rmsd=np.sqrt(np.mean(((xyzest-xyzref)**2)))
                epest=self.model3D(((np.mod(y[:,:l]+semidivisor,2*semidivisor)-semidivisor)-m_shift)/m_scale)+ep_shift
                # eploss=np.abs(epest[-1,0]-ept)
                barrier=abs(np.max(epest)-ep0.numpy())
                # print('rmsd: %12.4f     eploss: %12.4f     barrier: %12.4f' % (rmsd,eploss,barrier))
                if sum(best)> rmsd+barrier:
                    best=rmsd,barrier
                print('current       rmsd: %12.4f    barrier: %12.4f\nbest          rmsd: %12.4f    barrier: %12.4f\n' % (rmsd,barrier,*best))
                return rmsd+barrier
            res=dual_annealing(getDifference,tuple([(-.2,.2)]*27),x0=v0.flatten()/100,maxiter=10000,maxfun=100000)
            return res

        reactants,sps =loadXYZ(args.initXYZ)
        products,sps =loadXYZ(args.finalXYZ)
        for i in range(len(reactants)):
            xyz0=reactants[i]
            xyzt=products[i]
            res=findInit(xyz0,xyzt,args.reactionTime)
            saveXYZ(f'{path}/mol{i}_v0.xyz', res.x.reshape(9,3)/0.529177210903*24.188843265e-3*100,sps[i])
            
            saveXYZ(args.initVout, res.x.reshape(9,3)/0.529177210903*24.188843265e-3*100,sps[i])

            x=np.concatenate((np.repeat(Describe(xyz0[np.newaxis],res.x.reshape(1,9,3)*100,icdict),int(args.reactionTime/step),axis=0),((np.arange(int(args.reactionTime/step))+1)*step)[:,np.newaxis]),axis=1)
            y=predict(self.model,x,tc=args.FourD.tc,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift)
            theOppositeWayToCorrectAngle(y,idx=list(range(ld,l)))
            xyzs,v=unDescribe(y,icdict['idx'])
            # slider=np.zeros(xyzs.shape)
            # slider[:,:,0]=np.repeat(((np.arange(200)+1)/10-10)[:,np.newaxis],9,axis=1)
            # xyzs-=slider
            saveXYZs(f'{path}/mol{i}_reactionPath.xyz',xyzs,sps[i])
            np.savetxt(f'{path}/mol{i}_reactionPath.y',y)
            ep=self.model3D((y[:,:l]-m_shift)/m_scale)+ep_shift
            np.savetxt(f'{path}/mol{i}_reactionPath.ep',ep)


def gelu(features, approximate=False, name=None):
    features = tf.convert_to_tensor(features, name="features")
    if approximate:
        coeff = tf.cast(0.044715, features.dtype)
        return 0.5 * features * (
            1.0 + tf.tanh(0.7978845608028654 *
                                (features + coeff * tf.math.pow(features, 3))))
    else:
        return 0.5 * features * (1.0 + tf.math.erf(
            features / tf.cast(1.4142135623730951, features.dtype)))  