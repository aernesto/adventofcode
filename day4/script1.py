# -*- coding: utf-8 -*-
import numpy.ma as ma
import numpy as np


def read_numbers(string, sep):
    stripped = string.strip()
    if stripped:
        return [int(s) for s in stripped.split(sep) if len(s)]


def lire_data(fichier):
    tables = []  # Lista vacia de matrices
    with open(fichier, 'rt') as fh:
        for index, line in enumerate(fh):
            if index == 0:
                numeros = read_numbers(line, ',')
                matriz = []
            else:
                if not line.strip():  # linea vacia
                    if matriz:
                        tables.append(matriz)
                    matriz = []  # inicializar matriz vacia
                else:  # linea con numeros
                    linea = read_numbers(line, ' ')
                    matriz.append(linea)

    if matriz:
        tables.append(matriz)
    return numeros, tables


def appliquer_masque(table, number):
    boolean_mask = (table.data == (number * np.ones(table.data.shape)))
    table.mask = np.logical_or(table.mask, boolean_mask)


def compute_score(table, number):
    col_sum = table.mask.sum(axis=0)
    row_sum = table.mask.sum(axis=1)
    if any([c == 5 for c in set(col_sum).union(set(row_sum))]):
        return table.sum() * number
    return None


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    tirage, tableaux = lire_data(filename)
    tableaux = [ma.array(t) for t in tableaux]
    tableaux_ayant_gagne = [False for _ in tableaux]

    for numero in tirage:
        for index_tableau, tableau in enumerate(tableaux):
            if tableaux_ayant_gagne[index_tableau]:
                continue

            appliquer_masque(tableau, numero)
            score = compute_score(tableau, numero)
            if score:
                tableaux_ayant_gagne[index_tableau] = True
                last_score = score
    print(last_score)
