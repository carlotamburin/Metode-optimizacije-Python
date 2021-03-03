from matplotlib import pyplot as plt
import networkx as nx
import bellmanford as bf
from networkx.algorithms.cuts import normalized_cut_size
import time


def main():
    # Unos pocetnog grada
    unosGrada = input("Unesite pocetni grad")
    # Niz u kojeg spremamo gradove
    niz = []
    # Citanje u pajek pbliku
    G = nx.read_pajek('airports-split 1.net')
    # G1 = nx.Graph(G)
    # Citanje iz filea kako bi dobili sve vrhove
    niz = citanjeIzFilea()

    dijkstraProlaz(G, unosGrada, niz)

# Citanje iz filea da uhvatimo vrhove


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


# dijkstra funkcija za pronalazak najkraceg puta izmedu pocetnog i svih ostalih gradova
def dijkstraProlaz(G, pocetniGrad, niz):
    start1 = time.time()
    for el in niz:
        if el == pocetniGrad:
            continue
        print(nx.dijkstra_path(G, pocetniGrad, el), end=" ")
        print(nx.dijkstra_path_length(G, pocetniGrad, el))
    end = time.time()
    print(end-start1)

    # Program je n kompleksnosti (Ako ne gledamo što networkx radi u pozadini)


if __name__ == "__main__":
    main()
