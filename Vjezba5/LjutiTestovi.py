import csv
import pprint
from itertools import permutations
import time


def citanjeIzFilea():
    with open('distance.csv') as f:
        reader = csv.reader(f, delimiter=',')
        return reader


Datoteka = citanjeIzFilea()

for row in Datoteka:
    print(row)
