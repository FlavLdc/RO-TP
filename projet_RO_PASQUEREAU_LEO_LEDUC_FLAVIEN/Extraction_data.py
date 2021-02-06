#! /bin/env python3.8
# -- coding=utf-8 --
from pathlib import Path
import networkx as nx
import random 
def extract_data(file_to_open):

    graph = nx.DiGraph()
    with open(file_to_open,'r') as f_in:
        #Extraction des données de l'en-tête
        entete = f_in.readline()
        p = entete.split()[0] # Limite du camion
        start =entete.split()[1] #Depot de départ
        n_clientsuppr = entete.split()[2]#Nb de clients à ne pas servir
        n_depsuppr =entete.split()[3]# Nb de depots HS
        #Extraction des données des blocs
        bloc = ''
        for line in f_in:
            line_split = line.split()
            if bloc =='':
                bloc = line_split[0]
            elif line_split[0]=='}':
                bloc =''
            elif bloc == 'ENTITIES':
                a = line_split[0]
                b = line_split[1]
                c = line_split[2]
                graph.add_nodes_from([(a,{"demande" :c})])
                
            elif bloc =='ROADS':
                d = line_split[0]
                e = line_split[1]
                f = line_split[2]
                g = line_split[3]
                h = line_split[4]

                #graph.add_node(e)
                graph.add_edge(d,e,capacity=f, length =g)
            else:
                exit(f'ERROR: line = {line}')
        if(n_clientsuppr == 1):
            rdm = random.choice(['C1','C2'])
            graph.remove_node(rdm)
    return graph


if __name__ == '__main__':
    a = random.choice(['a','b'])

    print(a)
