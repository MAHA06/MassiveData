# Graph:	G_C Graph of the pages using FORMULA
# Structure:	Maximal Clique
import pandas as pd
import os
import networkx as nx
import re
import operator
import pickle

from itertools import combinations

def get_formula(str):
    if "formula" in str["results"][0][0]:
        return str["results"][0][0]['formula'][0]
    else:
        return ""


def is_clique(b,T):
    # Run a loop for all set of edges
    for i in range(1, b):
        for j in range(i + 1, b):

            # If any edge is missing
            if (not T.has_edge([store[i]],[store[j]])):
                return False;

    return True;


# Function to find all the sizes
# of maximal cliques
store={}
def maxCliques(i, l,T):
    # Maximal clique size
    max_ = 0;

    # Check if any vertices from i+1
    # can be inserted
    for j in range(i + 1, n + 1):

        # Add the vertex to store
        store[l] = j;

        # If the graph is not a clique of size k then
        # it cannot be a clique by adding another edge
        if (is_clique(l + 1,T)):
            # Update max
            max_ = max(max_, l);

            # Check if another edge can be added
            max_ = max(max_, maxCliques(j, l + 1));

    return max_;
def addEdges(source,str):
    formula=get_formula(str)
    x = re.findall("A[0-9]{6}", formula)
    for edge in x:
        G.add_edge(source,edge)
def load_data(base_dir):
    # base_dir = '/Users/thijseekelaar/Downloads/airlines_complete'

    # Get all files in the directory

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
def save_graph(filename,obj):
    outfile = open(filename, 'wb')
    pickle.dump(obj, outfile)
    outfile.close()
def load_obj(filename):
    infile = open(filename, 'rb')
    obj = pickle.load(infile)
    infile.close()
    return obj
# Press the green button in the gutter to run the script.
G = nx.Graph()


base_dir = "./sequences/sequences/"
load_data(base_dir)
save_graph("graph.out",G)
popular_nodes=sorted(dict(G.degree()).items(),key=operator.itemgetter(1))
T=G
n=G.number_of_nodes()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
