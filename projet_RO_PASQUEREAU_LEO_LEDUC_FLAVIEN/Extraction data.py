#! /bin/env python3.8
# -*- coding=utf-8 -*-
from pathlib import Path
import networkx as nx

SOURCE = 'S'
TARGET = 'T'

def extract_data(file_path):

    graph = nx.DiGraph()

    graph.add_node(SOURCE)
    graph.add_node(TARGET)

    with open(file_path,'r') as f_in:
        #Extraction des données de l'en-tête
        entete = f_in.readline()
        p = f_in.readline(0,1) #Limite du camion
        start = f_in.readline(3,4) #Dépôt de départ
        n_clientsuppr = f_in.readline(6)# Nombre de clients à ne pas servir
        n_desuppr = f_in.readline(8)# Nombre de dépôts hors service
        #Extraction des données des blocs
        bloc = ''
        for line in f_in:
            line_split = line.split()
            if bloc == 'ENTITIES':
                a,b,c = line_split
                add_entities(graph,a,b,c)
            elif bloc =='ROADS':
                a,b,c,d,e = line_split
                add_roads(graph,a,b,c,d,e)
            else:
                exit(f'ERROR: line = {line}')
    return graph

def add_entities(graph,a):
    #Ajout des dépôts et clients sur le graphe
    a_id = f'R{a}'
    graph.add_node(a_id)

def add_roads(graph,a,b):
    #Ajout des routes entre les dépôts et les clients sur le graphe
    a_id = f'R{a}'
    b_id = f'R{b}'
    graph.add_edge(a_id,b_id)

