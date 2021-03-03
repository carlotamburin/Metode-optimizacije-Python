n = int(input("Unesite broj"))
varY = 1


for x in range(1, n*2, 2):
    print("\n")
    for y in range(varY, x+1, 1):
        print(y % 10, end="")

    for z in range(x-1, varY-1, -1):
        if varY > 0:
            print(z % 10, end="")

    varY = varY+1
