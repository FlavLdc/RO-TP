#! /bin/env python3.8
# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""
from pathlib import Path
import pulp as pl

data_folder = Path("RO TP/data/")

file_to_open = data_folder / "truck_instance_base.data"

f = open(file_to_open)

print (f.read())

# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #


def solve_truck_problem(file_path):
# Faire quelque chose ici avec l'argument `file_path`
# qui est un chemin de fichier
# ...
# La fonction retournera :
# - la valeur de la fonction objectif égale aux bénéfices
# de l'entreprise si le problème est resolvable,
# sinon `None`. Le type de retour sera un "float" ;
# - un dictionnaire,
# où les clefs sont les routes et les valeurs associées
# sont les quantités de marchandises qui les traversent ;
# - ce que vous voulez en plus si besoin.
return optval, roads_qty #, ...


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

    solve_something()
