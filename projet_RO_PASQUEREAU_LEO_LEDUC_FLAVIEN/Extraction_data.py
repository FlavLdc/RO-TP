#! /bin/env python3.8
# -*- coding=utf-8 -*-
from pathlib import Path
import networkx as nx
def extract_data(file_to_open):

    graph = nx.DiGraph()
    with open(file_to_open,'r') as f_in:
        #Extraction des données de l'en-tête
        entete = f_in.readline()
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
                graph.add_nodes_from([(a,{"stock" :c})])
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
    return graph
