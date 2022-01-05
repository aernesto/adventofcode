# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    x, y = 0, 0
    with open(sys.argv[1], 'rt') as fh:
        for line in fh:
            word, number = line.split()
            number = int(number)
            #  print(word, number)
            if word == 'forward':
                x += number
            if word == 'up':
                y += number
            if word == 'down':
                y -= number
    print(x, y, x * y)
