import random


def kamenSkarePapir():

    bodoviIgrac = 0
    bodoviRacunalo = 0
    rezultat = [(1, 2), (3, 1), (2, 3)]

    while bodoviIgrac <= 5 or bodoviRacunalo <= 5:
        print("1. Kamen")
        print("2. Skare")
        print("3. Papir")

        odabirIgrac = int(
            input("odaberite broj pokraj predmeta kojeg zelite igrati"))
        odabirRacunalo = random.randint(1, 3)
        print("\n")

        for i in range(0, len(rezultat)):
            if (odabirIgrac in rezultat[i]) and (odabirRacunalo in rezultat[i]):
                for j in range(0, len(rezultat[i])):

                    if (odabirIgrac == rezultat[i][0]) and (odabirIgrac != odabirRacunalo):
                        bodoviIgrac += 1
                        break
                    elif (odabirRacunalo == rezultat[i][0]) and (odabirIgrac != odabirRacunalo):
                        bodoviRacunalo += 1
                        break
                    elif (odabirIgrac == odabirRacunalo):
                        break
        print("Igrac je odabrao {0}".format(odabirIgrac))
        print("Racunalo je odabralo {0}".format(odabirRacunalo))
        print("[Igrac {0} bodova]".format(bodoviIgrac))
        print("[Racunalo {0} bodova]".format(bodoviRacunalo))
        print("\n")

        if bodoviIgrac == 5:
            print("Igrac je pobijedio")
            break
        elif bodoviRacunalo == 5:
            print("Racunalo je pobijedilo")
            break


kamenSkarePapir()
