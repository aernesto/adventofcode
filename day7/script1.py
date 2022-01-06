# -*- coding: utf-8 -*-
import numpy as np
from collections import Counter


def load_line(filename):
    with open(filename, 'rt') as fh:
        texte = fh.read().strip()
    return np.array([int(c) for c in texte.split(',')])


def energia(x, freq):
    terms = 0
    for p in freq:
        n = freq[p]
        terms += n * abs(p - x)
    return terms


def main_function(fichier):
    numeros = load_line(fichier)
    frecuencias = Counter(numeros)
    e_min = 9999999999999999
    for xx in set(numeros):
        e = energia(xx, frecuencias)
        if e < e_min:
            e_min = e
            x_opt = xx
    return x_opt, e_min


if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    print(main_function(f))
