def prostiBroj():

    brojac = 0
    n = int(input("Unesite broj"))

    for x in range(2, n):

        if n % x == 0:
            brojac = brojac+1
            print("Broj nije prost")
            break

    if brojac == 0:
        print("Broj je prost")


prostiBroj()
