import csv
import pprint
from itertools import permutations
import time


def bruteForce():

    # Deklariranje varijabli
    pomocniFlag = 0
    lista = []
    listaGradova = []
    tempIndex = ""
    suma = 0
    flag = 0
    minSuma = []
    udaljenosti = []
    gradoviKonacni = []

    with open('distance.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            lista.append(row)

        # Unosimo pocetni grad
        Start = input("Unesite pocetni grad ")

        # Unosimo gradove
        gradoviUnos = input("Unesite gradove koje zelite obici i Vratiti se ")
        listaGradova = gradoviUnos.split()
        listaGradovaNum = []

        for el in lista[0]:
            for grad in listaGradova:
                if(grad == el):
                    # -1 zato jer nemamo u nasoj numerickoj listi gradova ne zelimo ' znak
                    listaGradovaNum.append(lista[0].index(el)-1)

        # Index za pocetni grad
        indexpg = lista[0].index(Start)

        # Permutacije
        perm = permutations(listaGradovaNum)

        start = time.time()

        # Logika za stvaranje veza izmedu redaka i stupaca u tablici
        for gradovi in list(perm):
            gradoviKonacni.clear()
            gradovi = list(gradovi)
            gradoviKonacni = gradovi.copy()
            gradoviKonacni.append(indexpg-1)
            gradoviKonacni.insert(0, indexpg-1)
            pomocniFlag = 0

            for grad in gradoviKonacni:
                flag = 0
                pocetniGrad = grad

                if(pomocniFlag == 1 and pocetniGrad == gradoviKonacni[0]):
                    enumeracija = [i for i, n in enumerate(
                        gradoviKonacni) if n == pocetniGrad][1]

                    if(enumeracija+1 >= len(gradoviKonacni)):
                        print("Ukupna suma ovog puta je: {0}".format(suma))
                        print("\n")
                        udaljenosti.append(suma)
                        suma = 0
                        break

                elif(grad == gradoviKonacni[0]):
                    pomocniFlag = 1

                if(gradoviKonacni.index(pocetniGrad)+1 < len(gradoviKonacni)):
                    KrajniGrad = gradoviKonacni[gradoviKonacni.index(
                        pocetniGrad)+1]
                else:
                    # Dodaj zadnji
                    print("Ukupna suma ovog puta je: {0}".format(suma))
                    print("\n")
                    udaljenosti.append(suma)
                    suma = 0
                    break
                for el in lista[1:]:
                    if(flag == 1):
                        break
                    if(el[0] != lista[0][pocetniGrad+1]):
                        continue

                    for i in range(len(el)):
                        if(flag == 1):
                            break
                        if(el.index(el[i]) == pocetniGrad):
                            #print("Nasli smo ga na indexu je: {0}".format(lista.index(el)))
                            pocetak = el
                            for el2 in lista[0]:
                                if(lista[0].index(el2) == KrajniGrad+1):
                                    tempIndex = lista[0].index(el2)
                                    suma = int(suma)+int(el[tempIndex])
                                    flag = 1
                                    print("Udaljenost izmedu {0} i {1} je: {2}".format(
                                        lista[0][pocetniGrad+1], lista[0][KrajniGrad+1], el[tempIndex]))
                                    minSuma.append(
                                        (lista[0][pocetniGrad+1], lista[0][KrajniGrad+1], el[tempIndex]))
                                    break
                                    # print(tempIndex)

        # for el in minSuma:
            # print(el)
        print(min(udaljenosti))

        end = time.time()
        print(end-start)

        # Slozenost n^5


if __name__ == "__main__":
    bruteForce()
