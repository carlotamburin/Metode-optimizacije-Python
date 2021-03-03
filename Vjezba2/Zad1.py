def zajednickiElementi():
    lista1 = input("Unesite elemente liste").split()
    lista2 = input("Unesite element druge liste").split()

    print(lista1)
    print(lista2)

    print("\n")

    s1 = set(lista1)
    s2 = set(lista2)

    print(s1)
    print(s2)

    s = s1.intersection(s2)
    sList = list(s)

    print(sList)


zajednickiElementi()
