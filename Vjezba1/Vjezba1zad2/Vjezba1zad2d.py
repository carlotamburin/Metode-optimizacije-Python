def naciniPrikazaBroja():
    prostiBrojevi = []
    brojac = 0
    while 1:
        broj = int(input("Unesite parni broj"))
        if broj % 2 != 0:
            print("Broj nije paran unesite ponovno")
        else:
            break

    for x in range(2, broj):
        for y in range(2, x):
            if x % y == 0:
                brojac = brojac+1
                break
        if brojac == 0:
            prostiBrojevi.append(x)
        brojac = 0

    for z in range(0, len(prostiBrojevi)):
        for t in range(0, z+1):
            if prostiBrojevi[z]+prostiBrojevi[t] == broj:
                print("Broj: {0} se može prikazati kao zbroj dva prosta broja {1} i {2}".format(
                    broj, prostiBrojevi[z], prostiBrojevi[t]))


naciniPrikazaBroja()
