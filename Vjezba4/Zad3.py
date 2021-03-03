import networkx as nx
from networkx.classes.function import degree


def brojVrhova():
    G = nx.read_pajek("euler.net")
    G1 = nx.Graph(G)
    print(len(G.nodes))


brojVrhova()


def brojBridova():
    G = nx.read_pajek("euler.net")
    G1 = nx.Graph(G)
    print(len(G.edges))


brojBridova()


def stupanjVrhova():
    G = nx.read_pajek("euler.net")
    G1 = nx.Graph(G)

    for el in G1.nodes:
        print("Vrh {0} ima stupanj:{1}".format(el, G1.degree[el]))


print("\n")
stupanjVrhova()


def maxIncidencija():
    G = nx.read_pajek("euler.net")
    G1 = nx.Graph(G)
    max = 0

    for el in G1.nodes:
        if max < G1.degree(el):
            max = G1.degree(el)

    print(max)
    for el in G1.nodes:
        if(G1.degree(el) == max):
            print("Cvor s max brojem incidentnih vrhova: {0}".format(
                el))


maxIncidencija()
