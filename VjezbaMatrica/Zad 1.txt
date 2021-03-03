import copy
from collections import defaultdict, deque


def matrica():
    new_dict = defaultdict(list)
    tempDict = defaultdict(list)
    lista = []
    lista2 = []
    counter = 0
    tempIzlazniVrh = 0
    tempUlazniVrh = 0
    konacnalista = []
    konacnalista2 = []
    brojelemenata = 0
    listasortirana = []
    templista = []

    # Citamo ali s \n znakovima
    with open("matrica.txt", "r") as f:
        for el in f:
            lista.append(el)

        # stavljamo listu u listu AKA matrica i micemo \n
        for el in lista:
            temp = el.split(' ')
            brojelemenata = len(temp)
            lista2.append(temp)

        # print(lista2)

        # Lista u listi normalan izgled
        for el in lista2:
            konacnalista.clear()
            for el2 in el:
                if(el2 != "\n"):
                    konacnalista.append(el2)
            konacnalista2.append(copy.deepcopy(konacnalista))

        # Trebamo zaminiti retke i stupce
        while(counter < brojelemenata-1):
            for el in konacnalista2:
                templista.append(el[counter])
            listasortirana.append(copy.deepcopy(templista))
            counter = counter+1
            templista.clear()
        # print(listasortirana)

        # Castanje

        for el in listasortirana:
            for i in range(0, len(el)):
                el[i] = int(el[i])

        # Stavljamo sve u dictionary
        new_dict = {new_list: [] for new_list in range(brojelemenata)}
        # print(new_dict)

        # kreiramo listu po kojoj cemo sortirati ulazne bridove
        sortiraniUlazniBridovi = [el for el in range(0, 5)]
        # print(sortiraniUlazniBridovi)
        # Brojac sortiranih ulazni bridova, konbinirat cemo sa soritraniUlazniBridovi
        sortiraniUlazniBridoviBrojac = [0 for el in range(0, 5)]
        # print(sortiraniUlazniBridoviBrojac)

        for el in listasortirana:
            for el2 in el:
                if(el2 == 1):
                    tempIzlazniVrh = el.index(el2)
                if(el2 < 0):
                    tempUlazniVrh = el.index(el2)
                    sortiraniUlazniBridoviBrojac[el.index(
                        el2)] = sortiraniUlazniBridoviBrojac[el.index(el2)]+1

            new_dict[tempIzlazniVrh].append(tempUlazniVrh)

        print("Dict prije sortiranja: {0}".format(new_dict))
        kombinirano = list(
            zip(sortiraniUlazniBridovi, sortiraniUlazniBridoviBrojac))
        # print(kombinirano)

        konacnoSortiranaLista = sorted(
            kombinirano, key=lambda x: x[1], reverse=False)
        print("Kako bi trebao izgledati dict u obliku liste: {0}".format(
            konacnoSortiranaLista))

        tempDict = {el[0]: [] for el in konacnoSortiranaLista}
        # print(tempDict)

        for keys, values in new_dict.items():
            tempDict[keys] = values
        print("Konacno sortirani dictionary:{0}".format(tempDict))

        postojiLiPut(1, 4, tempDict)


def postojiLiPut(vrh1, vrh2, d):
    q = deque(d[vrh1])

    listapredenih = []

    while(q):
        v = q.popleft()
        if(v == vrh2):
            print("Postoji put")
            return True
        if(v not in listapredenih):
            listapredenih.append(v)
            q.extendleft(reversed(d[v]))

    print("ne postoji put")
    return False


if __name__ == "__main__":
    matrica()
