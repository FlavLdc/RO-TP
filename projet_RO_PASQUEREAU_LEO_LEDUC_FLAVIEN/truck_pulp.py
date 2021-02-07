#! /bin/env python3.8
# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""
from pathlib import Path
import pulp as pl
import networkx as nx
from Extraction_data import extract_data

data_folder = Path("./data")

file_to_open = data_folder/"truck_instance_less_customers.data"

f = open(file_to_open)

# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_model_name():
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
    prob = pl.LpProblem(name='max_benef', sense=pl.LpMaximize)

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
    

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # TODO: write the objective function

    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # TODO: write constraints

    return prob

# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #

def solve_something():
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # TODO: set data

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob = set_model_name()
    # Coin Branch and Cut solver is used to solve the instanced model
    # TODO: change the log path file
    prob.solve(pl.PULP_CBC_CMD(logPath='./log_path_file.log'))

    # ------------------------------------------------------------------------ #
    # Print the solver output
    # ------------------------------------------------------------------------ #
    print(f'Status:\n{pl.LpStatus[prob.status]}')

    print()
    print('-' * 40)
    print()

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        print(v.name, '=', v.varValue)


if __name__ == '__main__':
    graph =extract_data(file_to_open)
    nx.write_graphml(graph,'test_clientsuppr.graphml')
