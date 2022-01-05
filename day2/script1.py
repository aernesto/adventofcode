# -*- coding: utf-8 -*-
from itertools import cycle

buffer_names = ['b0', 'b1', 'b2']
buffers = {nom: [] for nom in buffer_names}


def increment(buffer_name, valor):
    buffers[buffer_name].append(valor)


def output(fname):
    increase = 0

    with open(fname, 'rt') as fh:
        for i, line in enumerate(fh):
            number = int(line)
            if i < 2:
                if i == 0:
                    increment('b0', number)
                if i == 1:
                    increment('b0', number)
                    increment('b1', number)
                continue

            for buffer_name, buffer_value in buffers.items():
                buffer_length = len(buffer_value)

                if buffer_length == 3:
                    last = sum(buffer_value)
                    buffers[buffer_name] = []

                elif buffer_length == 2:
                    increment(buffer_name, number)
                else:
                    increment(buffer_name, number)
    return increase


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    print(output(filename))
