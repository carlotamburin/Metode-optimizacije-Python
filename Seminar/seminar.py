from collections import defaultdict
from typing import DefaultDict
from collections import deque


def main():
    # Trazimo unos unutar granica
    unosN = 0
    while True:
        try:
            unosN = int(
                input("Unesite n izmedu 1 i 50 (ukljucujuci obe granice)"))
        except ValueError:
            print("Unesite broj u intervalu od 1 do 50")
        if unosN <= 50 and unosN >= 1:
            break
        else:
            print("Niste unijeli broj u zadanom intervalu \n -1")

    # Ispis konacnog stanja
    vrece = checkIfProper(unosN)
    print("--------------------------------------")
    print(vrece)

# Rekurzivna funkcija koja hvata SVE NESTED DIKTOVE I NJIHOVE KEYEVE I VRIJEDNOSTI


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

# Deklariramo listu od n elementa i dict s n kljuceva i dictovima kao valuese
# lista prikazuje koje su vrijednosti na podu, a dict prikazuje odnose odnosno koja je vreca u kojoj


def checkIfProper(n):
    akcija = []
    vrece = defaultdict(dict)
    pod = list(range(1, n+1))
    pod = [int(i) for i in pod]
    vrece = {el: {} for el in pod}

    while "exit" not in akcija:
        i = 0
        j = 0
        while True:
            akcija = input(
                "Unesite akciju koju želite ivršiti \n PUT i INSIDE j \n SET i LOOSE \n SWAP i WITH j \n Gdje su i i j broj vrece (50>=i,j>=1) ").split()
            if(len(akcija) <= 50 and len(akcija) >= 0):
                break
            else:
                print("Nedozvoljen unos, previše znakova \n -----------")
                print("-1")
        try:
            # Prva akcija
            if(akcija[0] == "PUT"):
                while True:
                    i1 = akcija[1]
                    j1 = akcija[3]
                    i1.lstrip('0')
                    j1.lstrip('0')
                    i = int(i1)
                    j = int(j1)
                    if (i <= 50 and i >= 1) and (j <= 50 and j >= 1):
                        break
                    else:
                        print("i i j nisu u zadanom intervalu \n -----------------")
                        akcija = input(
                            "Unesite akciju koju želite ivršiti \n PUT i INSIDE j \n SET i LOOSE \n SWAP i WITH j \n Gdje su i i j broj vrece (50>=i,j>=1) ").split()
                if(i in vrece and j in vrece):
                    vrece[j][i] = vrece[i]
                    del vrece[i]
                    if(i < j):
                        print("---------------")
                        print(len(vrece))
                    else:
                        print("-1")
                else:
                    print("Krivi unos, obje vrece nisu na podu!")
                    print("-1")
            # Druga akcija
            if(akcija[0] == "SET"):
                while True:
                    i1 = akcija[1]
                    i1.lstrip('0')
                    i = int(i1)
                    if (i <= 50 and i >= 1):
                        break
                    else:
                        print("i i j nisu u zadanom intervalu \n -----------------")
                        print("-1")
                        akcija = input(
                            "Unesite akciju koju želite ivršiti \n PUT i INSIDE j \n SET i LOOSE \n SWAP i WITH j \n Gdje su i i j broj vrece (50>=i,j>=1) ").split()
                if(i in vrece):
                    try:
                        # Dio koda gdje se poziva rekurzivna funkcija
                        for key, value in recursive_items(vrece[i].copy()):
                            vrece[key] = {}
                        print("---------------")
                        print(len(vrece))
                    except IndexError:
                        print(
                            "Nemože se maknuti sadržaj iz vrece posto je ona vec prazna")
                    vrece[i] = {}

                else:
                    print("{0} vreca nije na podu:".format(i))
                    print("-1")
            # Treca akcija
            if (akcija[0] == "SWAP"):
                while True:
                    i1 = akcija[1]
                    i1.strip('0')
                    i = int(i1)
                    j1 = akcija[3]
                    j1.strip('0')
                    j = int(j1)
                    if (i <= 50 and i >= 1) and (j <= 50 and j >= 1):
                        break
                    else:
                        print("i i j nisu u zadanom intervalu \n -----------------")
                        akcija = input(
                            "Unesite akciju koju želite ivršiti (velikim slovima!) \n PUT i INSIDE j \n SET i LOOSE \n SWAP i WITH j \n Gdje su i i j broj vrece (50>=i,j>=1) ").split()
                if(i in vrece and j in vrece):
                    tempVreca = vrece[j]
                    vrece[j] = vrece[i]
                    vrece[i] = tempVreca
                    print("---------------")
                    print(len(vrece))

                else:
                    print("Krivi unos, obje vrece nisu na podu! \n  -1")

            if "exit" in akcija:
                print("Unijeli ste exit, prekid rada programa \n")

        except ValueError:
            print("Nedozvoljeni unos")
        print(vrece)

    return vrece


if __name__ == "__main__":
    main()
