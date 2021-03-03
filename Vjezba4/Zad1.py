
import matplotlib.pyplot as plt
import networkx as nx
import pprint
from collections import defaultdict


def readFromPayek():
    G = nx.read_pajek("euler.net")
    # print(G.edges)
    # print(G.nodes)
    # G1.number_of_nodes()
    # G1.number_of_edges()
    # G.degree[1]  koliko ima brida pojedini vrh
    # list(G.adj[1])  listat susjednih nodova
    # print(G1["A"]) je isto ko i G1.adj("A")
    G1 = nx.Graph(G)
    d = {key: [] for key in G1.nodes}

    for el in G1.nodes:
        for key in G1[el].keys():
            d[el].append(key)

    pprint.pprint(d)


readFromPayek()
