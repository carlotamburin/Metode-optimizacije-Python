from os import remove
import pprint
from collections import defaultdict
import csv
import random
from networkx.algorithms.euler import is_eulerian

from networkx.generators.classic import null_graph


def Vjezba1i2():
    lineCounter = 0
    niz = []
    niz2 = []
    d = defaultdict(list)
    d2 = defaultdict(list)
    d3 = defaultdict(list)
    AI = 0
    # Dodavanje iz fila u niz
    f = open("football.net", 'r')
    next(f)
    for line in f:
        if "*Arcs" in line:
            break
        niz.append(line.split())
        lineCounter += 1
    # Dodavanje iz filea u dict
    for i in range(0, len(niz)):
        d[niz[i][0]] += niz[i][1]

    # Micanje nepotrebnih znakova iz dicta
    for v in d.values():
        for s in v:
            if s == '"':
                v.remove(s)

    f.seek(0)
    # Postavljanje pocetne tocke
    for line in f:
        if "*Arcs" not in line and AI == 0:
            pass
        elif AI == 0:
            AI = 1
        elif AI == 1:
            niz2.append(line.split())
    # Stvaranje drugog dictionaria
    for el in d.keys():
        for i in range(0, len(niz2)):
            for j in range(0, len(niz2[i])):
                if el in niz2[i]:
                    if niz2[i][j] == el:
                        pass
                    else:
                        d2[tuple(d.get(el))] += (niz2[i][j])

        # Micanje nepotrebnih znakova u tupleu
        for v in d2.keys():
            for s in v:
                if s == '"':
                    v.remove(s)

    pprint.pprint(d)
    pprint.pprint(d2)
    pprint.pprint(d3)

    # Stvaranje liste ssusjedstva iz prijasnja 2 dictionaria
    for keys, values in d.items():
        for k, v in d2.items():
            for el in v:
                if el == keys:
                    d3[k].extend(values)

    pprint.pprint(d3)

    # Sad se radi matrica susjedstva, prvo prazna
    #
    #
    #

    matricaSusjedstva = [[0 for i in range(len(d3))]for j in range(len(d3))]

    # pprint.pprint(matricaSusjedstva)  Printa praznu matricu

    i = 0
    for keys, values in sorted(d2.items()):
        for el in values:
            # dodaju se jedinice na mijesta gdje su keyse odredenih bridova-1 zbog nultog indeksiranja
            matricaSusjedstva[i][int(el)-1] = 1
        i += 1
    pprint.pprint(matricaSusjedstva)

    # matrica incidencije
    #
    #
    #

    # Dolazenje do broja stupaca odnosno broj edgova
    nizPonavljajucih = []
    counterPonavljanja = 0

    for keys, values in sorted(d3.items()):
        for k in values:
            if(k not in nizPonavljajucih):
                counterPonavljanja += 1
        nizPonavljajucih.extend(keys)
    print("\n")
    # print(counterPonavljanja)
    #
    #
    # Prazna matrica
    matricaIncidencije = [
        [0 for i in range(counterPonavljanja)]for j in range(len(d3))]

    # pprint.pprint(matricaIncidencije)
    # Postavljanje matrice
    #
    #
    j = 0
    tempTuple = ""
    nizPonavljajucih2 = []
    for keysD2, valuesD2 in sorted(d2.items()):
        for k in valuesD2:
            if(d[k][0] not in nizPonavljajucih2):
                matricaIncidencije[int(k)-1][j] = 1
                for keysD, valuesD in sorted(d.items()):
                    tempTuple = keysD2[0]
                    if valuesD[0] == tempTuple:
                        matricaIncidencije[int(keysD)-1][j] = 1
                j += 1
            nizPonavljajucih2.extend(tempTuple)
    pprint.pprint(matricaIncidencije)
    ###
    ###
    ###
    # Poziv funkcije za racunanje stupnjeva
    print("\n")
    stupanjPojedinogVrha(d2)
    ###
    print("\n")
    ###
    # Poziv funkcije max incidenti vrhovi
    maxIncidentiVrhovi(d2)
    ####
    ####
    # Poziv funkcije jeliEulerov vrh i racunanje
    print("\n")
    dEulerov = d3.copy()
    JeliEuleroviEulerovPut(dEulerov)

    f.close()


def brojVrhova():
    AI = 0
    niz = []
    counterVrhova = 0

    f = open("football.net", 'r')
    for line in f:
        if '*Vertices' not in line and AI == 0:
            pass
        elif AI == 0:
            AI = 1
        elif AI == 1:
            if(('*Arcs' in line) or ('*Edges' in line)):
                break
            niz.append(line.split())
            counterVrhova += 1

    print(counterVrhova)

    f.close()


def brojBridova():
    AI = 0
    niz = []
    counterBridova = 0
    f = open("football.net", 'r')
    for line in f:
        if '*Edges' not in line and AI == 0:
            pass
        elif AI == 0:
            AI = 1
        elif AI == 1:
            if(('*Arcs' in line) or ('*Vertices' in line)):
                continue
            else:
                niz.append(line.split())
                counterBridova += 1
    niz = list(filter(None, niz))
    counterBridova = len(niz)
    print(counterBridova)

    f.close()


def stupanjPojedinogVrha(d2):
    BrojacStunjeva = 0
    for keys, values in d2.items():
        for el in values:
            BrojacStunjeva += 1
        print("Vrh: {0} je : {1} stupnja".format(keys[0], BrojacStunjeva))
        BrojacStunjeva = 0


def maxIncidentiVrhovi(d2):

    BrojacStunjeva = 0
    max = 0
    for keys, values in d2.items():
        for el in values:
            BrojacStunjeva += 1
        if max < BrojacStunjeva:
            max = BrojacStunjeva
        BrojacStunjeva = 0

    for keys2, values2 in d2.items():
        for el2 in values2:
            BrojacStunjeva += 1
        if BrojacStunjeva == max:
            print("Vrh: {0} je : {1} stupnja ujedno i maximalnog".format(
                keys2[0], BrojacStunjeva))
        BrojacStunjeva = 0


def JeliEuleroviEulerovPut(d3):

    kljucevi = []
    tempVrh = ""
    EulerovPut = []
    i = 0

# Ucitava se kljuceve koje postoje da bi mogao random odabrati jedan za pocetak
    for keys, values in sorted(d3.items()):
        kljucevi.append(keys)

# Odabire random kljuc za pocetak
    randomPocetak = random.choice(kljucevi)
    # print(randomPocetak[0])

# Micanjem 2 brida dobivamo eulerov graf
    for keys, values in sorted(d3.items()):
        if keys == kljucevi[0]:
            values.remove('E')
        if keys == kljucevi[4]:
            values.remove('A')

     # ispitujemo jeli graf eulerov
     # ############ #Note----------------> Graf je eulerov jer smoo oduzeli brid A E kako bi broj bridovova iz svakog vrha bio paran
    brojacStupnjeva = 0
    brojacNeparnih = 0
    for keys, values in d3.items():
        for el in values:
            brojacStupnjeva += 1

        if(brojacStupnjeva % 2 != 0):
            print("Graf nije eulerov")
            brojacNeparnih += 1
            break
        brojacStupnjeva = 0

    if(brojacNeparnih == 0):
        print("Graf je eulerov")


# Eulerov put
#
#
    while len(kljucevi) != 0:
        for keys, values in sorted(d3.items()):
            if(randomPocetak == keys):
                # print(values)
                kljucevi.remove(randomPocetak)
                EulerovPut.insert(0, randomPocetak)
                randomPocetak = None

                tempVrh = random.choice(kljucevi)
                while len(kljucevi) != 0:
                    if((tempVrh[0] not in values) or (tempVrh not in kljucevi)):
                        tempVrh = random.choice(kljucevi)
                    else:
                        break
                i += 1

            elif i == 1:
                if(tempVrh == keys):
                    if(len(kljucevi) == 0):
                        break
                    kljucevi.remove(tempVrh)
                    EulerovPut.append(tempVrh)

                    while len(kljucevi) != 0:
                        try:
                            if((tempVrh[0] not in values) or (tempVrh not in kljucevi)):
                                tempVrh = random.choice(kljucevi)
                                if(len(kljucevi) == 1):
                                    kljucevi.remove(tempVrh)
                                    if(tempVrh[0] in values):
                                        EulerovPut.append(tempVrh)
                                    break
                            else:
                                break
                        except:
                            pass
                        finally:
                            break

    print(EulerovPut)
    if(len(EulerovPut) == len(d3)):
        print("Uspjesno naden eulerov put")
    else:
        print("Neuspjesno naden eulerov put")


Vjezba1i2()
# brojVrhova()   Ukljuciti za provjeru!!
# brojBridova()  Ukljuciti za provjeru!!
