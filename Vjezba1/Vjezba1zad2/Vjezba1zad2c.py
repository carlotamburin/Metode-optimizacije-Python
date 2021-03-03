def susjedniProsti():
    brojacUdaljenosti = 0
    brojac = 0
    prostiBrojevi = []
    n = int(input("Unesite do kojeg broja n vraćamo susjedne proste brojeve"))

    for x in range(2, n+1):
        for y in range(2, x):
            if x % y == 0:
                brojac = brojac+1
                break
        if brojac == 0:
            prostiBrojevi.append(x)
        brojac = 0

    for z in range(0, len(prostiBrojevi)):

        if z+1 > len(prostiBrojevi)-1:
            break

        if prostiBrojevi[z+1]-prostiBrojevi[z] == 2:
            print("Par je: {0} i {1} ".format(
                prostiBrojevi[z], prostiBrojevi[z+1]))


susjedniProsti()
