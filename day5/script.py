# -*- coding: utf-8 -*-
import numpy as np


def read_points(path):
    segments = []
    x_max, y_max = 0, 0

    def update(old, new):
        return old if new <= old else new

    with open(path, 'rt') as fh:
        for line in fh:
            left, right = line.split(' -> ')
            left = left.split(',')
            right = right.split(',')
            x1, y1 = int(left[0]), int(left[1])
            x2, y2 = int(right[0]), int(right[1])
            x_max = update(x_max, x1)
            x_max = update(x_max, x2)
            y_max = update(y_max, y1)
            y_max = update(y_max, y2)
            segments.append([(x1, y1), (x2, y2)])

    return segments, x_max, y_max


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    lignes, xx, yy = read_points(filename)
    print(f'{len(lignes)=}  {lignes[0]=}  {lignes[-1]=}')
    print(f'{xx=}  {yy=}  {lignes[-1]=}')

    matriz = np.zeros((xx + 1, yy + 1))

    for ligne in lignes:
        p1, p2 = ligne
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = x2 - x1, y2 - y1
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2) + 1):
                matriz[x1, j] += 1
        elif y1 == y2:
            for k in range(min(x1, x2), max(x1, x2) + 1):
                matriz[k, y1] += 1
        elif abs(dx) == abs(dy):
            step_x = int(dx / abs(dx))
            step_y = int(dy / abs(dy))
            for i, j in zip(range(x1, x2, step_x), range(y1, y2, step_y)):
                matriz[i, j] += 1
            matriz[i + step_x, j + step_y] += 1
        else:
            print(ligne, 'not 45!!')

    #  print(matriz.T)
    counter = 0
    for value in matriz.ravel():
        if value > 1:
            counter += 1

    print(counter)
