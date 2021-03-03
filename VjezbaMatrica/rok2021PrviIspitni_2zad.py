from collections import defaultdict
import copy
from typing import ItemsView
from random import seed
from random import randint


def najbliziSusjedi():
    lista = []
    lista2 = []
    i = 0
    j = 0
    konacnalista = []
    konacnalista2 = []
    brojGradova = 0
    brojac = 0
    brojac2 = 0
    listaGradovaSusjeda = []
    listapredenihBrojevi = []
    minValue = 0
    flag = 0
    tempgrad = 0
    tempgradUdaljenost = 0
    new_dict = defaultdict(dict)
    listapredenih = []

    with open("gradovi.txt", "r") as f:
        for el in f:
            lista.append(el)
        # print(lista)

        for el in lista:
            temp = el.split(' ')
            brojelemenata = len(temp)
            lista2.append(temp)
        # print(lista2)

        for el in lista2:
            konacnalista.clear()
            for el2 in el:
                if(el2 != "\n"):
                    konacnalista.append(el2)
            konacnalista2.append(copy.deepcopy(konacnalista))
        # print(konacnalista2)

        # castanje i dobivanje duzine
        for el in konacnalista2:
            for i in range(0, len(el)):
                brojGradova = len(el)
                el[i] = int(el[i])
        print(konacnalista2)

        # stvaranje nested dictova
        new_dict = {new_list: {key: [] for key in range(
            brojGradova)} for new_list in range(brojGradova)}

        # Izbacivanje samog sebe kao ussjeda
        for keys, values in new_dict.items():
            if(keys in new_dict[keys]):
                new_dict[keys].pop(keys, None)
        # print(new_dict)

        i = 0
        j = 0
        for keys, values in new_dict.items():
            for keys2, values2 in values.items():
                if(konacnalista2[i][j] == 0):
                    j = j+1
                    new_dict[keys][keys2].append(konacnalista2[i][j])
                    j = j+1
                    continue
                new_dict[keys][keys2].append(konacnalista2[i][j])
                j = j+1
                continue
            i = i+1
            j = 0

        print(new_dict)

        # Obilazak
        n = int(input("Unesite koliko gradova zelite obici"))
        randomPocetniGrad = randint(0, 4)
        print(randomPocetniGrad)
        listapredenih.append((randomPocetniGrad, 0))
        listapredenihBrojevi.append(randomPocetniGrad)

        while(brojac != n):

            # stavljamo sve susjede u listu i uzimamo najmanji
            listaGradovaSusjeda = list(new_dict[randomPocetniGrad].values())
            listaGradovaSusjeda = sorted(listaGradovaSusjeda)
            minValue = listaGradovaSusjeda[brojac2]

            for keys, values in new_dict[randomPocetniGrad].items():
                if(values == minValue):
                    tempgrad = keys
                    tempgradUdaljenost = values
                    break

            if(tempgrad not in listapredenihBrojevi):
                listapredenih.append((tempgrad, tempgradUdaljenost[0]))
                listapredenihBrojevi.append(tempgrad)
                randomPocetniGrad = tempgrad
                brojac = brojac+1
                brojac2 = 0
            else:
                brojac2 = brojac2+1

            if(brojac == n):

                listapredenih.append(
                    (listapredenih[0][0], new_dict[randomPocetniGrad][listapredenih[0][0]][0]))

        print("Lista predenih gradova:{0}".format(listapredenih))


if __name__ == "__main__":
    najbliziSusjedi()
