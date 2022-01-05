# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter


def load_line(filename):
    with open(filename, 'rt') as fh:
        texte = fh.read().strip()
    return np.array([int(c) for c in texte.split(',')])


def update_line(ligne):
    print(f"\n--entering update_line")
    print(ligne)
    num_8 = ligne[0]
    del ligne[0]
    for entry in ligne:
        ligne[entry - 1] = ligne[entry]
    if num_8:
        ligne[6] += num_8
        ligne[8] += num_8
    print(ligne)
    print(f"\n--exiting update_line")
    return None


def main(f, l):
    line = load_line(f)
    peces_con_coef = Counter(line)
    print(peces_con_coef)

    for i, day in enumerate(range(l)):
        update_line(peces_con_coef)
        if i % 10 == 0:
            print(day)

    return peces_con_coef.total()


if __name__ == "__main__":
    import sys
    fichier = sys.argv[1]
    print(main(fichier, 18))
