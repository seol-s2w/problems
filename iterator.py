from itertools import combinations
from typing import Iterable


def distinct(iter: Iterable):
    elements = set()
    for e in iter:
        if e not in elements:
            elements.add(e)
            yield e


def subsets(iter: Iterable, minsize=0):
    maxsize = len(iter) + 1
    for size in range(minsize, maxsize):
        yield from combinations(iter, size)


def problem1():
    print("distinct: ", end="")
    print(list(distinct((i ** 2 % 10 for i in range(1000)))))


def problem2():
    print("subsets: ", end="")
    print(["".join(s) for s in subsets("abcd", 2)])


if __name__ == "__main__":
    problem1()
    problem2()
