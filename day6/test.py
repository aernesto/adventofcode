# -*- coding: utf-8 -*-
from script2 import algo as algoritmo
from time import perf_counter


def test1():
    return algoritmo('test.txt', 18) == 26


def test2():
    return algoritmo('test.txt', 80) == 5934


def test2bis():
    return algoritmo('test.txt', 120) > 0


def test3():
    return algoritmo('real.txt', 80) == 380612


def test3bis():
    return algoritmo('real.txt', 120) > 0


if __name__ == "__main__":
    tic = perf_counter()
    assert test1()
    print(f'test 1 passed in {perf_counter() - tic:.2f} seconds')

    tic = perf_counter()
    assert test2()
    print(f'test 2 passed in {perf_counter() - tic:.2f} seconds')

    tic = perf_counter()
    assert test2bis()
    print(f'test 2 bis passed in {perf_counter() - tic:.2f} seconds')

    tic = perf_counter()
    assert test3()
    print(f'test 3 passed in {perf_counter() - tic:.2f} seconds')

    tic = perf_counter()
    assert test3bis()
    print(f'test 3 bis passed in {perf_counter() - tic:.2f} seconds')
