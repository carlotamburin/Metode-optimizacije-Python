import csv
import pprint
from itertools import permutations
import time
from typing import DefaultDict
import time


def closestNeighbor():
    d = DefaultDict()
    lista = []
    brojac = 0
    brojacZaD = 2
    listaZaSortiranjeTemp = []
    tempLista = []
    permaLista = []
    BrojacZaPut = 0
    listaPredenihGradova = []

    with open('distance.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:

            lista.append(row)

        # Uredivanje liste
        for el in lista:
            for i in range(0, len(el)):
                if el[i] == '':
                    if(brojac == 0):
                        el.remove(el[i])
                    break
                if el[i] == '-':
                    el[i] = 0
        # print(lista)

        # Stvaranje dictionarya koristeći dictionary comprehension s gradovima kao keys i valuesima za sad praznim
        d = {el: {} for el in lista[0]}

        # Popunjavanje dictionarya s dictionaryma
        for row in lista[1:]:
            for el in row:
                brojacZaD = 1
                for elmentD in d:
                    d[el][elmentD] = row[brojacZaD]
                    brojacZaD += 1
                    if(brojac >= len(row)):
                        break
                break

        # Korisnikov unos te dodavanje tog grada u listu predenih
        korisnikovUnos = input("Unesite grad od kojeg zelite poceti")
        listaPredenihGradova.append(korisnikovUnos)

        start = time.time()

        # Logika najblizeg susjeda
        while (BrojacZaPut < 36):
            for keys, values in d.items():
                listaZaSortiranjeTemp.clear()
                tempLista.clear()

                if(keys == korisnikovUnos):
                    for keys2, values2 in values.items():
                        if(keys2 in listaPredenihGradova):
                            continue
                        listaZaSortiranjeTemp.append([keys2, values2])
                        permaLista.append([keys2, values2])

                # print(listaZaSortiranje)

                    for el in listaZaSortiranjeTemp:  # Maknit vec predene clanove
                        tempLista.append(int(el[1]))

                    tempLista = sorted(tempLista)
                    # tempLista.remove(0)     # Sad cemo viditi
                    tempMin = tempLista[0]
                    # print(tempLista)
                    # print(tempMin)

                    for el in listaZaSortiranjeTemp:
                        if(int(el[1]) == tempMin):
                            korisnikovUnos = el[0]
                            listaZaSortiranjeTemp.remove(el)
                            listaPredenihGradova.append(el[0])
                            print(el[1])
                            break

                    print(korisnikovUnos)
                    BrojacZaPut += 1
                    if(BrojacZaPut == 36):
                        print(d[korisnikovUnos][listaPredenihGradova[0]])
                        print(listaPredenihGradova[0])
                    break
        end = time.time()
        print(end-start)


if __name__ == "__main__":
    closestNeighbor()
