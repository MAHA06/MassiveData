# Graph:	G_C Graph of the pages using FORMULA
# Structure:	Maximal Clique
import pandas as pd
import os
import networkx as nx
import re
import operator
import pickle
import numpy as np

def get_formula(str):#extract the formula from the json object
    if "formula" in str["results"][0][0]:
        return str["results"][0][0]['formula'][0]
    else:
        return ""

def addEdges(source,str):#search for the references and add them as edges to our graph
    formula=get_formula(str)
    x = re.findall("A[0-9]{6}", formula)
    for edge in x:
        G.add_edge(source,edge)

def load_data(base_dir):
    data_list = {}
    for file in os.listdir(base_dir):

        # If file is a json, construct it's full path and open it, append all json data to list
        if 'json' in file:
            filenameWithoutExtension=os.path.splitext(file)[0]
            json_path = os.path.join(base_dir, file)
            json_data = pd.read_json(json_path, lines=True)
            data_list[filenameWithoutExtension]=json_data
            addEdges(filenameWithoutExtension,json_data)
    print(data_list)

def BronKerbosch(Graph,P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch(Graph,
            P=P.intersection(Graph.neighbors(v)), R=R.union([v]), X=X.intersection(Graph.neighbors(v)))
        X.add(v)

def save_graph(filename,obj):##save the graph object to disk to  skip further trainings
    outfile = open(filename, 'wb')
    pickle.dump(obj, outfile)
    outfile.close()

def load_obj(filename):## load the graph object from persistent storage
    infile = open(filename, 'rb')
    obj = pickle.load(infile)
    infile.close()
    return obj

#############
def Algorithm1(Gr):#display only 1 maximal clique
    P = list(Gr.nodes)
    r = list(BronKerbosch(Gr, P))
    print("A maximal clique is ")
    print(r[0])

def Algorithm2(Gr):#display all the maximal cliques
    P = list(Gr.nodes)
    r = list(BronKerbosch(Gr, P))
    print("All the solutions are")
    print(r)

def Algorithm3(Gr):#display the maximum clique
    P = list(Gr.nodes)
    r = list(BronKerbosch(Gr, P))
    maxVal=max(map(len,r))
    arg=np.argmax(list(map(len,r)))
    if(maxVal>2):
        print("The maximim solution is ", r[arg]," with a length of ", maxVal)
    else:
        print('No solution with minimum 3 elements was found')
if __name__ == "__main__":
    ########### CHANGE HERE IF RUN FOR THE FIRST TIME
    train=False
    if train:#this branch creates the graph object from the start
        G = nx.Graph()
        base_dir = "./sequences/sequences/" #change this to point to our folder of sequences
        load_data(base_dir)
        save_graph("graph.out",G)
    else:#here we just load the pretrained graph
        G=load_obj("graph.out")
    Algorithm1(G)
    Algorithm2(G)
    Algorithm3(G)

