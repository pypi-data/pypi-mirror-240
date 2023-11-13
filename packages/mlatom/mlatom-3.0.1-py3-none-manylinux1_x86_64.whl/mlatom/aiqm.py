#!/usr/bin/env python3
'''
.. code-block::

  !---------------------------------------------------------------------------! 
  ! AIQM: Artificial intelligence quantum-mechanical method                   ! 
  ! Implementations by: Peikung Zheng & Yuxinxin Chen                         ! 
  !---------------------------------------------------------------------------! 
'''

import os
import numpy as np
from . import models
from . import stopper
from . import data             

#import numdifftools as nd
# Get TorchANI
try: 
    import torch
    import torchani
    from torchani.utils import ChemicalSymbolsToInts
    from torchani.units import hartree2kcalmol
except:
    raise ValueError('Please install all Python modules required for TorchANI')


class aiqm(models.model):
    """
    The Artificial intelligence-quantum mechanical method:
    QM baseline + NN correction + other corrections

    Arguments:
        method (str): AIQM1 methods and 'aiqm'. If 'aiqm' is given, user needs to provide each part of aiqm method.
        qm_kwargs (dict optional): keywords used in QM method 
        baseline (dict): dictionary of keywords that define baseline QM method, please refer to QM interfaces in mlatom
        MLs (list): a list of paths of ML models that used in NN correction
        sae (dict): self atomic energy used in ANI neural network
        d4 (dict): dictionary of keywords that define d4 method, please refer to dftd4 interface
    
    .. code-block:: python

        # Initialize molecule
        mol = ml.data.molecule()
        mol.read_from_xyz_file(filename='ethanol.xyz')
        # Run AIQM calculation
        aiqm = ml.models.methods(method='aiqm', 
                                 baseline={'type': 'method', 'method': 'GFN2-xTB'},
                                 MLs=['model1.py', 'model2.pt],
                                 sae={1: -0.60359714, 6:-38.03882037, 7: -54.66985925, 8: -75.16565028},
                                 d4={'type': 'method', 'method': 'GFN2-xTB', 'functional': 'wb97x'})
        aiqm1.predict(molecule=mol)
        # Get energy of AIQM method 
        energy = mol.energy

    """
    available_methods = models.methods.methods_map['aiqm'][:-1]
    atomic_energies = {'AIQM1': {1:-0.50088038, 6:-37.79221710, 7:-54.53360298, 8:-75.00986203},
                       'AIQM1@DFT': {1:-0.50139362, 6:-37.84623117, 7:-54.59175573, 8:-75.07674376}}
    atomic_energies['AIQM1@DFT*'] = atomic_energies['AIQM1@DFT']
    

    def __init__(self, method='', qm_kwargs={}, **kwargs):
        mlatomdir=os.path.dirname(__file__)
        self.children_list = []

        if method in self.available_methods:

            if method == 'AIQM1':
                self.baseline = {'type': 'method', 'method': 'odm2*', 'program':'mndo', 'method_kwargs':qm_kwargs}          
                ML_dirname = os.path.join(mlatomdir, 'aiqm1_model')
                self.MLs = [f'{ML_dirname}/aiqm1_cc_cv{ii}.pt' for ii in range(8)]
                self.d4 = {'type': 'method', 'method': 'D4', 'functional':'wb97xtz'}
                self.sae = {1: -4.29365862e-02, 6: -3.34329586e+01, 7: -4.69301173e+01, 8: -6.29634763e+01}

            if method == 'AIQM1@DFT':
                self.baseline = {'type': 'method', 'method': 'odm2', 'program':'mndo', 'method_kwargs':qm_kwargs}          
                ML_dirname = os.path.join(mlatomdir, 'aiqm1_model')
                self.MLs = [f'{ML_dirname}/aiqm1_dft_cv{ii}.pt' for ii in range(8)]
                self.d4 = {'type': 'method', 'method': 'D4', 'functional':'wb97xtz'}
                self.sae = {1: -4.27888067e-02, 6: -3.34869833e+01, 7: -4.69896148e+01, 8: -6.30294433e+01}
                
            if method == 'AIQM1@DFT*':
                self.baseline = {'type': 'method', 'method': 'odm2', 'program':'mndo', 'method_kwargs':qm_kwargs}          
                ML_dirname = os.path.join(mlatomdir, 'aiqm1_model')
                self.MLs = [f'{ML_dirname}/aiqm1_dft_cv{ii}.pt' for ii in range(8)]
                self.sae = {1: -4.27888067e-02, 6: -3.34869833e+01, 7: -4.69896148e+01, 8: -6.30294433e+01}
                
            # if method == 'AIQM1u.wb97xdef2tzvpp_8aninnstar_d4wb97x_shift_20230220':
            #     self.baseline = models.model_tree_node(name='baseline', operator='predict',model=models.methods(method='wb97x/def2-tzvpp', program='orca', method_kwargs=qm_kwargs))
            #     ML = [models.model_tree_node(name=f'nn_{ii}', operator='predict', 
            #           model=ani_nns_in_aiqm(model_file=f'/export/home/chenyxx/project/aiqm/aiqm-wb97x-d4/cv{ii}/energy-training-best.pt')) for ii in range(8)]
            #     self.MLs = models.model_tree_node(name='nns', children=ML, operator='average')
            #     self.other_corrections = [models.model_tree_node(name='d4', operator='predict', model=models.methods(method='D4', functional='wb97x')),
            #                               models.model_tree_node(name='aes', operator='predict', model=atomic_energy_shift(method='AIQM1u.wb97xdef2tzvpp_8aninnstar_d4wb97x_shift_20230220'))]
            #     children_list = [self.baseline, self.MLs] + self.other_corrections

            # if method == 'AIQM1u.wb97x631Gd_8aninnstar_d4wb97x_shift_20230407':
            #     self.baseline = models.model_tree_node(name='baseline', operator='predict',model=models.methods(method='wb97x/6-31G*', program='Gaussian', **qm_kwargs))
            #     ML = [models.model_tree_node(name=f'nn_{ii}', operator='predict', 
            #           model=ani_nns_in_aiqm(model_file=f'/export/home/chenyxx/project/aiqm/aiqm-model/AIQM1u_wb97xdz_ani_d4wb97x_shift_20230406/cv{ii}/energy-training-best.pt')) for ii in range(8)]
            #     self.MLs = models.model_tree_node(name='nns', children=ML, operator='average')
            #     self.other_corrections = [models.model_tree_node(name='d4', operator='predict', model=models.methods(method='D4', functional='wb97x')),
            #                               models.model_tree_node(name='aes', operator='predict', model=atomic_energy_shift(method='AIQM1u.wb97x631Gd_8aninnstar_d4wb97x_shift_20230407'))]
            #     children_list = [self.baseline, self.MLs] + self.other_corrections

            # if method == 'AIQM0u.8aninnstar_d4wb97x_shift_20230220':
            #     ML_dirname = '/export/home/chenyxx/project/aiqm/ani-1ccx-d4/transfer_ccsdtstar/'
            #     ML = [models.model_tree_node(name='nn_0', operator='predict', model=ani_nns_in_aiqm(model_file=f'{ML_dirname}/pretrain_rca4_transfer_rca4_layer24.pt'))]
            #     self.MLs = models.model_tree_node(name='nns', children=ML, operator='average')
            #     self.other_corrections = [models.model_tree_node(name='d4', operator='predict', model=models.methods(method='D4', functional='wb97x')),
            #                         models.model_tree_node(name='aes', operator='predict', model=atomic_energy_shift(method='AIQM0u.8aninnstar_d4wb97x_shift_20230220'))]
            #     children_list = [self.MLs] + self.other_corrections
            
        else:
            
            self.baseline = kwargs['baseline'] if 'baseline' in kwargs else None
            self.MLs = kwargs['MLs'] if 'MLs' in kwargs else None
            self.sae = {} if 'sae' in kwargs else None

            sae = kwargs['sae']
            for ac, ee in sae.items():
                self.sae[int(ac)] = float(ee)
            self.d4 = kwargs['d4'] if 'd4' in kwargs else None

    
    def predict_for_molecule(self, molecule=None,
                calculate_energy=True, calculate_energy_gradients=False, calculate_hessian=False):
        
        for atom in molecule.atoms:
            if not atom.atomic_number in [1, 6, 7, 8]:
                print(' * Warning * Molecule contains elements other than CHNO, no calculations performed')
                return
        self.aiqm_model.predict(molecule=molecule,
                            calculate_energy=calculate_energy, calculate_energy_gradients=calculate_energy_gradients, calculate_hessian=calculate_hessian)
        
        properties = [] ; atomic_properties = []
        if calculate_energy: properties.append('energy')
        if calculate_energy_gradients: atomic_properties.append('energy_gradients')
        if calculate_hessian: properties.append('hessian')
        molecule.__dict__['nns'].standard_deviation(properties=properties+atomic_properties)

    def predict(self, **kwargs):

        self.load()

        if kwargs['molecular_database'] != None:
            molDB = kwargs['molecular_database']
        elif kwargs['molecule'] != None:
            molDB = data.molecular_database()
            molDB.molecules.append(kwargs['molecule'])
        else:
            errmsg = 'Either molecule or molecular_database should be provided in input'
            raise ValueError(errmsg)

        if 'calculate_energy' in kwargs:
            calculate_energy = kwargs['calculate_energy']
        else:
            calculate_energy = True
        if 'calculate_energy_gradients' in kwargs:
            calculate_energy_gradients = kwargs['calculate_energy_gradients']
        else:
            calculate_energy_gradients = False
        if 'calculate_hessian' in kwargs:
            calculate_hessian = kwargs['calculate_hessian']
        else:
            calculate_hessian = False
        
        for mol in molDB.molecules:
            self.predict_for_molecule(molecule=mol, calculate_energy=calculate_energy, calculate_energy_gradients=calculate_energy_gradients, calculate_hessian=calculate_hessian)

    def load(self):
        if self.baseline:
            self.baseline['type'] = 'method'
            baseline = models.load_dict(self.baseline)
            baseline = models.model_tree_node(name='baseline', operator='predict', model=baseline)
            self.children_list.append(baseline)
        if self.MLs:
            MLs = [models.model_tree_node(name = f'nn_{ii}', operator='predict', model=ani_nns_in_aiqm(model_file=ML)) for ii, ML in enumerate(self.MLs)]
            MLs = models.model_tree_node(name='nns', operator='average', children=MLs)
            self.children_list.append(MLs)
        if self.sae:
            SAE = atomic_energy_shift(sae=self.sae)
            SAE = models.model_tree_node(name='sae', operator='predict', model=SAE)
            self.children_list.append(SAE)
        if self.d4:
            self.d4['type'] = 'method'
            d4 = models.load_dict(self.d4)
            d4 = models.model_tree_node(name='d4', operator='predict', model=d4)
            self.children_list.append(d4)
        self.aiqm_model = models.model_tree_node(name='aiqm', children=self.children_list, operator='sum')
        
        
class ani_nns_in_aiqm():
    species_order = [1, 6, 7, 8]
    
    def __init__(self, model_file=None):
        self.model_file = model_file
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.define_aev()
        self.load_models()
    
    def define_aev(self):
        Rcr = 5.2000e+00
        Rca = 4.0000e+00
        EtaR = torch.tensor([1.6000000e+01], device=self.device)
        ShfR = torch.tensor([9.0000000e-01, 1.1687500e+00, 1.4375000e+00, 1.7062500e+00, 1.9750000e+00, 2.2437500e+00, 2.5125000e+00, 2.7812500e+00, 3.0500000e+00, 3.3187500e+00, 3.5875000e+00, 3.8562500e+00, 4.1250000e+00, 4.3937500e+00, 4.6625000e+00, 4.9312500e+00], device=self.device)
        Zeta = torch.tensor([3.2000000e+01], device=self.device)
        ShfZ = torch.tensor([1.9634954e-01, 5.8904862e-01, 9.8174770e-01, 1.3744468e+00, 1.7671459e+00, 2.1598449e+00, 2.5525440e+00, 2.9452431e+00], device=self.device)
        EtaA = torch.tensor([8.0000000e+00], device=self.device)
        ShfA = torch.tensor([9.0000000e-01, 1.6750000e+00,  2.4499998e+00, 3.2250000e+00], device=self.device)
        num_species = len(self.species_order)
        aev_computer = torchani.AEVComputer(Rcr, Rca, EtaR, ShfR, EtaA, Zeta, ShfA, ShfZ, num_species)
        self.aev_computer = aev_computer

    def load_models(self):
        self.define_nn()
        checkpoint = torch.load(self.model_file, map_location=self.device)
        self.nn.load_state_dict(checkpoint['nn'])
        model = torchani.nn.Sequential(self.aev_computer, self.nn).to(self.device).double()
        self.model = model

    def define_nn(self):
        aev_dim = self.aev_computer.aev_length
        H_network = torch.nn.Sequential(
            torch.nn.Linear(aev_dim, 160),
            torch.nn.GELU(),
            torch.nn.Linear(160, 128),
            torch.nn.GELU(),
            torch.nn.Linear(128, 96),
            torch.nn.GELU(),
            torch.nn.Linear(96, 1)
        )
        
        C_network = torch.nn.Sequential(
            torch.nn.Linear(aev_dim, 144),
            torch.nn.GELU(),
            torch.nn.Linear(144, 112),
            torch.nn.GELU(),
            torch.nn.Linear(112, 96),
            torch.nn.GELU(),
            torch.nn.Linear(96, 1)
        )
        
        N_network = torch.nn.Sequential(
            torch.nn.Linear(aev_dim, 128),
            torch.nn.GELU(),
            torch.nn.Linear(128, 112),
            torch.nn.GELU(),
            torch.nn.Linear(112, 96),
            torch.nn.GELU(),
            torch.nn.Linear(96, 1)
        )
        
        O_network = torch.nn.Sequential(
            torch.nn.Linear(aev_dim, 128),
            torch.nn.GELU(),
            torch.nn.Linear(128, 112),
            torch.nn.GELU(),
            torch.nn.Linear(112, 96),
            torch.nn.GELU(),
            torch.nn.Linear(96, 1)
        )
        
        nn = torchani.ANIModel([H_network, C_network, N_network, O_network])
        self.nn = nn

    def predict(self, molecular_database=None, molecule=None,
                calculate_energy=True, calculate_energy_gradients=False, calculate_hessian=False):
        if molecular_database != None:
            molDB = molecular_database
        elif molecule != None:
            molDB = data.molecular_database()
            molDB.molecules.append(molecule)
        else:
            errmsg = 'Either molecule or molecular_database should be provided in input'
            raise ValueError(errmsg)
        
        species_to_tensor = ChemicalSymbolsToInts(self.species_order)
        
        for mol in molDB.molecules:
            atomic_numbers = np.array([atom.atomic_number for atom in mol.atoms])
            xyz_coordinates = torch.tensor(np.array(mol.xyz_coordinates).astype('float')).to(self.device).requires_grad_(calculate_energy_gradients or calculate_hessian)
            xyz_coordinates = xyz_coordinates.unsqueeze(0)
            species = species_to_tensor(atomic_numbers).to(self.device).unsqueeze(0)
            ANI_NN_energy = self.model((species, xyz_coordinates)).energies
            
            if calculate_energy: mol.energy = float(ANI_NN_energy)
            if calculate_energy_gradients or calculate_hessian:
                ANI_NN_energy_gradients = torch.autograd.grad(ANI_NN_energy.sum(), xyz_coordinates, create_graph=True, retain_graph=True)[0]
                if calculate_energy_gradients:
                    grads = ANI_NN_energy_gradients[0].detach().cpu().numpy()
                    for iatom in range(len(mol.atoms)):
                        mol.atoms[iatom].energy_gradients = grads[iatom]
            if calculate_hessian:
                ANI_NN_hessian = torchani.utils.hessian(xyz_coordinates, energies=ANI_NN_energy).cpu()
                mol.hessian = np.array(ANI_NN_hessian[0])

class atomic_energy_shift():
    atomic_energy_shifts = {'AIQM1': 
                            {1: -4.29365862e-02, 6: -3.34329586e+01, 7: -4.69301173e+01, 8: -6.29634763e+01},

                            'AIQM1@DFT': 
                            {1: -4.27888067e-02, 6: -3.34869833e+01, 7: -4.69896148e+01, 8: -6.30294433e+01},

                            # 'AIQM1u.wb97xdef2tzvpp_8aninnstar_d4wb97x_shift_20230220':
                            # {1: 5.24074584e-05, 6: 5.39532225e-02, 7: 5.89913655e-02, 8: 6.55949035e-02},

                            # 'AIQM0u.8aninnstar_d4wb97x_shift_20230220':
                            # {1: -0.60023595, 6: -38.03692936, 7: -54.67357136, 8: -75.1619857},

                            # 'AIQM1u.wb97x631Gd_8aninnstar_d4wb97x_shift_20230407':
                            # {1: -0.00299102, 6: 0.04430595, 7: 0.03768013, 8: 0.02923053}
                            }
    atomic_energy_shifts['AIQM1u.odm2star_8aninnstar_d4wb97x_shift_20210720'] = atomic_energy_shifts['AIQM1']
    atomic_energy_shifts['AIQM1@DFT*'] = atomic_energy_shifts['AIQM1@DFT']
    
    def __init__(self, **kwargs):
        
        if 'sae' in kwargs:
            self.sae = kwargs['sae']       
                
    def predict(self, molecular_database=None, molecule=None,
                calculate_energy=True, calculate_energy_gradients=False, calculate_hessian=False):
        if molecular_database != None:
            molDB = molecular_database
        elif molecule != None:
            molDB = data.molecular_database()
            molDB.molecules.append(molecule)
        else:
            errmsg = 'Either molecule or molecular_database should be provided in input'
            raise ValueError(errmsg)
         
        for mol in molDB.molecules:
            if calculate_energy:
                ee = 0.0
                for atom in mol.atoms:
                    ee += self.sae[atom.atomic_number]
                mol.energy = ee
            if calculate_energy_gradients:
                for atom in mol.atoms:
                    atom.energy_gradients = np.zeros(3)
            if calculate_hessian:
                ndim = len(mol.atoms) * 3
                mol.hessian = np.zeros(ndim*ndim).reshape(ndim,ndim)
        






