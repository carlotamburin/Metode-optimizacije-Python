def prostiCounter():
    n = float(input("Unesi prvi decimalni broj"))
    m = float(input("Unesi drugi decimalni broj"))

    # print(n)
    # print(m)
    n = int(round(n))
    m = int(round(m))

    counter = 0
    counterProstih = 0

    for x in range(n+1, m):
        for y in range(2, x):
            if x % y == 0:
                counter = counter+1

        if counter == 0:
            counterProstih = counterProstih+1
        counter = 0

    print("Izmedu {0} i {1} ima {2} prostih brojeva".format(
        n, m, counterProstih))


prostiCounter()
