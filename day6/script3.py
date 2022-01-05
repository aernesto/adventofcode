# -*- coding: utf-8 -*-
import numpy as np
from script import load_line
from collections import Counter


def update_line(ligne):
    #  print(f"\n--entering update_line")
    #  print(ligne)
    num_8 = ligne[0]
    new_line = ligne[1:]
    new_line.append(num_8)
    new_line[6] += num_8
    #  print(ligne)
    #  print(f"\n--exiting update_line")
    return new_line


def optimal(f, l):
    line = load_line(f)
    peces_con_coef = Counter(line)
    row = [peces_con_coef[i] for i in range(9)]
    for i, day in enumerate(range(l)):
        row = update_line(row)
        if i % 10 == 0:
            print(day)

    return sum(row)


if __name__ == "__main__":
    import sys
    fichier = sys.argv[1]
    print(optimal(fichier, 256))
