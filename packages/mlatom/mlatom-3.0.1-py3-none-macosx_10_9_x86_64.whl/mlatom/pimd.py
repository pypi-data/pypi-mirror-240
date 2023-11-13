#!/usr/bin/env python3

import numpy as np
import json
from multiprocessing.pool import ThreadPool as Pool
from . import data
from . import constants
from . import stopper
from .thermostat import Andersen_thermostat, Nose_Hoover_thermostat, Langevin_thermostat
from .initial_conditions import getridofang
from .environment_variables import env

class pimd():
    Andersen_thermostat = Andersen_thermostat 
    Nose_Hoover_thermostat = Nose_Hoover_thermostat
    Langevin_thermostat = Langevin_thermostat
    def __init__(self, **kwargs):
        if 'model' in kwargs:
            self.model = kwargs['model']
        elif 'method' in kwargs:
            self.model = kwargs['method']
        if 'replicas_with_initial_conditions' in kwargs:
            self.init_replicas = kwargs['replicas_with_initial_conditions']
        if 'ensemble' in kwargs:
            self.ensemble = kwargs['ensemble']
        else:
            self.ensemble = 'NVE'
        if 'temperature' in kwargs:
            self.temperature = kwargs['temperature']
        
        if 'thermostats' in kwargs:
            self.thermostats = kwargs['thermostats']
        if 'time_step' in kwargs:
            self.time_step = kwargs['time_step']
        if 'maximum_propagation_time' in kwargs:
            self.maximum_propagation_time = kwargs['maximum_propagation_time']
        if 'number_of_processes' in kwargs:
            self.number_of_processes = kwargs['number_of_processes']
        else:
            self.number_of_processes = 1

        self.Natoms = len(self.init_replicas.molecules[0].atoms)
        self.Nreplicas = len(self.init_replicas.molecules)
        self.masses = self.init_replicas.molecules[0].get_nuclear_masses() 
        self.mass = self.masses.reshape(self.Natoms,1)
        self.omega_n = self.Nreplicas*constants.kB * self.temperature*2.0*np.pi/(constants.planck_constant*1.0E15)  # Unit: fs^-1

        if self.ensemble.upper() == 'NVE':
            self.propagation_algorithm = nve() 
        elif self.ensemble.upper() == 'NVT':
            self.propagation_algorithm = self.thermostats 
        self.propagate() 

    def propagate(self, **kwargs):
        self.molecular_trajectory = data.molecular_trajectory_pimd()

        istep = 0 
        while istep * self.time_step <= self.maximum_propagation_time:
            print(f"DEBUG: Step {istep}")
            trajectory_step = data.molecular_trajectory_step()
            if istep == 0:
                replicas = self.init_replicas.copy(atomic_labels=['xyz_coordinates','xyz_velocities'],molecular_labels=[])
                self.calculate_forces(moldb=replicas)
                # nthreads = env.get_nthreads()
                # if self.number_of_processes == 1:
                #     self.model.predict(molecular_database=replicas,calculate_energy=True,calculate_energy_gradients=True)
                # else:
                #     env.set_nthreads(1)
                #     pool = Pool(processes=self.number_of_processes)
                #     pool.map(self.run_prediction,replicas.molecules)
                #     env.set_nthreads(nthreads)
                forces = -np.array([each_replica.get_energy_gradients() for each_replica in replicas.molecules])
                accelerations = forces / self.mass / constants.ram2au * (constants.Bohr2Angstrom**2) * (100.0/2.4188432)**2 #/ MLenergyUnits
            else:
                previous_replicas = replicas 
                replicas = self.init_replicas.copy(atomic_labels=['xyz_coordinates','xyz_velocities'],molecular_labels=[])
                for ireplica in range(self.Nreplicas):
                    # Copy XYZ coordinates
                    replicas.molecules[ireplica].xyz_coordinates = previous_replicas.molecules[ireplica].xyz_coordinates
                    # Copy XYZ velocities
                    replicas.molecules[ireplica].update_xyz_vectorial_properties('xyz_velocities',previous_replicas.molecules[ireplica].get_xyz_vectorial_properties('xyz_velocities'))
                
                # Thermostat step
                self.thermostat_step(replicas)
                # for ireplica in range(self.Nreplicas):
                #     self.propagation_algorithm[ireplica].update_velocities_first_half_step(molecule=replicas.molecules[ireplica],time_step = self.time_step)

                coords = np.array([each_molecule.xyz_coordinates for each_molecule in replicas.molecules])
                velocities = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas.molecules])

                # Velocities update half step 
                velocities = velocities + accelerations * self.time_step * 0.5

                # Coordinates update
                #coords = coords + velocities * self.time_step + accelerations * self.time_step**2 * 0.5

                momenta = velocities * self.mass * constants.ram2au
                P_nm = np.zeros((self.Nreplicas,self.Natoms,3))
                Q_nm = np.zeros((self.Nreplicas,self.Natoms,3))
                for kk in range(self.Nreplicas):
                    for iatom in range(self.Natoms):
                        for jj in range(self.Nreplicas):
                            P_nm[kk][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * momenta[jj][iatom]
                            Q_nm[kk][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * coords[jj][iatom]
                # for iatom in range(self.Natoms):
                #     Q_nm[0][iatom] += P_nm[0][iatom] / self.masses[iatom] / constants.ram2au * self.time_step
                for kk in range(self.Nreplicas):
                    for iatom in range(self.Natoms):
                        if kk!=0:
                            omega_k = 2*self.omega_n*np.sin(kk*np.pi/self.Nreplicas)
                            p_ = P_nm[kk][iatom]*np.cos(omega_k*self.time_step)-Q_nm[kk][iatom]*self.masses[iatom]*constants.ram2au*omega_k*np.sin(omega_k*self.time_step)
                            q_ = P_nm[kk][iatom]*np.sin(omega_k*self.time_step)/(self.masses[iatom]*constants.ram2au*omega_k)+Q_nm[kk][iatom]*np.cos(omega_k*self.time_step)
                            P_nm[kk][iatom] = p_ 
                            Q_nm[kk][iatom] = q_
                        else:
                            Q_nm[kk][iatom] += P_nm[kk][iatom] * self.time_step
                momenta = np.zeros((self.Nreplicas,self.Natoms,3))
                coords = np.zeros((self.Nreplicas,self.Natoms,3))
                for jj in range(self.Nreplicas):
                    for iatom in range(self.Natoms):
                        for kk in range(self.Nreplicas):
                            momenta[jj][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * P_nm[kk][iatom]
                            coords[jj][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * Q_nm[kk][iatom]
                velocities = momenta / self.mass / constants.ram2au

                

                # Calculate forces 
                for ireplica in range(self.Nreplicas):
                    replicas.molecules[ireplica].xyz_coordinates = coords[ireplica]
                self.calculate_forces(moldb=replicas)
                # nthreads = env.get_nthreads()
                # if self.number_of_processes == 1:
                #     self.model.predict(molecular_database=replicas,calculate_energy=True,calculate_energy_gradients=True)
                # else:
                #     env.set_nthreads(1)
                #     pool = Pool(processes=self.number_of_processes)
                #     pool.map(self.run_prediction,replicas.molecules)
                #     env.set_nthreads(nthreads)
                forces = -np.array([each_replica.get_energy_gradients() for each_replica in replicas.molecules])
                accelerations = forces / self.mass / constants.ram2au * (constants.Bohr2Angstrom**2) * (100.0/2.4188432)**2 #/ MLenergyUnits

                # Velocities update half step
                velocities = velocities + accelerations * self.time_step * 0.5

                for ireplica in range(self.Nreplicas):
                    replicas.molecules[ireplica].update_xyz_vectorial_properties('xyz_velocities',velocities[ireplica])

                # Thermostat step
                self.thermostat_step(replicas)
                # for ireplica in range(self.Nreplicas):
                #     self.propagation_algorithm[ireplica].update_velocities_first_half_step(molecule=replicas.molecules[ireplica],time_step = self.time_step)

                # Eliminate linear and angular momentum
                remove_momentum(replicas)

            velocities = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas.molecules])
            kinetic_energies = [np.sum(each**2*self.mass) / 2.0 * 1822.888515* (0.024188432 / constants.Bohr2Angstrom)**2 for each in velocities]
            for ireplica in range(self.Nreplicas):
                replicas.molecules[ireplica].kinetic_energy = kinetic_energies[ireplica]
                replicas.molecules[ireplica].total_energy = kinetic_energies[ireplica] + replicas.molecules[ireplica].energy
            trajectory_step.step = istep 
            trajectory_step.time = istep * self.time_step 
            trajectory_step.molecular_database = replicas 
            self.molecular_trajectory.steps.append(trajectory_step)
            #print(istep)
            istep += 1

            coords = np.array([each_molecule.xyz_coordinates for each_molecule in replicas.molecules])
            #print(coords)
            velocities = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas.molecules])
            #print(coords[0])
            #print(np.sum(coords,axis=0)/len(coords))
            avg_v = np.sum(velocities,axis=0) / len(velocities)
            kinetic_energy = np.sum(avg_v**2 * self.mass) / 2.0 * 1822.888515 * (0.024188432 / constants.Bohr2Angstrom)**2
            print(kinetic_energy*2/(3*len(coords[0])-6)/(constants.kB_in_Hartree)) 

    def run_prediction(self,mol):
        self.model.predict(molecule=mol,calculate_energy=True,calculate_energy_gradients=True)

    def calculate_forces(self,moldb):
        nthreads = env.get_nthreads()
        if self.number_of_processes == 1:
            self.model.predict(molecular_database=moldb,calculate_energy=True,calculate_energy_gradients=True)
        else:
            env.set_nthreads(1)
            pool = Pool(processes=self.number_of_processes)
            pool.map(self.run_prediction,moldb.molecules)
            env.set_nthreads(nthreads)

    def thermostat_step(self,replicas):
        replicas_temp = replicas.copy()
        velocities = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas.molecules])
        momenta = velocities * self.mass * constants.ram2au
        P_nm = np.zeros((self.Nreplicas,self.Natoms,3))
        for kk in range(self.Nreplicas):
            for iatom in range(self.Natoms):
                for jj in range(self.Nreplicas):
                    P_nm[kk][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * momenta[jj][iatom]
        velocities_temp = P_nm / self.mass / constants.ram2au 
        for ireplica in range(self.Nreplicas):
            replicas_temp.molecules[ireplica].update_xyz_vectorial_properties('xyz_velocities',velocities_temp[ireplica])
        for ireplica in range(self.Nreplicas):
            self.propagation_algorithm[ireplica].update_velocities_first_half_step(molecule=replicas_temp.molecules[ireplica],time_step = self.time_step)
        velocities_temp = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas_temp.molecules])
        P_nm = velocities_temp * self.mass * constants.ram2au

        momenta = np.zeros((self.Nreplicas,self.Natoms,3))
        for jj in range(self.Nreplicas):
            for iatom in range(self.Natoms):
                for kk in range(self.Nreplicas):
                    momenta[jj][iatom] += Cfunction(jj+1,kk,self.Nreplicas) * P_nm[kk][iatom]
        velocities = momenta / self.mass / constants.ram2au
        for ireplica in range(self.Nreplicas):
            replicas.molecules[ireplica].update_xyz_vectorial_properties('xyz_velocities',velocities[ireplica])


class nve():
    def __init__(self):
        pass 

    def update_velocities_first_half_step(self,**kwargs):
        if 'molecule' in kwargs:
            molecule = kwargs['molecule']
        return molecule

    def update_velocities_second_half_step(self,**kwargs):
        if 'molecule' in kwargs:
            molecule = kwargs['molecule']
        return molecule

def Cfunction(j,k,n):
    if k==0:
        return np.sqrt(1/n)
    elif 1<=k and k<=n//2-1:
        return np.sqrt(2/n)*np.cos(2*np.pi*j*k/n)
    elif k == n//2:
        return np.sqrt(1/n)*(-1)**j 
    elif n//2+1 <= k and k<=n-1:
        return np.sqrt(2/n)*np.sin(2*np.pi*j*k/n)

def remove_momentum(replicas):
    Nreplicas = len(replicas.molecules)
    xyzs = np.array([each_molecule.xyz_coordinates for each_molecule in replicas.molecules])
    vxyzs = np.array([each_molecule.get_xyz_vectorial_properties('xyz_velocities') for each_molecule in replicas.molecules])
    avg_xyz = np.sum(xyzs,axis=0)/Nreplicas 
    avg_vxyz = np.sum(vxyzs,axis=0)/Nreplicas
    mass = replicas.molecules[0].get_nuclear_masses()
    masses = mass.reshape(len(mass),1)

    # Remove angular momentum 
    new_avg_vxyz = getridofang(np.copy(avg_xyz),np.copy(avg_vxyz),mass)
    correction = new_avg_vxyz - avg_vxyz
    vxyzs = vxyzs + correction

    # Remove linear momentum
    v_cm = sum(new_avg_vxyz*masses)/np.sum(mass)
    vxyzs = vxyzs - v_cm 

    # Update velocities
    for ireplica in range(Nreplicas):
        replicas.molecules[ireplica].update_xyz_vectorial_properties('xyz_velocities',vxyzs[ireplica])

