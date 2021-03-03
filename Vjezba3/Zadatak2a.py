from collections import defaultdict
import csv
from functools import reduce
import json
from os import read
from typing import DefaultDict


def prosjekPrviRok():
    lista = []
    lista1 = []
    lista2 = []

    with open('evidencija.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            lista.append(row["1.rok"])
            lista1.append(row["K1"])
            lista2.append(row["K2"])

        def jeliPopunjen(el):
            if el != "":
                return True
            else:
                return False

        spremnik = list(filter(jeliPopunjen, lista))
        spremnik = list(map(int, spremnik))
        sumaPrviRok = reduce(lambda a, b: a+b, spremnik)
        prosjek1rok = sumaPrviRok/len(spremnik)
        print("Prosjek na 1. ispitnom roku je: {0}".format(prosjek1rok))

        spremnik1 = list(filter(jeliPopunjen, lista1))
        spremnik1 = list(map(int, spremnik1))
        sumaPrvikol = reduce(lambda a, b: a+b, spremnik1)
        prosjek1kol = sumaPrvikol/len(spremnik1)
        print("Prosjek na 1. kolokviju je: {0}".format(prosjek1kol))

        spremnik2 = list(filter(jeliPopunjen, lista2))
        spremnik2 = list(map(int, spremnik2))
        sumaDrugikol = reduce(lambda a, b: a+b, spremnik2)
        prosjek2kol = sumaDrugikol/len(spremnik2)
        print("Prosjek na 2. kolokviju je: {0}".format(prosjek2kol))


def neprisutniNaPrvomKol():
    lista = []
    with open('evidencija.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[4] == "":
                lista.append(row[0])
        print(
            "Studenti koji nisu bili prisutni na 1. kolokviju su: {0}".format(lista))


def nisuIzasliNiNaJedan():
    brojac = 0
    with open('evidencija.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[4] == "":
                if row[5] == "":
                    if row[6] == "":
                        brojac += 1

        print(
            "Studenti koji nisu bili prisutni ni na jednom ispitu: {0}".format(brojac))


def prosjecniRezPolozenih():
    listaK = []
    listaI = []
    polozeniStud = []

    # def jeliPolozeno(el):
    # if el > 40:
    # return el
    # else:
    # return 0

    with open('evidencija.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:

            if row["1.rok"] == "":
                listaI.append("0")
            else:
                listaI.append(row["1.rok"])

            if (row["K1"] != "") and (row["K2"] != ""):
                listaK.append(float((int(row["K1"])+int(row["K2"]))/2))
                continue
            elif (row["K1"] != "") and (row["K2"] == ""):
                listaK.append(row["K1"])
            elif (row["K2"] != "") and (row["K1"] == ""):
                listaK.append(row["K2"])
            else:
                listaK.append("0")

        listaK = list(map(float, listaK))
        listaI = list(map(int, listaI))

        for i in range(0, len(listaK)):
            if listaK[i] >= 40 and listaI[i] >= 40:
                if listaK[i] >= listaI[i]:
                    polozeniStud.append(listaK[i])
                else:
                    polozeniStud.append(listaI[i])

            elif listaK[i] >= 40:
                polozeniStud.append(listaK[i])
            elif listaI[i] >= 40:
                polozeniStud.append(listaI[i])

        ukupno = reduce(lambda a, b: a+b, polozeniStud)
        prosjecnirez = ukupno/len(polozeniStud)
        print("Prosjecan rezultat studenata koji su polozili ispit ili kol: {0}".format(
            prosjecnirez))


def studentiSOdredenomOcjenom():
    ocjena = int(input("Unesite ocjenu"))
    listaI = []
    listaK = []
    rjecnik = {k: [] for k in range(2, 6)}
    najboljiBodovi = []
    listaStudenata = []

    with open('evidencija.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            listaStudenata.append(row["mat."])

            if row["1.rok"] == "":
                listaI.append("0")

            else:
                listaI.append(row["1.rok"])

            if (row["K1"] != "") and (row["K2"] != ""):
                listaK.append(float((int(row["K1"])+int(row["K2"]))/2))

                continue
            elif (row["K1"] != "") and (row["K2"] == ""):
                listaK.append(row["K1"])

            elif (row["K2"] != "") and (row["K1"] == ""):
                listaK.append(row["K2"])

            else:
                listaK.append("0")

        f.seek(0)

        listaK = list(map(float, listaK))
        listaI = list(map(int, listaI))

        for i in range(0, len(listaK)):
            if listaK[i] >= listaI[i]:
                najboljiBodovi.append(listaK[i])
            else:
                najboljiBodovi.append(listaI[i])
        # print(listaStudenata)
        for i in range(0, len(listaStudenata)):
            if (najboljiBodovi[i] >= 40) and (najboljiBodovi[i] < 55):
                rjecnik[2].append(listaStudenata[i])
            if (najboljiBodovi[i] >= 55) and (najboljiBodovi[i] < 70):
                rjecnik[3].append(listaStudenata[i])
            if (najboljiBodovi[i] >= 70) and (najboljiBodovi[i] < 85):
                rjecnik[4].append(listaStudenata[i])
            if (najboljiBodovi[i] >= 85) and (najboljiBodovi[i] <= 100):
                rjecnik[5].append(listaStudenata[i])

        if ocjena == 2:
            print("Studenti s ocjenom 2 : {0}".format(rjecnik[2]))
        if ocjena == 3:
            print("Studenti s ocjenom 3 : {0}".format(rjecnik[3]))
        if ocjena == 4:
            print("Studenti s ocjenom 4 : {0}".format(rjecnik[4]))
        if ocjena == 5:
            print("Studenti s ocjenom 5 : {0}".format(rjecnik[5]))


def zapisUJson():
    listaK = []
    listaI = []
    listaZajson = []
    polozeniStud = []
    najboljiBodovi = []

    listaStudenataMat = []
    listaStudenataStatus = []
    listaStudenataKod = []
    listaStudenataV = []
    listaStudenataK1 = []
    listaStudenataK2 = []
    listaStudenata1R = []

    with open('evidencija.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            listaStudenataMat.append(row["mat."])
            listaStudenataStatus.append(row["status"])
            listaStudenataKod.append(row["kod"])
            listaStudenataV.append(row["V"])
            listaStudenataK1.append(row["K1"])
            listaStudenataK2.append(row["K2"])
            listaStudenata1R.append(row["1.rok"])

            if row["1.rok"] == "":
                listaI.append("0")
            else:
                listaI.append(row["1.rok"])

            if (row["K1"] != "") and (row["K2"] != ""):
                listaK.append(float((int(row["K1"])+int(row["K2"]))/2))
                continue
            elif (row["K1"] != "") and (row["K2"] == ""):
                listaK.append(row["K1"])
            elif (row["K2"] != "") and (row["K1"] == ""):
                listaK.append(row["K2"])
            else:
                listaK.append("0")

        listaK = list(map(float, listaK))
        listaI = list(map(int, listaI))

        for i in range(0, len(listaK)):
            if listaK[i] >= listaI[i]:
                najboljiBodovi.append(listaK[i])
            else:
                najboljiBodovi.append(listaI[i])

        for i in range(0, len(listaK)):
            if najboljiBodovi[i] >= 40:
                polozeniStud.append(najboljiBodovi[i])
                listaZajson.append({"mat.": listaStudenataMat[i],
                                    "status": listaStudenataStatus[i],
                                    "kod": listaStudenataKod[i],
                                    "V": listaStudenataV[i],
                                    "K1": listaStudenataK1[i],
                                    "K2": listaStudenataK2[i],
                                    "1.rok": listaStudenata1R[i]})

        with open('output.json', 'w') as f:
            json.dump(listaZajson, f, indent=4)


prosjekPrviRok()
print("\n")
neprisutniNaPrvomKol()
print("\n")
nisuIzasliNiNaJedan()
print("\n")
prosjecniRezPolozenih()
print("\n")
studentiSOdredenomOcjenom()
zapisUJson()
