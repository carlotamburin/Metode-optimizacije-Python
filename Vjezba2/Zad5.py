import collections
from typing import OrderedDict
from collections import defaultdict


def obrtanjeRjecnika():
    lista = []
    lista2 = []
    max = 0
    min = 0

    d = dict()
    d2 = defaultdict(list)
    d3 = defaultdict(int)

    for i in range(1, 4):
        lista = input("Unesite {0} listu ".format(i)).split()
        for j in range(0, len(lista)):
            lista[j] = int(lista[j])
            if(lista[j] > max):
                max = lista[j]
            if(j == 0 and i == 0):
                min = lista[j]
            if(lista[j] < min):
                min = lista[j]

        d[i] = lista

    print(d)

    print(max)
    print(min)
    print("\n")

    for key, value in d.items():
        for i in range(0, len(value)):
            d2[value[i]].append(key)

    print("Ne sortirani dictionary {0}".format(d2))

    for key, value in d2.items():
        temp = key
        lista2.append(temp)

    lista2.sort()

    for key, value in d2.items():
        for i in range(0, len(lista2)):
            d3[lista2[i]] = d2.get(lista2[i])

    #print("Konacni dict je: {0}".format(d3))

    return d3


obrtanjeRjecnika()
# print(obrtanjeRjecnika())
