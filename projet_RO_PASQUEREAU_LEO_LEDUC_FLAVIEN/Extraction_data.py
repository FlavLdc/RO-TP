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
        p = int(entete.split()[0]) # Limite du camion
        start =entete.split()[1] #Depot de départ
        n_clientsuppr = int(entete.split()[2])#Nb de clients à ne pas servir
        n_depsuppr = int(entete.split()[3])# Nb de depots HS
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
                c = int(line_split[2])
                if(b == 'depot'):
                    graph.add_node(a, Stock = c)
                else:                   
                    graph.add_node(a, Demande = c)     
            elif bloc =='ROADS':
                d = line_split[0]
                e = line_split[1]
                f = int(line_split[2])
                g = int(line_split[3])
                h = int(line_split[4])
                graph.add_edge(d, e, Capacity=f, Essence=g, Douane=h)
            else:
                exit(f'ERROR: line = {line}')
        if(n_clientsuppr == 1):
            rdm = random.choice(['C1','C2'])
            graph.remove_node(rdm)
        elif(n_clientsuppr == 2):
            graph.remove_node('C1')
            graph.remove_node('C2')
        if(n_depsuppr == 1):
            rdm = random.choice(['D1','D2','D3'])
            graph.remove_node(rdm)
        elif(n_depsuppr == 2):
            depot = ['D1','D2','D3']
            rdm = random.choice(depot)
            depot.remove(rdm)
            rdm2 = random.choice(depot)
            graph.remove_node(rdm)          
            graph.remove_node(rdm2)
        elif(n_depsuppr == 3):
            graph.remove_node('D1')
            graph.remove_node('D2')
            graph.remove_node('D3')
    return graph, start, p

