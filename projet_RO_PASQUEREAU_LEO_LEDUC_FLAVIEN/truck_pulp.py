#! /bin/env python3.8
# -*- coding=utf-8 -*-

"""TODO: DESCRIPTION."""
from pathlib import Path
import pulp as pl
import networkx as nx
from Extraction_data import extract_data


# ============================================================================ #
#                                  SET MODEL                                   #
# ============================================================================ #
def set_benef_max(graph, source, p):
    """Set the max benef possible from a graph"""
    # ------------------------------------------------------------------------ #
    # Linear problem with maximization
    # ------------------------------------------------------------------------ #
<<<<<<< HEAD
    prob = pl.LpProblem(name='Maximisation_du_benefice', sense=pl.LpMaximize)
=======
    prob = pl.LpProblem(name='max_benef', sense=pl.LpMaximize)
>>>>>>> e8ce1cab008a442921f80103347842ab6bfe3ad2

    # ------------------------------------------------------------------------ #
    # The variables
    # ------------------------------------------------------------------------ #
<<<<<<< HEAD
    Points = graph.nodes() #dictionnaire ['D1','D2',...]
    Routes = graph.edges() #dictionnaire [('D1','D2'),('D1','D3'),...]
    Depart = source
    Arrivee = source
    p_camion = p

    Essence = nx.get_edge_attributes(graph,'Essence') #list {('D1', 'D2'): 20, ('D1', 'D3'): 20,...}
    Capacity = nx.get_edge_attributes(graph, 'Capacity') #list {('D1', 'D2'): 10, ('D1', 'D3'): 10,...}
    Douane = nx.get_edge_attributes(graph, 'Douane') #list {('D1', 'D2'): 30, ('D1', 'D3'): 30,...}
    Demande_clients = nx.get_node_attributes(graph, 'Demande') #list {'C1': 8, 'C2': 10}
    Stock_depots = nx.get_node_attributes(graph, 'Stock') #list {'D1': -10, 'D2': -3, 'D3': -5}
    
    Camion = pl.LpVariable.dicts('Gpu_Camion', Routes, lowBound=0, cat=pl.LpInteger)
    Livraison = pl.LpVariable.dicts('Livraison', Points, lowBound=0, cat=pl.LpInteger)
    Quantite_depot = pl.LpVariable.dicts('Quantite', Points, upBound=0, cat=pl.LpInteger)

    #big_M = graph.number_of_edges()

    d_passage_e = {}  # a dictionnary of LpVariable which means: is e in path?
    for (u,v) in Routes:
        # Add the edges binaries
        d_passage_e[(u, v)] = pl.LpVariable(f'passage_{u}_{v}', cat=pl.LpBinary)
=======
    
>>>>>>> e8ce1cab008a442921f80103347842ab6bfe3ad2

    # ------------------------------------------------------------------------ #
    # The objective function
    # ------------------------------------------------------------------------ #
    # TODO: write the objective function
    prob += pl.lpSum([1000 * pl.lpSum(Demande_clients)]) - pl.lpSum([(Essence[e] + Douane[e] * Camion[e]) for e in Routes])
    # ------------------------------------------------------------------------ #
    # The constraints
    # ------------------------------------------------------------------------ #
    # TODO: write constraints
    # C1: capacity is the transport limit for each edge
    for e in Routes:
        prob += Camion[e] <= Routes[e]['Capacity'], f'capacity_limit_{e}'
        prob += Camion[e] <= p_camion

    #C2 : On doit commencer a la source et finir a la source
    
    # On ne peut passer qu'1 fois sur un chemin 
    for point in Points:
        if point == source:
            prob += pl.lpSum(d_passage_e[(u,v)] for u, v in Routes if u == point) == 1
            prob += pl.lpSum(d_passage_e[(t,u)] for u, t in Routes if u == point) == 1
        #else:
            #prob += pl.lpSum(Transport_Camion[u,v] for v, u in Routes if v == point) - \
             #       pl.lpSum(Transport_Camion[v,w] for w, v in Routes if v == point) == Demande_clients[point]
    print(Stock_depots)
    
    for e in Routes:
        prob += d_passage_e[e] <= 1, f'{e}_max_one_time_in_path'
        
        for (u,v) in e:
            if u == source:
                prob += pl.lpSum(d_passage_e[(u,v)] for u, v in Routes) == 1
            elif v == source:
                prob += pl.lpSum(d_passage_e[(u,v)] for u, v in Routes) == 1
            
    return prob

# ============================================================================ #
#                               SOLVE WITH DATA                                #
# ============================================================================ #

def solve_truck_problem(file_path):
    """TODO: Description."""
    # ------------------------------------------------------------------------ #
    # Set data
    # ------------------------------------------------------------------------ #
    # TODO: set data
    graph, source, p = extract_data(file_path)

    # ------------------------------------------------------------------------ #
    # Solve the problem using the model
    # ------------------------------------------------------------------------ #
    prob = set_benef_max(graph,source,p)
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

    print("benefice max : ", pl.value(prob.objective) )


if __name__ == '__main__':

    data_folder = Path("./data")

    file_to_open = data_folder/"truck_instance_base.data"

    graph = extract_data(file_to_open)
    solve_truck_problem(file_to_open)
    #print(nx.get_node_attributes(graph,'Demande'))
    #nx.write_graphml(graph,'test_clientsuppr.graphml')
