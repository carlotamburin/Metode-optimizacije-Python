import collections
import pickle


def brojanjeRijeci():
    with open("rijeci.txt") as f:
        string = []

        temp = 0
        d = dict()

        for line in f:
            string.extend(line.split())
        print(string)

        print("\n")

        for i in range(0, len(string)):
            if(i == 0):
                d[string[i]] = 1
                continue
            for j in range(0, i):
                if(string[i] == string[j]):
                    d[string[j]] += 1
                    break
            else:
                d[string[i]] = 1

        print(d)

        print("\n")

        f.close()


brojanjeRijeci()
