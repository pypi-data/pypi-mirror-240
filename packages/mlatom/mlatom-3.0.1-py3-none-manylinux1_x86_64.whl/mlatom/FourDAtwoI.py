from utils import addReplaceArg
from .functions4D import *
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
            'device':None,
            'initXYZ':'',
            'initVXYZ':'',
            'trun':1000,
            'finalXYZ':'',
            'initVout':'',
            'reactionTime':10,
            'trajName':'traj',
            'Ntrajs':16,
            # 'trajXYZout':'traj.xyz',
            # 'trajVXYZout':'traj.vxyz',
            # 'trajTime':'traj.t',
            # 'trajH5MDout':'traj.h5',
            # 'trajEpot':'traj.epot',
            # 'trajEkin':'traj.ekin',
            # 'trajEtot':'traj.etot',
            # 'trajDescr':'traj.y',
            'tc':10,
            'tSegm':'tc',
            'dt':'tc',
            'Trajs':[]
        })
        self.parse_input_content([
            "FourD.ICdict=0",
            'FourD.tmax=0',
            'FourD.use3D=1',
            'FourD.use3Dgrad=0',
            'FourD.reuseData=0',
            'FourD.reuse3D=0',
            'FourD.reuse4D=0',
            'FourD.tc=0',
            'Nsubtrain=0.95',
            'Nvalidate=0.05',
            'NNvalidate=0',
            'NNsubtrain=0',
            'FourD.initFreq=tc',
            'FourD.batchSize3D=1024',
            'FourD.batchSize4D=1024',
            'FourD.maxEpoch3D=1024',
            'FourD.maxEpoch4D=1024',
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
            'FourD.vbias=0.0',
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
            # self.FourD.use3D=self.meta['3Dmodel']['use']
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
        # if self.FourD.Descriptor.lower()=='ic' and not self.FourD.ICdict: self.FourD.ICdict=readIC(self.ICidx[0]) 
        if self.FourD.Descriptor.lower()=='ic' : self.FourD.ICdict=readIC(self.ICidx[0]) 
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
            self.meta['3Dmodel']['grad']=self.FourD.use3Dgrad
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
        self.masses=None

        self.training_sets=[]
        self.test_sets=[]
        self.training_sets3D=[]
        self.test_sets3D=[]
        
        self.loss3D=np.inf
        self.loss4D=np.inf
        self.losses4D=None

        self.epoch3D=0
        self.epoch4D=0

        self.normalizeTfactor=10

        if self.args.device:
            self.device = torch.device(self.args.device)
        else:
            self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        
        self.msg=msg
        

        self.init_lr=0.001
        self.decay_steps=8192
        self.decay_rate=0.99

        if self.args.MLmodelIn:
            self.masse=self.args.meta['masses']
            self.z=np.array(self.args.meta['z'])
            if self.args.meta['3Dmodel']['use']==1:
                model3D=torch.load(f'{self.args.mlmodelin}/model3D.pt',map_location=self.device)
                self.model3D=lambda x: model3D(torch.tensor(x).float().to(self.device)).cpu().detach().numpy()
                self.epoch3D=self.args.meta['3Dmodel']['Epoch']
                self.loss3D=self.args.meta['3Dmodel']['loss']
            self.model=torch.load(f'{self.args.mlmodelin}/model4D.pt',map_location=self.device)
            self.epoch4D=self.args.meta['4Dmodel']['Epoch']
            self.losses4D=tuple(self.args.meta['4Dmodel']['losses'])
            self.loss4D=self.losses4D[-1]

        if self.args.MLmodelsIn:
            self.model3Ds=[]
            self.models=[]
            for model in self.args.MLmodelsIn.split(','):
                self.models.append(torch.load(f'{model}/model4D.pt'))
                if self.args.meta['3Dmodel']['use']==1: self.model3Ds.append(torch.load(f'{model}/model3D.pt'))
            if self.args.meta['3Dmodel']['use']==1: self.model3D=lambda x: torch.mean(torch.tensor([m3D(torch.tensor(x).float().to(self.device)).cpu().detach().numpy() for m3D in self.model3Ds]),dim=0)

    
    def prepareData(self,trajs,tc=0):
        args=self.args
        if tc==0: tc=args.FourD.tc
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
            x,y=getData(dataset,self.xlist,self.ylist,tc,0,tmax*args.Nsubtrain,0,step=1)
            # xEx,yEx=getData(dataset,xlist,ylist,tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
            xEx,yEx=getData(dataset,self.xlist,self.ylist,tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
            if 'deltaE' in args.FourD.xlist+args.FourD.ylist:
                ek0=getEks(dataset['v'],dataset['m'][0])
                dataset['v']+=np.random.normal(0,0.01,dataset['v'].shape)
                ek1=getEks(dataset['v'],dataset['m'][0])
                dataset['deltaE']=ek1-ek0
                xx,yy=getData(dataset,self.xlist,self.ylist,tc,0,tmax*args.Nsubtrain,0,step=1)
                xxEx,yyEx=getData(dataset,self.xlist,self.ylist,tc,0,tmax*(args.Nsubtrain+args.Nvalidate),tmax*args.Nsubtrain,step=1)
                x=np.concatenate((x,xx),axis=0)
                y=np.concatenate((y,yy),axis=0)
                xEx=np.concatenate((xEx,xxEx),axis=0)
                yEx=np.concatenate((yEx,yyEx),axis=0)
            if not args.FourD.Descriptor3D:
                x3D=dataset['Descriptor'][:,:dataset['Descriptor'].shape[1]//2]
            elif args.FourD.Descriptor3D.lower()=='id':
                x3D=IDescr(dataset['xyz'])
            y3D=dataset['ep']
            if args.FourD.use3Dgrad:
                y3Dgrad=getGradIC(dataset['grad'],x3D,args.FourD.ICdict).cpu().detach().numpy()
                y3D=np.concatenate((y3D,y3Dgrad),axis=1)

            # print('described')
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
            if trajs[0][-4:]=='.npz':
                trajdata=dict(np.load(trajs[0]))
                self.masses=trajdata['m'][0]
                self.z=trajdata['z'][0]
            elif trajs[0][-3:]=='.h5':
                with File(trajs[0],'r') as f:
                    self.masses=f['particles/all/mass'][()]
                    self.z=f['particles/all/species'][()]
            args.meta['masses']=list(self.masses.astype(float))
            args.meta['z']=[int(z) for z in self.z]
            args.meta['descriptor']['length']=len(args.meta['masses'])*6
            args.writeMeta()

            manager = Manager()
            xs=manager.dict()
            ys=manager.dict()
            xExs=manager.dict()
            yExs=manager.dict()
            x3Ds=manager.dict()
            y3Ds=manager.dict()
            if args.FourD.use3Dgrad: y3Dgrads=manager.dict()

            print(' preparing data...')
            pool = Pool(args.nthreads)
            pool.map(getDataFromTraj,trajs)
            pool.close()
            x=np.concatenate([xs[traj] for traj in trajs], axis=0).astype(np.float32)
            y=np.concatenate([ys[traj] for traj in trajs], axis=0).astype(np.float32)
            xEx=np.concatenate([xExs[traj] for traj in trajs], axis=0).astype(np.float32)
            yEx=np.concatenate([yExs[traj] for traj in trajs], axis=0).astype(np.float32)
            x3D=np.concatenate([x3Ds[traj] for traj in trajs], axis=0).astype(np.float32)
            y3D=np.concatenate([y3Ds[traj] for traj in trajs], axis=0).astype(np.float32)
            np.save(f'{args.mlmodelout}/x.npy',x)
            np.save(f'{args.mlmodelout}/y.npy',y)
            np.save(f'{args.mlmodelout}/xEx.npy',xEx)
            np.save(f'{args.mlmodelout}/yEx.npy',yEx)
            np.save(f'{args.mlmodelout}/x3D.npy',x3D)
            np.save(f'{args.mlmodelout}/y3D.npy',y3D)


        x,y=shuffle(x,y)
        xEx,yEx=shuffle(xEx,yEx)
        x3D,y3D=shuffle(x3D,y3D)

        x3D=x3D[:y.shape[0]]
        y3D=y3D[:y.shape[0]]
        xEx3D=x3D[y.shape[0]:]
        yEx3D=y3D[y.shape[0]:]

        if args.NNvalidate:
            xEx,yEx=xEx[:args.NNvalidate],yEx[:args.NNvalidate]
            xEx3D,yEx3D=x3D[-args.NNvalidate:],y3D[-args.NNvalidate:]
        if args.NNsubtrain:
            x,y=x[:args.NNsubtrain],y[:args.NNsubtrain]
            x3D,y3D=x3D[:args.NNsubtrain],y3D[:args.NNsubtrain]

        l=args.meta['descriptor']['length']//2


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
        self.x,self.y=torch.from_numpy(x),torch.from_numpy(y)
        self.xEx,self.yEx=torch.from_numpy(xEx),torch.from_numpy(yEx)
        self.training_sets.append(data.TensorDataset(self.x,self.y))
        self.test_sets.append(data.TensorDataset(self.xEx, self.yEx))

        self.x3D,self.y3D=torch.from_numpy(x3D),torch.from_numpy(y3D)
        self.xEx3D,self.yEx3D=torch.from_numpy(xEx3D),torch.from_numpy(yEx3D)
        self.training_sets3D.append(data.TensorDataset(self.x3D,self.y3D))
        self.test_sets3D.append(data.TensorDataset(self.xEx3D, self.yEx3D))

    def create3Dmodel(self):
        args=self.args
            
        if args.FourD.reuse3D:
            self.model3D=torch.load(f'{args.mlmodelout}/model3D.pt',map_location=self.device).to(self.device)  
            self.epoch3D=self.args.meta['3Dmodel']['Epoch']
            self.loss3D=self.args.meta['3Dmodel']['loss']
            if self.epoch3D + 2 > args.FourD.maxEpoch3D:
                return
        else:
            self.model3D = NN((self.x3D.shape[1]-6,512,256,128,64,1)).to(self.device)
            self.model3D.setNormalization(
                mX=self.x3D.mean(dim=0,keepdim=True)[:,args.FourD.ICdict['mask']],
                sX=self.x3D.std(dim=0,keepdim=True)[:,args.FourD.ICdict['mask']],
                mY=self.y3D.mean(dim=0,keepdim=True),
                sY=self.y3D.std(dim=0,keepdim=True),)
            self.model3D.setDevice(self.device)
        print(self.model3D)
        
        self.train3D()

    def train3D(self):
        args=self.args
        optimizer = optim.AdamW(params=self.model3D.parameters(),lr=0.001)
        # scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.995, verbose=False)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.5, patience=16, threshold=0)
        
        def loss_fn(model,xx,yy):
            xx=xx[:,args.FourD.ICdict['mask']].to(self.device).float()
            yy=yy.to(self.device).float()
            return torch.sqrt(torch.mean(torch.square(model(xx)-yy)))

        def validate(model,dataset):
            se=0.0
            count=0
            for xx,yy in data.DataLoader(dataset,batch_size=args.FourD.batchSize3D,shuffle=False):
                se+=torch.square(loss_fn(model,xx,yy)).item()*xx.shape[0]
                count+=xx.shape[0]
            return np.sqrt(se/count)

        def training_epoch(model,training_set,test_set):
            print('----------------------------------------------------')
            epoch_start= time.time()
            model.train()

            for batch, (xx, yy) in enumerate(data.DataLoader(training_set,batch_size=args.FourD.batchSize3D,shuffle=True)):
                loss=loss_fn(model,xx,yy)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            model.eval()
            # train_loss=validate(model,training_set)
            test_loss=validate(model,test_set)
            scheduler.step(test_loss)
            lr=optimizer.param_groups[0]['lr']
            if test_loss < self.loss3D:
                torch.save(model,f'{args.mlmodelout}/model3D.pt')
                self.loss3D=test_loss
                args.meta['3Dmodel']['bestEpoch']=self.epoch3D
                args.meta['3Dmodel']['loss']=float(self.loss3D)
                args.writeMeta()

            
            now=time.time()
            t_epoch=now-epoch_start
            print('epoch %-4d batch %-4d lr %.1e            t %6.1f       ' % (self.epoch3D,batch,lr,t_epoch))
            # print('\repoch %-6d %5d/%-5d         t_epoch: %10.1f       ' % (self.epoch3D,batch,batch,t_epoch))
            # print('train:     %-10.6f'% train_loss)
            print('validate:  %-10.6f'% test_loss)
            # print('validate:  %-10.6f'% ex_loss1)            
            print('best:      %-10.6f'% self.loss3D)

            
            args.meta['3Dmodel']['Epoch']=self.epoch3D
            self.epoch3D+=1
            if lr<1e-6:
                print('Early-stopping')
                self.epoch3D+=args.FourD.maxEpoch3D
            sys.stdout.flush()
        
        print(' training 3D model')        
        print("     Ntrain: ",self.y3D.shape[0])

        training_set=data.ConcatDataset(self.training_sets3D)
        test_set=data.ConcatDataset(self.test_sets3D)
        while True:
            if self.epoch3D >= args.FourD.maxEpoch3D: 
                break
            training_epoch(self.model3D,training_set,test_set)

        print(' 3D model trained')

    def create4Dmodel(self):
        args=self.args
        
        self.xlist=self.args.meta['descriptor']['xList']
        self.ylist=self.args.meta['descriptor']['yList']

        self.prepareData(args.Trajs)
        
        l=args.meta['descriptor']['length']//2

        if args.FourD.use3D:
            if type(args.FourD.use3D)==str:
                if args.FourD.use3D == 'ANI-1ccx':
                    pass
                else:
                    self.model3D=torch.load(f'{args.FourD.use3D}/model3D.pt',map_location=self.device).to(self.device) 
            elif args.FourD.use3D == 1:
                self.create3Dmodel()
        if args.FourD.reuse4D:
            self.model=torch.load(f'{args.mlmodelout}/model4D.pt',map_location=self.device).to(self.device)
            self.epoch4D=self.args.meta['4Dmodel']['Epoch']
            self.losses4D=tuple(self.args.meta['4Dmodel']['losses'])
            self.loss4D=self.losses4D[-1]
            if self.epoch4D + 1 >= args.FourD.maxEpoch4D:
                return
        else:
            self.model = NN((self.x.shape[1]-12,1024,512,256,128,64,l-6)).to(self.device)
            self.model.setNormalization(
                mX=self.x.mean(dim=0,keepdim=True)[:,args.FourD.ICdict['maskV']],
                sX=self.x.std(dim=0,keepdim=True)[:,args.FourD.ICdict['maskV']],
                mY=self.y[:,:l].mean(dim=0,keepdim=True)[:,args.FourD.ICdict['mask']],
                sY=self.y[:,:l].std(dim=0,keepdim=True)[:,args.FourD.ICdict['mask']],)
            self.model.setDevice(self.device)
        print(self.model)
        self.train4D()

    def train4D(self):
        args=self.args
        l=args.meta['descriptor']['length']//2
        if args.FourD.Descriptor.lower()=='ic':
            icidx=torch.tensor(args.meta["descriptor"]["ICdict"]['idx']).to(self.device)
        m=torch.tensor(args.meta['masses']).float().to(self.device)

        optimizer = optim.AdamW(params=self.model.parameters(),lr=0.001)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, factor=0.5, patience=16, threshold=0)
        # scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.995, verbose=False)
        
        def loss_fn_ic(model,x,y,model3D=None,checkEk=1,checkEp=1):   
            x=x[:,args.FourD.ICdict['maskV']].to(self.device).float().requires_grad_(True)
            y=y.to(self.device).float()

            ekerr=torch.tensor(0).to(self.device).float()
            eperr=torch.tensor(0).to(self.device).float()
            eterr=torch.tensor(0).to(self.device).float()
            ekbias=torch.tensor(0).to(self.device).float()
            epbias=torch.tensor(0).to(self.device).float()
            etbias=torch.tensor(0).to(self.device).float()
            w=torch.tensor(1).to(self.device).float()

            mp=model(x)
            vp=batch_jacobian(mp,x)[:,:,-1]
            vt=y[:,l:2*l][:,args.FourD.ICdict['mask']]
            mt=y[:,:l][:,args.FourD.ICdict['mask']]

            if args.FourD.checkV0:
                x0=torch.cat((x[:,:-1],x[:,-1:]*0),dim=1)
                v0p=(model(x0))*10
                v0t=x0[:,l:2*l]
                v0loss=torch.sqrt(torch.mean(torch.square(v0t-v0p)*w))
    

            if args.FourD.normalizeT:
                xx=x
                t=xx[:,[-1]]
                ft=1-torch.exp(-10*t)
                dftdt=10*torch.exp(-10*t)
                # mpic=mp*(1-torch.exp(-torch.square(t)))+xx[:,:l]+xx[:,l:2*l]*t
                # mtic=mt*(1-torch.exp(-torch.square(t)))+xx[:,:l]+xx[:,l:2*l]*t
                mpic=mp*ft+xx[:,:l-6]
                mtic=mt*ft+xx[:,:l-6]
                if checkEk:
                    vpic=vp*ft+dftdt*mp
                    vtic=vt*ft+dftdt*mt
                w=torch.exp(-t)+2*torch.exp(t-10)+1
            else:
                mpic=mp
                mtic=mt
                vpic=vp
                vtic=vp

            # deltaE=torch.exp(-10*tf.abs(xx[:,-2][:,None]))
            # w=xx[:,-1][:,None]/10*(torch.sqrt(deltaE)-deltaE)+deltaE
            
            if model3D and checkEp:
                Epp=model3D(((torch.remainder(mpic+semidivisor,2*semidivisor)-semidivisor)))
                Ept=model3D(((torch.remainder(mtic+semidivisor,2*semidivisor)-semidivisor)))
                eperr=torch.sqrt(torch.mean(torch.square((Epp-Ept)*w)))
                epbias=torch.mean((Epp-Ept)*w)

            if checkEk:
                descrp=torch.ones((mpic.shape[0],mpic.shape[1]*2+12)).to(self.device)
                descrt=torch.ones((mtic.shape[0],mtic.shape[1]*2+12)).to(self.device)
                descrp[:,args.FourD.ICdict['maskV'][:-1]]=torch.cat((mpic,vpic),1)
                descrt[:,args.FourD.ICdict['maskV'][:-1]]=torch.cat((mtic,vtic),1)
                mpxyz,vpxyz=unDescribeTorch(descrp,icidx,self.device)
                mtxyz,vtxyz=unDescribeTorch(descrt,icidx,self.device)
                vpxyz=adjVtorch(mpxyz,vpxyz,m,device=self.device)
                vtxyz=adjVtorch(mtxyz,vtxyz,m,device=self.device)
                # print(vpxyz[0])
                # print(vtxyz[0])
                # print((vpxyz-vtxyz)[0])
                Ekp=getEkTorch(vpxyz,m)
                # Ekt=y[:,-2] if 'ek' in args.FourD.ylist else getEkTorch(vtxyz,m)
                Ekt=getEkTorch(vtxyz,m)
                # print(Ekp[0])
                # print(Ekt[0])
                if torch.sum(torch.isnan(Ekt)):
                    print(x[torch.isnan(Ekt)],mtic[torch.isnan(Ekt)],vtic[torch.isnan(Ekt)])
                if torch.sum(torch.isnan(Ekp)):
                    print(x[torch.isnan(Ekp)],mpic[torch.isnan(Ekp)],vpic[torch.isnan(Ekp)])
                ekerr=torch.sqrt(torch.mean(torch.square((Ekp-Ekt)*w)))
                ekbias=torch.mean((Ekp-Ekt)*w)
                eterr=torch.sqrt(torch.mean(torch.square((Ekp-Ekt+Epp-Ept)*w)))
                etbias=epbias+ekbias
            

            mloss=torch.sqrt(torch.mean(torch.square((mp-mt)*w),dim=0))
            vloss=torch.sqrt(torch.mean(torch.square((vp-vt)*w),dim=0))
            Dloss=torch.mean(mloss[:ld])
            Aloss=torch.mean(mloss[ld:ld+la])
            DAloss=torch.mean(mloss[ld+la:])
            vDloss=torch.mean(vloss[:ld])
            vAloss=torch.mean(vloss[ld:ld+la])
            vDAloss=torch.mean(vloss[ld+la:])
            vbias=(torch.mean((vp-vt)*w))
            # vbias=torch.abs(torch.mean(vt-vp))
            loss=1.0*Dloss+2.0*Aloss+4.0*DAloss+16.0*vDloss+20.0*vAloss+24.0*vDAloss+16.*eperr+16.*ekerr+16.*eterr+torch.abs(16.*epbias+16.*ekbias+16.*etbias+16.*vbias)
            return Dloss,Aloss,DAloss,eperr,ekerr,eterr,vDloss,vAloss,vDAloss,epbias,ekbias,etbias,vbias,loss

        if args.FourD.Descriptor.lower()=='ic':
            la=l//3-2
            ld=la-1
            lda=la+1
            semidivisor=torch.tensor([100]*ld+[np.pi]*(la+lda)).to(self.device).float()
            loss_fn=loss_fn_ic

        def validate(model,dataset):
            se=np.zeros(14 if args.FourD.Descriptor.lower()=='ic' else 5)
            count=0
            for xx,yy in data.DataLoader(dataset,batch_size=args.FourD.batchSize4D,shuffle=False):
                n=xx.shape[0]
                se+=np.square([loss.cpu().detach().numpy() for loss in loss_fn(model,xx,yy,model3D=self.model3D if self.model3D else None)])*n
                count+=n
            return tuple(np.sqrt(se/count))

        def training_epoch(model,training_set,test_set):
            print('--------------------------------------------------------------------------')
            epoch_start= time.time()
            model.train()
            for batch, (xx,yy) in enumerate(data.DataLoader(training_set,batch_size=args.FourD.batchSize4D,shuffle=True)):
                *_,loss=loss_fn(model,xx,yy,self.model3D,checkEk=args.FourD.checkEk,checkEp=1)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            model.eval()

            # train_losses=validate(model,training_set)
            test_losses=validate(model,test_set)
            scheduler.step(test_losses[-1])
            # scheduler.step()
            lr=optimizer.param_groups[0]['lr']
            if test_losses[-1] < self.loss4D:
                torch.save(model,f'{args.mlmodelout}/model4D.pt')
                self.loss4D=test_losses[-1]
                self.losses4D=test_losses
                args.meta['4Dmodel']['bestEpoch']=self.epoch4D
                args.meta['4Dmodel']['losses']=[loss.astype(float) for loss in self.losses4D]
                args.writeMeta()

            now=time.time()
            t_epoch=now-epoch_start
            print('%-10s %-10s %-10s %-10s %-10s %-10s %-10s'% ('epoch %-4d'%self.epoch4D,'batch %-4d'%batch,'','','lr %.1e'%lr,'','t %6.1f'%t_epoch))
            if args.FourD.Descriptor.lower()=='ic':
                print('%-10s %-10s %-10s %-10s %-10s %-10s %-10s'% (self.msg,"D","A","DA","Ep","Ek","Et"))
                print('validate | %-10.6f %-10.6f %-9.6f| %-10.6f %-10.6f %-10.6f\nd/dt|bias| %-10.6f %-10.6f %-9.6f| %-10.6f %-10.6f %-10.6f\n                          bias   %-9.6f                 Loss   %-10.6f'% test_losses)            
                print('best     | %-10.6f %-10.6f %-9.6f| %-10.6f %-10.6f %-10.6f\nd/dt|bias| %-10.6f %-10.6f %-9.6f| %-10.6f %-10.6f %-10.6f\n                          bias   %-9.6f                 Loss   %-10.6f'% self.losses4D)
            
            args.meta['4Dmodel']['Epoch']=self.epoch4D
            self.epoch4D+=1
            if lr<1e-6:
                print('Early-stopping')
                self.epoch4D+=args.FourD.maxEpoch4D
            sys.stdout.flush()
            
        
        print('training 4D model')
        training_set=data.ConcatDataset(self.training_sets)
        test_set=data.ConcatDataset(self.test_sets)
        while True:
            if self.epoch4D >= args.FourD.maxEpoch4D: 
                break
            training_epoch(self.model,training_set,test_set)
        print('4D model trained')

    def use4Dmodel(self, xyz0=None,v0=None, sp=None, tRun=0 ,trajName=None,tSegMax=0):
        args=self.args
        
        tRun=args.trun if tRun==0 else tRun
        tSegMax=args.tSegm if tSegMax==0 else tSegMax
        
        icdict=args.meta["descriptor"]["ICdict"]
        m=np.array(args.meta['masses'])

        l=args.meta['descriptor']['length']//2
        la=l//3-2
        ld=la-1
        lda=la+1
        # path=args.FourD.MD.dirOut
        # os.system(f'mkdir {path}')

        tm=args.trun

        
        dt=args.dt
        if xyz0 is None or v0 is None or sp is None :
            [xyz0, *_],[sp, *_] =loadXYZ(args.initXYZ,list)
            [v0, *_], _ = loadXYZ(args.initVXYZ,list,getsp=False)

        xyzoffset=getCoM(xyz0,m)
        voffset=getCoM(v0,m)
        x0=Describe(xyz0[np.newaxis],v0[np.newaxis],icdict,m=m)[:,args.FourD.ICdict['maskV'][:-1]]
        ts=np.arange(0,tm,dt)+dt
        ts[-1]=tm
        t0=0
        
        if not trajName: trajName=args.trajName
        xyzfile=trajName+'.xyz'
        vxyzfile=trajName+'.vxyz'
        ft=open(trajName+'.t','w')
        fek=open(trajName+'.ekin','w')
        fy=open(trajName+'.y','w')
        fep=open(trajName+'.epot','w')
        fet=open(trajName+'.etot','w')
        print(trajName)

        ek=getEk(v0,m)[np.newaxis][np.newaxis]
        if args.FourD.use3D=='ANI-1ccx' or '4Dethanol_torch' in str(args.FourD.use3D):
            ep=getANI1ccxPot(xyz0[np.newaxis], self.z)
        elif self.model3D:
            ep=self.model3D(x0[:,:l-6])
        else:
            ep=np.zeros_like(ek)
        etot=(ep+ek)[0,0]
        P0=getLinM(v0,m)
        L0=getAngM(xyz0,v0,m)
        Eerror=0
        np.savetxt(fek,ek)
        np.savetxt(fep,ep)
        np.savetxt(fet,(ep+ek))
        np.savetxt(fy,x0)
        saveXYZ(xyzfile,xyz0,sp,'w',msg=f't=0.0fs')
        saveXYZ(vxyzfile,v0,sp,'w',msg=f't=0.0fs')
        ft.write('0.0\n')
        

        def getY(x, model):
            y=model.predict(x).cpu().detach().numpy()
            if np.sum(np.isnan(y)) > 0:
                stopper.stopMLatom('prediction failed')
                
            if args.FourD.normalizeT:
                x,y=unnormalizeT(x,y,l=l-6,a=self.normalizeTfactor)
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
            yy=np.ones((y.shape[0],y.shape[1]+12))
            yy[:,args.FourD.ICdict['maskV'][:-1]]=y
            # yy[:,[0,9,10,18,19,20]]=np.array([ 1.44915205,  0.53537275,  0.9038438 ,  0.95050887,  1.5841834 , -0.58186192])
            xyz,v=unDescribe(yy,icdict['idx'])
            xyz=xyz-getCoM(xyz,m)
            xyz=xyz+xyzoffset+voffset*(x[:,[-1],np.newaxis]+t0)
            v=v-getCoM(v,m)+voffset
            for i in range(len(v)):
                # print(xyz[i].shape,v[i].shape,P0.shape,L0.shape)
                v[i]=adjV(xyz[i],v[i],m)
            y=Describe(xyz,v,icdict,m=m)[:,args.FourD.ICdict['maskV'][:-1]]
            ek=getEks(v,m)[:,np.newaxis]
            ep=np.zeros_like(ek)
            if args.FourD.use3D=='ANI-1ccx' or '4Dethanol_torch' in str(args.FourD.use3D):
                ep=getANI1ccxPot(xyz, self.z)
            elif self.model3D:
                ep=self.model3D(y[:,:l-6])
            if args.FourD.forceEtot:
                v=v*np.sqrt((etot-ep)/ek)[:,np.newaxis,np.newaxis]
                ek=getEks(v,m)
                # x0=Describe(xyz[[-1]],v[[-1]],icdict,m=m).astype(np.float32)

            # print(ek)
            # print(ep)
            # print(etot)
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
            ep=self.model3D(y[:,:l])
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
            ep=self.model3D(y[:,:l])
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
            ep=self.model3D(torch.tensor(y[:,:l]))
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
            saveXYZs(xyzfile,xyz,sp,'a',msgs=tstamps)
            saveXYZs(vxyzfile,v,sp,'a',msgs=tstamps)

            np.savetxt(fek,ek)
            np.savetxt(fy,y)
            for tstamp in tstamps:
                ft.write(tstamp+'\n')
            return

        Segms=[]
        pdict={0:0}
        tbreak=0
        threshold=8
        while t0 < tm:
            if args.FourD.adaptSeg:
                tSegm=findNextT0(x0)
            else:
                tSegm=tSegMax

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
                # print([result[-1][-1,-1].cpu().detach().numpy()*627.5 for result in results])
                Eerrors=np.abs([result[-1][-1,-1] for result in results]).flatten()
                # print(Eerrors)
                sort=np.argsort(Eerrors)
                self.model=self.models[sort[pdict[t0]]]
                print(sort[pdict[t0]],Eerrors[sort[pdict[t0]]]*627.5)
                if np.abs(Eerrors[sort[pdict[t0]]])*627.5>threshold or pdict[t0]>=len(sort)-1:
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
                x0, xyzt, vt, ekt ,ept, Eerror=results[sort[pdict[t0]]]

            else:
                x0, xyzt, vt, ekt ,ept, Eerror =getAll(xSegm, self.model)
            Segms.append([getAll(x, self.model),['%.3f fs %s' % (i, 'model'+str(sort[pdict[t0]]) if self.args.MLmodelsIn else '') for i in t+t0],x0])
            if len(Segms)>10:
                saveResult(*Segms[0][:-1])
                Segms.pop(0)
            
            print(' %.2f-%.2f fs'% (t0,t0+tSegm))
            print(f'Etot error: {(Eerror[-1,-1])*627.5} kcal/mol')
            

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
        return x0[-1], xyzt[-1], vt[-1], ekt[-1], ept[-1], Eerror[-1]
            

        # h5file=File(args.trajH5MDout,'w')
        # part=h5file.particles_group('all')
        # part.create_box(dimension=3, boundary=['none','none','none'])
        # part_pos=element(part,'position',store='time',shape=xyz0.shape,dtype=np.float32, time=True)
        # part_descr=element(part,'descriptor',store='time',shape=descr.shape,dtype=np.float32, time=True)
        # part_pos.append(xyz0,0,0.0)
        # part_descr.append(descr,0,0.0)
        # h5file.observables = h5file.require_group('observables')
        # element(part, 'names', data=np.array([bytes('%-2s'%name,'utf-8')for name in sp]), store='fixed')
        # h5file.close()
    def estAcc4Dmodel(self):
        pass
        
    def activeLearning(self):
        args=self.args
        tc=1
        self.Niter=0

        os.system(f'mkdir {args.MLmodelOut}')
        if not os.path.isdir(f'{args.MLmodelOut}/4DMD'): os.system(f'mkdir {args.MLmodelOut}/4DMD')
        if not os.path.isdir(f'{args.MLmodelOut}/3DMD'): os.system(f'mkdir {args.MLmodelOut}/3DMD')

        xyzs,sps =loadXYZ(args.initXYZ)
        vs, _ = loadXYZ(args.initVXYZ,getsp=False)

        Ntrajs=args.Ntrajs
        trajidx=np.arange(Ntrajs)
        
        manager = Manager()
        newtrajs=manager.list()
        os.system(f'mkdir {args.MLmodelOut}/3DMD/{self.Niter}')
        # global run3D
        # def run3D(xyz0,v0,sp,trajName,returnList):
        #     returnList.append(self.run3DMD(xyz0,v0,sp,trajName))
        
        # pool=Pool(args.nthreads)
        # pool.starmap(run3D,[(xyzs[j],vs[j],sps[j],f'traj_{j}',newtrajs) for j in trajidx])
        # pool.close()

        # processes=[]
        # for j in trajidx:
        #     p = Process(target = run3D, args=(xyzs[j],vs[j],sps[j],f'traj_{j}',newtrajs))
        #     processes.append(p)
        #     p.start()
            
        # for p in processes:
        #     p.join()
        newtrajs=[]
        for j in trajidx:
            newtrajs.append(self.run3DMD(xyzs[j],vs[j],sps[j],f'traj_{j}'))

        Nmodel=len(args.ICidx)

        models=[]
        for i in range(Nmodel):
            newargs=addReplaceArg('activeLearning','create4Dmodel',args.args2pass)
            newargs=addReplaceArg('ICidx',f'ICidx={args.ICidx[i]}',newargs)
            newargs=addReplaceArg('MLmodelOut',f'MLmodelOut={args.MLmodelOut}/ALmodel{i}',newargs)
            newargs=addReplaceArg('Trajs',f'Trajs={",".join(newtrajs)}',newargs)
            newargs=addReplaceArg('tc',f'tc={tc}',newargs)
            
            models.append(FourDcls(newargs, msg=f'AL_{i}'))
            # models.append(FourDcls(newargs))
        
        # global create4DAL

        # def create4DAL(model):
        #     model.create4Dmodel()

        # pool=Pool(Nmodel)
        # pool.map(create4DAL,[models[i] for i in range(Nmodel)])
        # pool.close()
        for i in range(Nmodel):
            # if i>0 and args.ICidx[i]==args.ICidx[-1] and not args.FourD.reuse3D and not args.FourD.reuse4D:
            #     os.system(f'rm -rf {args.MLmodelOut}/ALmodel{i}; cp -r {args.MLmodelOut}/ALmodel{i-1} {args.MLmodelOut}/ALmodel{i}')
            #     newargs=addReplaceArg('FourD.reuseData','FourD.reuseData=1',newargs)
            print(f" training ALmodel{i}...")
            models[i].create4Dmodel()

        # processes=[]
        # for i in range(Nmodel):
        #     p = Process(target = models[i].create4Dmodel)
        #     p.start()
        #     processes.append(p)
            
        # for p in processes:
        #     p.join()
        
        while True:
            error=0
            print(f'tc={tc}')
            self.Niter+=1
            path=f'{args.MLmodelOut}/4DMD/{self.Niter}'
            os.system(f'mkdir {path}')
            xyzts=[]
            vts=[]
            yts=[]
            Eerrors=[]
            try:
                for i in range(Nmodel):
                    os.system(f'mkdir {path}/{i}')
                    xyzts.append([])
                    vts.append([])
                    yts.append([])
                    Eerrors.append([])

                    for j in trajidx:
                        print(f" running 4DMD with ALmodel{i}...")
                        yt,xyzt,vt,_,_,Eerror=models[i].use4Dmodel(xyzs[j],vs[j],sps[j],tc,f'{path}/{i}/traj{j}',tc)
                        xyzts[-1].append(xyzt)
                        vts[-1].append(vt)
                        yts[-1].append(yt)
                        Eerrors[-1].append(Eerror)

                sdxyz=np.std(np.array(xyzts),axis=0)
                sdv=np.std(np.array(vts),axis=0)
                sdy=np.std(np.array(yts),axis=0)
                # print(f' SD of finial geometries:\n{sdxyz}')
                # print(f' SD of finial velocities:\n{sdv}')
                # print(f' SD of finial descriptors:\n{sdy.reshape(2,3,-1).transpose(0,2,1)}')
                # sd=np.mean(sdxyz)+np.mean(sdv)
                sd=np.mean(sdxyz)
                print(f' SDxyz: {sd} SD Etot: {np.std(Eerrors)*627.5} Min Etot Error: {np.min(np.abs(Eerrors))*627.5}')

                xyzs[trajidx]=np.mean(np.array(xyzts),axis=0)
                vs[trajidx]=np.mean(np.array(vts),axis=0)
            except:
                error=1
                print('Error!')
            trajidx=(trajidx+Ntrajs)%len(vs)


            if error or sd >0.1 or np.isnan(sd) or np.min(np.abs(Eerrors))*627.5>1 or np.std(Eerrors)*627.5>10:
                os.system(f'mkdir {args.MLmodelOut}/3DMD/{self.Niter}')
                newtrajs=[]
                for j in trajidx:
                    newtrajs.append(self.run3DMD(xyzs[j],vs[j],sps[j],f'traj_{j}'))
                for i in range(Nmodel):
                    models[i].prepareData(newtrajs,tc=tc)
                    print(f' retraining ALmodel{i}...')
                    # models[i].train3D()
                    models[i].epoch4D=0
                    models[i].loss4D=np.inf
                    models[i].train4D()
            elif tc+1<=args.tc:
                tc+=1
    
    def run3DMD(self,xyz0,v0,sp,trajName):
        args=self.args
        path=f'{args.MLmodelOut}/3DMD/{self.Niter}'
        saveXYZ(f'{path}/{trajName}_init.xyz',xyz0,sp)
        saveXYZ(f'{path}/{trajName}_init.vxyz',v0,sp)
        args3D=addReplaceArg('activeLearning','create4Dmodel',args.args2pass)
        args3D=addReplaceArg('device',f'device=cpu',args3D)
        args3D=addReplaceArg('initXYZ',f'initXYZ={path}/{trajName}_init.xyz',args3D)
        args3D=addReplaceArg('initVXYZ',f'initVXYZ={path}/{trajName}_init.vxyz',args3D)
        args3D=addReplaceArg('trajXYZout',f'trajXYZout={path}/{trajName}.xyz',args3D)
        args3D=addReplaceArg('trajVXYZout',f'trajVXYZout={path}/{trajName}.vxyz',args3D)
        args3D=addReplaceArg('trajTime',f'trajTime={path}/{trajName}.t',args3D)
        args3D=addReplaceArg('trajEpot',f'trajEpot={path}/{trajName}.epot',args3D)
        args3D=addReplaceArg('trajEkin',f'trajEkin={path}/{trajName}.ekin',args3D)
        args3D=addReplaceArg('trajEtot',f'trajEtot={path}/{trajName}.etot',args3D)
        args3D=addReplaceArg('trajH5MDout',f'trajH5MDout={path}/{trajName}.h5',args3D)
        # print(" models didn't meet criteria, runing 3DMD...")
        import ThreeDMD
        ThreeDMD.ThreeDcls.dynamics(args3D)
        return f'{path}/{trajName}.h5'

    def reactionPath(self):
        args=self.args
        from scipy.optimize import dual_annealing
        
        icdict=args.meta["descriptor"]["ICdict"]
        # model=torch.load(f'{args.mlmodelin}/4D_model')
        # model3D=torch.load(f'{args.mlmodelin}/3D_model')

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
                # eperr=np.abs(epest[-1,0]-ept)
                barrier=abs(np.max(epest)-ep0.numpy())
                # print('rmsd: %12.4f     eperr: %12.4f     barrier: %12.4f' % (rmsd,eperr,barrier))
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
            saveXYZ(f'{path}/mol{i}_v0.xyz', res.x.reshape(9,3)/0.529177210903*24.188843265e-3*100,sp)
            
            saveXYZ(args.initVout, res.x.reshape(9,3)/0.529177210903*24.188843265e-3*100,sp)

            x=np.concatenate((np.repeat(Describe(xyz0[np.newaxis],res.x.reshape(1,9,3)*100,icdict),int(args.reactionTime/step),axis=0),((np.arange(int(args.reactionTime/step))+1)*step)[:,np.newaxis]),axis=1)
            y=predict(self.model,x,tc=args.FourD.tc,x_shift=x_shift,x_scale=x_scale,y_shift=y_shift)
            theOppositeWayToCorrectAngle(y,idx=list(range(ld,l)))
            xyzs,v=unDescribe(y,icdict['idx'])
            # slider=np.zeros(xyzs.shape)
            # slider[:,:,0]=np.repeat(((np.arange(200)+1)/10-10)[:,np.newaxis],9,axis=1)
            # xyzs-=slider
            saveXYZs(f'{path}/mol{i}_reactionPath.xyz',xyzs,sp)
            np.savetxt(f'{path}/mol{i}_reactionPath.y',y)
            ep=self.model3D((y[:,:l]-m_shift)/m_scale)+ep_shift
            np.savetxt(f'{path}/mol{i}_reactionPath.ep',ep)

