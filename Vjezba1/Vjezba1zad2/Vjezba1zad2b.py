def vratiProsti():

    n = 0
    brojac = 0
    prostiBrojevi = []

    for x in range(2, 1000):
        for y in range(2, x):
            if x % y == 0:
                brojac = brojac+1
                break
        if brojac == 0:
            prostiBrojevi.append(x)
        brojac = 0
    n = int(input("Unesite n"))

    while 1:
        if n <= 0:
            print("Krivi unos")
            break
        else:

            print(prostiBrojevi[n-1])
            break


vratiProsti()
