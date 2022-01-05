# -*- coding: utf-8 -*-
import numpy as np


def load_line(filename):
    with open(filename, 'rt') as fh:
        texte = fh.read().strip()
    return np.array([int(c) for c in texte.split(',')])


def update_line(ligne):
    num_8 = sum(ligne == 0)
    #  print(num_8)
    array_of_8 = np.ones(num_8) * 8
    new_line = ligne - 1
    new_line[new_line == -1] = 6
    return np.r_[new_line, array_of_8]


def main(f, l):
    line = load_line(f)
    #  print(line)
    for i, day in enumerate(range(l)):
        line = update_line(line)
        if i % 10 == 0:
            print(day)
        #  print(line)
    print(len(line))
    return len(line)


if __name__ == "__main__":
    import sys
    fichier = sys.argv[1]
    main(fichier, 180)
