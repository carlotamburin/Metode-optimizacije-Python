import bellmanford as bf
from bellmanford.bellmanford import bellman_ford
import networkx as nx
import time
import matplotlib.pyplot as plt


def main():
    # Unos pocetnog grada
    unosGrada = input("Unesite pocetni grad")
    # Niz u kojeg spremamo gradove
    niz = []
    # Citanje u pajek pbliku
    G = nx.read_pajek('airports-split 1.net')
    G1 = nx.DiGraph(G)

    # Citanje iz filea kako bi dobili sve vrhove
    niz = citanjeIzFilea()

    bellmanFord(G1, unosGrada, niz)


# Citanje iz datoteke
def citanjeIzFilea():
    niz = []
    niz2 = []
    f = open('airports-split 1.net', 'r')
    next(f)
    for line in f:
        if "arcs" in line:
            break
        niz.append(line.split())

    for el in niz:
        niz2.append(el[1])
    f.close()
    return niz2


# Bellman ford prolazak za svaki grad
def bellmanFord(g, pocetnigrad, ostaliGradovi):
    start1 = time.time()

    for el in ostaliGradovi:
        if el == pocetnigrad:
            continue
        path_length, path_nodes, negative_cycle = bf.bellman_ford(
            g, pocetnigrad, el)
        print("Postoji li negativni krug {0}".format(negative_cycle))
        print("Najkraci put duzina: {0}".format(path_length))
        print("Najkraci put: {0}".format(path_nodes))
        print("-------------------------------------")

    end = time.time()
    print(end-start1)

    # Program je n kompleksnosti (Ako ne gledamo što networkx radi u pozadini)


if __name__ == "__main__":
    main()
