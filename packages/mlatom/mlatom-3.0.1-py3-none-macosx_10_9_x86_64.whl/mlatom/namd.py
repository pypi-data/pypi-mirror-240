#!/usr/bin/env python3
'''
  !---------------------------------------------------------------------------! 
  ! MD: Module for molecular dynamics                                         ! 
  ! Implementations by: Lina Zhang & Pavlo O. Dral                            ! 
  !---------------------------------------------------------------------------! 
'''
import numpy as np
import os
from collections import Counter
from . import data
from . import constants
from .md import md as md
try:
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as mfm
    import matplotlib.colors as mcolors
except:
    pass

class surface_hopping_md():
    def __init__(self, model=None,
                 molecule_with_initial_conditions=None,
                 ensemble='NVE',
                 thermostat=None,
                 time_step=0.1,
                 maximum_propagation_time=100,
                 dump_trajectory_interval=None,
                 filename=None, format='h5md',
                 stop_function=None, stop_function_kwargs=None,
                 hopping_algorithm='Landau-Zener',
                 nstates=None, initial_surface=None,
                 random_seed=1, prevent_back_hop=False, rescale_velocity_direction='along velocities'):
        self.model = model
        self.molecule_with_initial_conditions = molecule_with_initial_conditions
        self.ensemble = ensemble
        if thermostat != None:
            self.thermostat = thermostat
        self.time_step = time_step
        self.maximum_propagation_time = maximum_propagation_time
        
        self.dump_trajectory_interval = dump_trajectory_interval
        if dump_trajectory_interval != None:
            self.format = format
            if format == 'h5md': ext = '.h5'
            elif format == 'json': ext = '.json'
            if filename == None:
                import uuid
                filename = str(uuid.uuid4()) + ext
            self.filename = filename 
        
        self.stop_function = stop_function
        self.stop_function_kwargs = stop_function_kwargs
        
        self.hopping_algorithm=hopping_algorithm
        self.nstates=nstates
        self.initial_surface=initial_surface
        self.random_seed = random_seed
        self.prevent_back_hop = prevent_back_hop
        self.rescale_velocity_direction = rescale_velocity_direction
        
        self.propagate()

    def propagate(self):
        self.molecular_trajectory = data.molecular_trajectory()

        istep = 0
        stop = False
        np.random.seed(self.random_seed)
        self.current_surface = self.initial_surface
        one_step_propagation = True

        while not stop:
            if istep == 0:
                molecule = self.molecule_with_initial_conditions.copy(atomic_labels=['xyz_coordinates','xyz_velocities'], molecular_labels=[])
            else:
                molecule = self.molecular_trajectory.steps[-1].molecule.copy(atomic_labels=['xyz_coordinates','xyz_velocities'], molecular_labels=[])
            if one_step_propagation:
                self.model.current_surface=self.current_surface
                dyn = md(model=self.model,
                        molecule_with_initial_conditions=molecule,
                        ensemble='NVE',
                        thermostat=None,
                        time_step=self.time_step,
                        maximum_propagation_time=self.time_step,
                        dump_trajectory_interval=None,
                        filename=None, format='h5md')
                if istep == 0:
                    self.molecular_trajectory.steps.extend(dyn.molecular_trajectory.steps)
                else:
                    self.molecular_trajectory.steps.append(dyn.molecular_trajectory.steps[-1])
                    self.molecular_trajectory.steps[-1].step = istep + 1
                    self.molecular_trajectory.steps[-1].time = (istep + 1) * self.time_step

            random_number = np.random.random()
            self.molecular_trajectory.steps[istep+1].random_number = random_number
            if istep == 0:
                self.molecular_trajectory.steps[istep].current_surface = self.current_surface
            # fssh/lzsh/znsh: prob list
            if self.hopping_algorithm == 'Landau-Zener':
                prob_all_stat = self.lzsh(istep=istep)
            self.molecular_trajectory.steps[istep+1].prob_all_stat = prob_all_stat
            max_prob = max(prob_all_stat)
            if max_prob > random_number:
                max_prob_stat = prob_all_stat.index(max_prob)
                self.initial_surface = self.current_surface
                self.current_surface = max_prob_stat
                # fssh/lzsh/znsh: rescale_velocity; change en grad in molecular_trajectory; change ekin etot
                hopping_gap = (self.molecular_trajectory.steps[istep+1].molecule.electronic_state_energies[self.current_surface]
                                -self.molecular_trajectory.steps[istep+1].molecule.electronic_state_energies[self.initial_surface])
                if self.rescale_velocity_direction == 'along velocities':
                    self.molecular_trajectory.steps[istep+1].molecule.rescale_velocities(kinetic_energy_change=-hopping_gap)
                self.change_properties_of_hopping_step(step=istep+1) 
                if self.hopping_algorithm == 'Landau-Zener':
                    del self.molecular_trajectory.steps[-1]
                    one_step_propagation = True
            elif self.hopping_algorithm == 'Landau-Zener':
                one_step_propagation = False
            self.molecular_trajectory.steps[istep+1].current_surface = self.current_surface

            istep += 1

            if self.dump_trajectory_interval != None:
                if (istep - 1) == 0:
                    if self.format == 'h5md':
                        temp_traj = data.molecular_trajectory()
                        temp_traj.steps.append(self.molecular_trajectory.steps[0])
                    elif self.format == 'json':
                        temp_traj.steps.append(self.molecular_trajectory.steps[0])
                if istep % self.dump_trajectory_interval == 0:
                    if self.format == 'h5md':
                        if (istep - 1) != 0:
                            temp_traj = data.molecular_trajectory()
                        temp_traj.steps.append(self.molecular_trajectory.steps[istep])
                    elif self.format == 'json':
                        temp_traj.steps.append(self.molecular_trajectory.steps[istep])
                    temp_traj.dump(filename=self.filename, format=self.format)

            if type(self.stop_function) != type(None):
                if self.stop_function_kwargs == None: self.stop_function_kwargs = {}
                stop = self.stop_function(molecule, **self.stop_function_kwargs)
            if istep * self.time_step + 1e-6 > self.maximum_propagation_time:
                stop = True

        if float(f"{self.molecular_trajectory.steps[-1].time:.6f}") > self.maximum_propagation_time:
            del self.molecular_trajectory.steps[-1]
                
    def lzsh(self, istep=None):
        dyn = md(model=self.model,
                molecule_with_initial_conditions=self.molecular_trajectory.steps[-1].molecule.copy(atomic_labels=['xyz_coordinates','xyz_velocities'], molecular_labels=[]),
                ensemble='NVE',
                thermostat=None,
                time_step=self.time_step,
                maximum_propagation_time=self.time_step,
                dump_trajectory_interval=None,
                filename=None, format='h5md')
        self.molecular_trajectory.steps.append(dyn.molecular_trajectory.steps[-1])
        self.molecular_trajectory.steps[-1].step = istep + 2
        self.molecular_trajectory.steps[-1].time = (istep + 2) * self.time_step
        
        prob_all_stat = []
        for stat in range(self.nstates):
            gap_per_stat = []
            if stat == self.current_surface:
                prob = -1.0      
            else:
                for iistep in [istep, istep+1, istep+2]:
                    gap_per_stat.append(abs(self.molecular_trajectory.steps[iistep].molecule.electronic_state_energies[self.current_surface]
                                        -self.molecular_trajectory.steps[iistep].molecule.electronic_state_energies[stat]))
                if (gap_per_stat[0] > gap_per_stat[1]) and (gap_per_stat[2] > gap_per_stat[1]):
                    if not self.prevent_back_hop:
                        if (stat > self.current_surface) and (self.molecular_trajectory.steps[istep+1].molecule.kinetic_energy < gap_per_stat[1]):
                            prob = -1.0
                        else:
                            prob = self.lz_prob(gap_per_stat)
                    else:
                        if stat > self.current_surface:
                            prob = -1.0
                        else:
                            prob = self.lz_prob(gap_per_stat)
                else:
                    prob = -1.0
            prob_all_stat.append(prob)
        return prob_all_stat

    def lz_prob(self, gap_per_stat):
        gap = gap_per_stat[1]
        gap_sotd = ((gap_per_stat[2] + gap_per_stat[0] - 2 * gap) / (self.time_step * constants.fs2au)**2)
        return np.exp((-np.pi/2.0) * np.sqrt(abs(gap)**3 / abs(gap_sotd)))

    def change_properties_of_hopping_step(self, step):
        new_epot = self.molecular_trajectory.steps[step].molecule.electronic_state_energies[self.current_surface]
        self.molecular_trajectory.steps[step].molecule.energy = new_epot
        for atom in self.molecular_trajectory.steps[step].molecule.atoms:
            atom.energy_gradients = atom.electronic_state_energy_gradients[self.current_surface]
        #self.molecular_trajectory.steps[step].molecule.calculate_kinetic_energy()
        new_ekin = self.molecular_trajectory.steps[step].molecule.kinetic_energy
        new_etot = new_epot + new_ekin
        self.molecular_trajectory.steps[step].molecule.total_energy = new_etot
    
def analyze_trajs(trajectories=None, maximum_propagation_time=100.0):
    print('Start analyzing trajectories.') # debug

    traj_status_list = []
    for i in range(len(trajectories)):
        traj_status = {}
        try:
            if float(f"{trajectories[i].steps[-1].time:.6f}") == maximum_propagation_time:
                traj_status['status'] = 1
            else:
                traj_status['status'] = 0
        except:
            traj_status['status'] = 0
        if traj_status:
            try:
                final_time = float(f"{trajectories[i].steps[-1].time:.6f}")
                traj_status.update({"final time": final_time})
            except:
                traj_status.update({"final time": 0.0})
        traj_status_list.append(traj_status)

    print('%d trajectories ends normally.' % sum(1 for traj_status in traj_status_list if traj_status["status"] == 1))
    print('%d trajectories ends abnormally.' % sum(1 for traj_status in traj_status_list if traj_status["status"] == 0))
    for i in range(len(trajectories)):
        print("TRAJ%d ends %s at %.3f fs." % (i+1, ("normally" if traj_status_list[i]["status"] == 1 else "abnormally"), traj_status_list[i]["final time"]))

    print('Finish analyzing trajectories.') # debug
    
def plot_population(trajectories=None, time_step=0.1, max_propagation_time=100.0, nstates=3, filename='population.png', ref_pop_filename='ref_pop.txt'):
    time_list = list(np.arange(0.0, (max_propagation_time*100 + time_step*100)/100, time_step))
    pes_all_timestep = []
    population_all_timestep = []
    population_plot = []

    for i in range(len(time_list)):
        pes_per_timestep = []
        for j in range(len(trajectories)):
            try:
                pes_per_timestep.append(trajectories[j].steps[i].current_surface+1)
            except:
                pes_per_timestep.append(None)
        Count_pes = Counter()
        for pes in pes_per_timestep:
            Count_pes[pes] += 1
        population_all_timestep.append([time_list[i]] + list(map(lambda x: Count_pes[x] / (len(pes_per_timestep) - pes_per_timestep.count(None))
                                                                    if (pes_per_timestep.count(None) != len(pes_per_timestep))
                                                                    else Count_pes[x] / len(pes_per_timestep), range(1, nstates + 1))))
        pes_all_timestep.append(pes_per_timestep)

    for i in range(1, nstates + 1 + 1):
        population_plot.append(
            [population_all_timestep[j][i-1] for j in range(len(population_all_timestep))])

    if os.path.exists(ref_pop_filename):
        ref_population_all_timestep = []
        ref_population_plot = []

        with open('%s' % ref_pop_filename) as f_refpop:
            refpop_data = f_refpop.read().splitlines()
        for line in refpop_data:
            ref_population_all_timestep.append(
                list(map(float, line.split())))

        for i in range(1, nstates + 1 + 1):
            ref_population_plot.append(
                [ref_population_all_timestep[j][i-1] for j in range(len(ref_population_all_timestep))])

    plt.clf()

    plt.xlabel('Time (fs)')
    plt.ylabel('Population')

    plt.xlim([0, max_propagation_time])
    plt.ylim([0.0, 1.0])
    num_major_xticks = int(max_propagation_time / 10) + 1
    plt.xticks(np.linspace(0.0, max_propagation_time, num_major_xticks))
    num_major_yticks = int(1.0 / 0.25) + 1
    plt.yticks(np.linspace(0.0, 1.0, num_major_yticks))

    x = population_plot[0]
    if os.path.exists(ref_pop_filename):
        x_ref = ref_population_plot[0]

    for i in range(1, nstates + 1):
        y = population_plot[i]
        plt.plot(x, y, color=list(mcolors.TABLEAU_COLORS.keys())[
                    i-1], label='S%d' % (i-1))
        if os.path.exists(ref_pop_filename):
            y_ref = ref_population_plot[i]
            plt.plot(x_ref, y_ref, color=list(mcolors.TABLEAU_COLORS.keys())[
                    i-1], label='%s-S%d' % (ref_pop_filename,i-1), linestyle='dashed')
            
    plt.legend(loc='best', frameon=False, prop={'size': 10})

    plt.savefig(filename, bbox_inches='tight', dpi=300)
