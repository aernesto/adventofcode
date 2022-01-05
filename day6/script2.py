# -*- coding: utf-8 -*-
from collections import Counter, deque
import numpy as np
from script import load_line
from joblib import Parallel, delayed

visited_fish = Counter([])


def children(poisson):
    hijos = deque([])
    n_inicial, h_inicial = poisson
    #  print(f"{poisson=}")
    h = h_inicial - (n_inicial + 1)
    i = 0
    while h >= 0:
        hijos.append((8, h))
        h -= 7

    #  print(f"    {hijos=}")
    return hijos


def get_descendants(generacion):
    to_return = deque([])  # array de descendants
    for pez in generacion:
        to_return += children(pez)
    return to_return


def count_single(one_ancestor, weight):
    total_peces = 1
    descendants = deque([one_ancestor])
    ii = 0
    while len(descendants):
        ii += 1
        #  print()
        print(f"{one_ancestor=} -- Peces de la generacion {ii}")
        descendants = get_descendants(descendants)
        #  visited_fish.update(descendants)
        #  print(f"-- total de {len(descendants)} peces\n")
        total_peces += len(descendants)
    return total_peces * weight


def algo(nom_de_fichier, horizon_initial):
    line = load_line(nom_de_fichier)
    conteos = Counter(line)
    unique_values = set(line)

    assert all(v in range(7) for v in unique_values)

    poissons_initiaux = [(v, horizon_initial) for v in unique_values]
    poids = [conteos[v] for v in unique_values]
    pw = zip(poissons_initiaux, poids)

    all_gen = Parallel(n_jobs=4)(delayed(count_single)(*aw) for aw in pw)

    print(all_gen)

    return sum(all_gen)


if __name__ == '__main__':
    from time import perf_counter
    tic = perf_counter()
    print(algo('real.txt', 256))
    print(f"{perf_counter() - tic:.2f} sec")
