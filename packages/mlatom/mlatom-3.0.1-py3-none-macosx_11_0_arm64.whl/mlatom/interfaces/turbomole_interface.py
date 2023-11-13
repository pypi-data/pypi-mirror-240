#!/usr/bin/env python3
'''
  !---------------------------------------------------------------------------! 
  ! Turbomole: interface to the Turbomole program package                     ! 
  ! Implementations by: Sebastian V. Pios                                     !
  !---------------------------------------------------------------------------! 
'''

import os
import numpy as np
import tempfile
import subprocess
import re
import time
import shutil
#pythonpackage = True
from .. import constants, data, stopper
from . import file_utils

class turbomole_methods():
    
    turbomole_keywords = {
            'method'     : 'ricc2', #rimp2, ricc2, escf...
            'cores'      : 2,       #number of parnodes
            }
    def __init__(self, save_files_in_current_directory=True, directory_with_input_files=None, **kwargs):
        #self.turbomole_task = turbomole_keywords['method']
        self.save_files_in_current_directory = save_files_in_current_directory
        self.directory_with_input_files = directory_with_input_files
        try:
            self.progbin = os.environ['TURBODIR'] 
        except:
            msg = 'Cannot find the TURBOMOLE program package, please set the environment variable: export TURBODIR=...'
            if pythonpackage: raise ValueError(msg)
            else: stopper.stopMLatom(msg) 
        
    def predict(self,method='ricc2', molecular_database=None, molecule=None, calculate_energy=True, calculate_energy_gradients=False, calculate_hessian=False):
        self.STDOUT = 'turbofile.out'
        self.gs_model = 'mp2'
        self.turbomole_task = method
        if molecular_database != None:
            molDB = molecular_database
        elif molecule != None:
            molDB = data.molecular_database()
            molDB.molecules.append(molecule)
        #else:
        #    errmsg = 'Either molecule or molecular_database should be provided in input'
        #if pythonpackage: raise ValueError(errmsg)
        else: 
            stopper.stopMLatom(errmsg)
        for mol in molDB.molecules:
            with tempfile.TemporaryDirectory() as tmpdirname:
                if self.save_files_in_current_directory:
                    tmpdirname = './test/'
                    if os.path.exists(tmpdirname):
                        os.system('rm -rf %s' % tmpdirname)
                    os.system(f'mkdir {tmpdirname}')
                if self.directory_with_input_files != None:
                    filenames=os.listdir(self.directory_with_input_files)
                    for filename in filenames:
                        shutil.copy2(os.path.join(self.directory_with_input_files, filename), tmpdirname)                  
                xyzfilename = f'{tmpdirname}/coord'
                outfilename = f'{tmpdirname}'+self.STDOUT
                #geo_input = np.loadtxt('qm_geom')
                #file_utils.replace_cols_inplace('coord', geo_input, r'\$coord')
                
                proc = subprocess.Popen(self.turbomole_task+'>'+self.STDOUT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=tmpdirname, universal_newlines=True, shell=True)
                proc.communicate()
                check_turbo = subprocess.run('actual', stdout=subprocess.PIPE, cwd=tmpdirname, shell=True)
                if check_turbo.stdout.startswith(b'fine, '): ### Check if Turbomole had convergence issues
                    # Get energies
                    mol.electronic_state_energies = ricc2_energy(outfilename,self.gs_model)
                    
                    # Get energy gradients
                    temp_key, temp_grad = next(iter(ricc2_gradient(self, fname=outfilename).items()))
                    for atom in mol.atoms:
                        atom.electronic_state_energy_gradients = []
                    self.nstates = len(mol.electronic_state_energies)
                    for istate in range(0, self.nstates):
                        if istate == (temp_key - 1):
                            iatom = -1
                            for i in range(len(temp_grad)):
                                iatom += 1
                                mol.atoms[iatom].electronic_state_energy_gradients.append([float(xx) / constants.Bohr2Angstrom for xx in temp_grad[i]])
                        else:
                            iatom = -1
                            for i in range(len(temp_grad)):  
                                iatom += 1
                                mol.atoms[iatom].electronic_state_energy_gradients.append([np.nan for i in temp_grad[i]])
                    #delete_files_in_directory(f'{tmpdirname}')
                else: 
                    check_turbo = subprocess.run('actual -r', cwd=tmpdirname, shell=True)
                    return

                
                
                # Get nonadiabatic coupling vectors
                #from itertools import combinations
                #state_comb = list(combinations(range(1, nstates+1), 2))
                #for atom in mol.atoms:
                #    atom.nonadiabatic_coupling_vectors = [[np.zeros(3) for ii in range(nstates)] for jj in range(nstates)]
                #for final_state, initial_state in state_comb:
                #    nacpath = f'{tmpdirname}/GRADIENTS/cartgrd.nad.drt1.state{initial_state}.drt1.state{final_state}.sp'
                #    if os.path.exists(nacpath):
                #        with open(nacpath) as ff:
                #            iatom = -1
                #            for line in ff:
                #                iatom += 1
                #                nacvec = np.array([float(xx) / constants.Bohr2Angstrom for xx in line.replace('D','e').split()]).astype(float)
                #                mol.atoms[iatom].nonadiabatic_coupling_vectors[initial_state-1][final_state-1] = nacvec
                #                mol.atoms[iatom].nonadiabatic_coupling_vectors[final_state-1][initial_state-1] = -nacvec
    

def ricc2_gradient(self,fname):
    grads = dict()
    # Try to get ground state gradient.
    try:
        cfile = file_utils.go_to_keyword(fname, "GROUND STATE FIRST-ORDER PROPERTIES")[0]
        grads[1] = get_grad_from_stdout(cfile)
    except ValueError:
        pass
    # Try to get excited state gradients.
    try:
        cfile = file_utils.go_to_keyword(fname, "EXCITED STATE PROPERTIES")[0]
    except ValueError:
        return grads
    while True:
        try:
            line = file_utils.search_file(cfile, 
                    "Excited state reached by transition:", 
                    max_res=1, 
                    close=False, 
                    after=3)
            cstate = int(line[0].split()[4]) + 1
        except ValueError:
            cfile.close()
            break
        try:
            file_utils.search_file(cfile, 
                    "cartesian gradient of the energy",
                    max_res=1,
                    stop_at=r"\+={73}\+",
                    close=False)
            grads[cstate] = get_grad_from_stdout(cfile)
        except ValueError:
            pass
    return grads


def ricc2_energy(fname, model):
    search_string = "Final "+re.escape(model.upper())+" energy"
    gs_energy = file_utils.search_file(fname, search_string)
    file_utils.split_columns(gs_energy, col=5, convert=np.float64)
    ex_energy = file_utils.search_file(fname, "Energy:")
    ex_energy = file_utils.split_columns(ex_energy, 1, convert=np.float64)
    energy = np.repeat(gs_energy, len(ex_energy) + 1)
    energy[1:] = energy[1:] + ex_energy
    return energy

def get_grad_from_stdout(cfile):
    grad = file_utils.search_file(cfile, r"^  ATOM", after=3, stop_at=r"resulting FORCE", close=False)
    grad = [line[5:] for line in grad]
    grad = [' '.join(grad[0::3]), ' '.join(grad[1::3]), ' '.join(grad[2::3])]
    grad = [line.split() for line in grad]
    grad = [list(map(file_utils.fortran_double, vals)) for vals in grad]
    return np.array(grad).T

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")





if __name__ == '__main__':
    pass
