from typing import List
from itertools import permutations
from math import prod


def get_answer(data: List[int], r: int):
    return next(prod(d) for d in permutations(data, r) if sum(d) == 2020)


def main():
    with open("inputs/day01.txt", 'r') as f:
        data = [int(i) for i in f.readlines()]
        print(f"part a: {get_answer(data, 2)}")
        print(f"part b: {get_answer(data, 3)}")


if __name__ == '__main__':
    main()
