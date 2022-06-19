import os
from plot_utils.grid import Grid
from plot_utils.utils import get_stored_structure, store_plot_data
from plot_utils.features import compute_actuation, compute_emptiness
from utils.algo_utils import Structure, get_percent_survival_evals
import numpy as np
import math


if __name__ == '__main__':

    for i in range(1, 7):

        exp_name = 'ga_carrier_' + str(i)
        pop_size = 100
        max_evaluations = 2000
        print("Storing data of exp", exp_name)

        activity_grid = Grid()
        performances_grid = Grid(default=-50)
        activity_after_eval = {}
        best_after_eval = {}

        exp_path =  os.path.join('saved_data', exp_name)

        print()
        num_evaluations = 0
        num_survivors = 0

        for gen_number in range(30):
            gen_path = os.path.join(exp_path, "generation_" + str(gen_number))
            gen_data = {}

            # get generation stored fitness values
            output_path = os.path.join(gen_path, "output.txt")
            f = open(output_path, "r")
            for line in f:
                gen_data[int(line.split()[0])] = float(line.split()[1])

            for ind in range(pop_size):
                num_evaluations += 1
                try:
                    structure_path = os.path.join( gen_path, 'structure', str(ind) + '.npz' ) 
                    body, conn = get_stored_structure(structure_path)
                except:
                    continue
                structure = Structure(body=body, connections=conn, label=ind)

                # get ind fitness
                fitness = gen_data[ind]

                # compute ind features
                actuation, v, h = compute_actuation(structure)
                emptiness = compute_emptiness(structure)

                # update grids
                pos = performances_grid.get_pos(actuation, emptiness)
                if fitness > performances_grid.grid[pos]:  # update grid values
                    performances_grid.insert(fitness, pos[0], pos[1])
                    activity_grid.increment(pos[0], pos[1])

            # clean evaluations counter from survivors	
            num_evaluations = min(num_evaluations - num_survivors, max_evaluations)
            percent_survival = get_percent_survival_evals(num_evaluations, max_evaluations)
            num_survivors = max(2, math.ceil(pop_size * percent_survival))

            # track evaluations results
            best_after_eval[num_evaluations] = np.max(performances_grid.grid)
            activity_after_eval[num_evaluations] = len(np.nonzero(activity_grid.grid)[0])
                
        # clean performance grid border values
        for i in range(len(performances_grid.grid)):
            for j in range(len(performances_grid.grid[i])):
                if performances_grid.grid[(i, j)] == -50:
                    performances_grid.insert(None, i, j)

        # store plot data
        plot_path = os.path.join('saved_data', exp_name, 'plots')
        store_plot_data((np.array(list(activity_after_eval.keys())), np.array(list(activity_after_eval.values()))), plot_path, 'activityTrend')
        store_plot_data((np.array(list(best_after_eval.keys())), np.array(list(best_after_eval.values()))), plot_path, 'fitnessTrend')
        store_plot_data(activity_grid.grid, plot_path, 'activityGrid')
        store_plot_data(performances_grid.grid, plot_path, 'performancesGrid')

        print("Plot data stored at", plot_path)