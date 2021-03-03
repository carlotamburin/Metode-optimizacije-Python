from collections import defaultdict, deque
import csv
import random
import pprint
from itertools import permutations
import time
from typing import DefaultDict
import time


def sortedBridges():
    lista = []
    g = defaultdict(list)
    brojac = 0
    permaLista = []
    praznaListaZaDfs = []
    prodeniGradovi = []
    prazniGraf = defaultdict()
    listaKljuceva = []

    with open('distance.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            lista.append(row)

        praznaListaZaDfs = input("Unesite gradove").split(",")
        #randomOdabir = random.choice(praznaListaZaDfs)

        # Dodavanje samo gradova ko i u 2. zadatku
        for el in lista:
            for i in range(0, len(el)):
                if el[i] == '':
                    if(brojac == 0):
                        el.remove(el[i])
                    break
                if el[i] == '-':
                    el[i] = 0

        # Popunjavanje dicta sa samo vrhovima
        d = {el: {} for el in lista[0]}

        # Popunjavanje dicta s unutarnjim dictovima
        for row in lista[1:]:
            for el in row:
                brojacZaD = 1
                for elmentD in d:
                    d[el][elmentD] = row[brojacZaD]
                    brojacZaD += 1
                    if(brojac >= len(row)):
                        break
                break

        # Stvaranje sortirane liste bridova

        for keys, values in d.items():
            for keys2, values2 in values.items():
                if(keys in praznaListaZaDfs and keys2 in praznaListaZaDfs):
                    if(keys2 == keys):
                        continue
                    permaLista.append((keys, keys2, int(values2)))
        permaLista.sort(key=lambda x: x[2])
        # print(permaLista)

        # Stvaranje novog grafa

        # Stvaranje liste kljuceva
        for keys in g.keys():
            listaKljuceva.append(keys)

        put = dfs(g, praznaListaZaDfs, prodeniGradovi, permaLista)
        # print(put)
        print(g)


def dfs(graph, start, path, permalista):
    q = deque(start)
    i = 0
    listaPredenihGradova = []
    start1 = time.time()             # Je nas stack
    while q:                                    # Dok stack nije prazan
        v = q.popleft()                         # Micemo sa stacka zadnj ielement
        # Glecamo jesmo li vec bili na tom elementu
        if v not in path and stupanjPojedinogVrha(graph, v) != 3:
            for el in permalista:
                if(el[0] == v and el[1] not in listaPredenihGradova):
                    graph[el[0]].append([el[1], el[2]])
                    listaPredenihGradova.append(el[0])
                    if(i == len(start)-2):
                        listaPredenihGradova.pop(0)

                    i += 1
                    break

            # Ako nismo dodamo ga u listu predenih
            path.append(v)
            # Dodamo njegovu djecu na stack ili ti ga valuese
            for susjedi in graph[v]:
                q.appendleft(susjedi[0])
    end = time.time()
    print(end-start1)
    return path


def stupanjPojedinogVrha(graph, v):
    brojacStupnjeva = 0

    for el in graph[v]:
        brojacStupnjeva += 1
    return brojacStupnjeva


if __name__ == "__main__":
    sortedBridges()
