import collections


def obrnutaRecenica():
    recenica = input("Unesite recenicu ").split()
    recenicaobrnuta = []
    j = 0
    konacnarecenicaString = ""

    BrojacRijeci = len(recenica)
    # print(recenica)
    # print(BrojacRijeci)

    for i in range(BrojacRijeci-1, -1, -1):
        recenicaobrnuta.append(recenica[i])
        j += 1

    for ele in recenicaobrnuta:
        konacnarecenicaString += " "+ele
    # print(konacnarecenicaString)

    return konacnarecenicaString


obrnutaRecenica()
# print(obrnutaRecenica())
