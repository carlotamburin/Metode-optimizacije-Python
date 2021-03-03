from collections import defaultdict
import itertools
from matplotlib import pyplot as plt
import networkx as nx
from networkx import exception
from networkx.algorithms.cuts import normalized_cut_size
import time
from typing import DefaultDict
from math import sqrt
from networkx.algorithms.shortest_paths.weighted import _weight_function
from networkx.readwrite.pajek import generate_pajek
import heapq
from queue import PriorityQueue
import copy
from Carlo_Tamburin_Vjezba7_Zad2 import aStarAlgorithm


def main():

    # Greedy best first search
    d = DefaultDict(list)
    d2 = DefaultDict(list)
    d3 = DefaultDict(list)
    # Unos pocetnog grada
    unosGrada = input("Unesite pocetni grad")
    unosKrajnjegGrada = input("Unesite krajni grad")
    # Niz u kojeg spremamo gradove
    niz = []
    nzi2 = []
    # Citanje u pajek pbliku
    G = nx.read_pajek('airports-astar.net')
    G1 = nx.Graph(G)
    # G2 = nx.DiGraph(G)

    # A* algoritam zadatak 1
    print(" \n A* algoritam ------------------------------")
    Astar = aStarAlgorithm(citanjeKordinata(
        "airports-astar.net"), unosGrada, unosKrajnjegGrada)
    putPreden, udaljenostPredena, vrijemeOdradivanjaAlgoritma = Astar.a_star()
    print("Put preden je: {0}, udaljenost predena je: {1}, vrijeme odradivanja algoritma je: {2}".format(
        putPreden, udaljenostPredena, vrijemeOdradivanjaAlgoritma))

    print(" \n -----------------------------------------")

    # BFS ALGORITAM
    print("Best first search algoritam ---------------------")
    # Citanje iz filea
    niz, niz2 = citanjeIzFilea(d, d2, d3)
    # print(niz)

    #print(udaljenostDoCilja(d3["LHR"][0], d3["BER"][0]))
    print("\n")
    listaPredenihGradova = greedyBFS(
        d, d2, d3, unosGrada, unosKrajnjegGrada, niz, niz2)
    suma = ispisKonacnogPuta(listaPredenihGradova, d2)
    print("\n Suma udaljenosti puta je:{0}".format(suma))

    # Zadatak 2

    put, distanca, vrijemeAlgoritma = Astar.a_star()
    print(put)
    print(distanca)

    # Graf graficki prikazan
    """ generate_pajek(G)
    nx.draw(G1)
    fig = plt.figure(figsize=(15, 10))
    nx.draw(G1)
    plt.show() """


def citanjeKordinata(filename):
    coordinateDict = {}
    with open(filename) as f:
        next(f)
        for line in f:
            if "arcs" in line:
                break
            airport = line.split()
            coordinateDict[airport[1]] = (int(airport[2]), int(airport[3]))

    return coordinateDict


def ispisKonacnogPuta(listaPredenihGradova, d2):
    suma = 0
    brojac = 0
    print("-------------------------")
    for i in range(0, len(listaPredenihGradova)):
        brojac = 0
        for keys, values in d2.items():
            if(brojac != 0):
                break
            if keys == listaPredenihGradova[i][0]:
                for el in values:
                    try:
                        if el[0] == listaPredenihGradova[i+1][0]:
                            print(el[1])
                            suma = suma+int(el[1])
                            brojac += 1
                            break
                    except IndexError:
                        print("Dosli smo do krajnje aerodroma")
                        return suma


def greedyBFS(d, d2, d3, pocetniGrad, zavrsniGrad, niz, niz2):
    brojac1 = 0
    brojac2 = 0
    brojacQ = 0
    kraj = False
    flagPostojanosti = 0
    q = PriorityQueue()
    izbrisaniGrad = None
    predenGrad = ()
    konacnoIzbrisanGrad = ()
    tempGrad = ""
    tempNiz = []
    d4 = d3.copy()
    tempPosition = ""
    ListaPredenihGradova = []

    # Dohvacanje brojcane vrijednosti prvog grada
    for keys, values in d2.items():
        if(pocetniGrad == keys):
            break
        brojac1 += 1

    # Dohvacanje brojcane vrijednosti drugog grada
    for keys, values in d2.items():
        if(zavrsniGrad == keys):
            break
        brojac2 += 1

    # Dobivanje udaljenost od kraja do svake druge tocke u grafu
    print("\n")
    for keys, vakues in d3.items():
        if(zavrsniGrad == keys):
            continue
        d4[keys].append(udaljenostDoCilja(d3[keys][0], d3[zavrsniGrad][0]))
    print(d4)

    ListaPredenihGradova.append((pocetniGrad, d4[pocetniGrad][0][1]))
    # Prolazenje po grafu GLAVNI DIO
    while pocetniGrad != zavrsniGrad:
        brojacQ = 0
        flagPostojanosti = 0
        if pocetniGrad not in d2:
            pass
        else:
            tempNiz.append(d2[pocetniGrad])

        # Radimo for da zaminimo tj stavimo brojcanu vrijenodst na pocetak
        try:
            # ako ude ovdje znaci da postoji element u tempNIzu odnosno imamo jos susjeda
            for el in tempNiz[0]:
                if(pocetniGrad not in d2):
                    break
                if(el[0] == zavrsniGrad):
                    pocetniGrad = zavrsniGrad
                    ListaPredenihGradova.append((zavrsniGrad, 0))
                    kraj = True
                    break
                tempPosition = d4[el[0]]
                q.put(tempPosition[1])
                flagPostojanosti = 1
        except IndexError:
            try:
                if not ListaPredenihGradova:
                    print("Ne moze se doci do kraja")
                    break
                ListaPredenihGradova.pop()
            except IndexError:
                print("Ne moze doci do kraja jer tocka nema susjeda")
                break

        while not q.empty():
            if kraj == True:
                break

            # NEEE RADI radi shallow copy i kad se izbrise listapredenih gradova izbrise se sve u izbrisaniGrad ??

            tempGrad = q.get()
            print(tempGrad)

            if(brojacQ == 0):

                for keys, values in d4.items():
                    try:
                        if values[1] == tempGrad:

                            pocetniGrad = keys
                            ListaPredenihGradova.append(
                                (pocetniGrad, tempGrad))
                            break
                    except IndexError:
                        continue
            brojacQ += 1
            break

        tempNiz.clear()
    print("-----------------------")
    print(ListaPredenihGradova)
    return ListaPredenihGradova


def udaljenostDoCilja(grad1, grad2):
    grad1 = tuple(map(int, grad1))
    grad2 = tuple(map(int, grad2))
    return round(sqrt(pow(grad1[0]-grad2[0], 2) + pow(grad1[1]-grad2[1], 2)))


def citanjeIzFilea(d, d2, d3):
    niz = []
    niz2 = []
    flag = 0

    # Niz 1 do arcs
    f = open('airports-astar.net', 'r')
    next(f)
    for line in f:
        if "arcs" in line:
            break
        niz.append(line.split())

    # niz2 od arcsa pa nadalje
    f.seek(0)
    flag = 0
    for line in f:
        if "arcs" in line:
            flag += 1
        if "arcs" not in line and flag == 0:
            continue
        niz2.append(line.split())

    # Drugi dio koji stvara Dict 1
    for el in niz:
        f.seek(0)
        flag = 0
        for line in f:
            if "arcs" in line:
                flag += 1
            if "arcs" not in line and flag == 0:
                continue
            if(el[0] == line[0]):
                d[el[0]].append(line[2])

    # Stvara se Dict 2 5 komada
    for key, value in d.items():
        for el in niz:
            if(el[0] == key):
                for brid in value:
                    for el2 in niz:
                        if(el2[0] == brid):
                            for elNiza in niz2:
                                if(el[0] == elNiza[0] and el2[0] == elNiza[1]):
                                    d2[el[1]].append(
                                        (el2[1], elNiza[2]))
                                    break
    # Stvara se dict 3
    for el in niz:
        d3[el[1]].append((el[2], el[3]))

    print(d)
    print("-------------------------------------------")
    print(d2)
    print("-------------------------------------------")
    print(d3)
    f.close()
    return niz, niz2


if __name__ == "__main__":
    main()
