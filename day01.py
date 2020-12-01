from itertools import combinations
from math import prod
from typing import Iterable


def get_answer(d: Iterable[int], r: int) -> int:
    return next(prod(d) for d in combinations(d, r) if sum(d) == 2020)


with open("inputs/day01.txt", 'r') as f:
    data = [int(i) for i in f.readlines()]
    print(f"part a: {get_answer(data, 2)}")
    print(f"part b: {get_answer(data, 3)}")
