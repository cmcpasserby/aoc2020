from itertools import tee
from collections import Counter
from typing import Iterator, Iterable


def pairs(iterable: Iterable[int]) -> Iterator[tuple[int, int]]:
    a, b = tee(iterable, 2)
    next(b)
    return zip(a, b)


with open("inputs/day10.txt", 'r') as f:
    adapters = sorted(int(line) for line in f.read().splitlines())
    adapters.append(adapters[-1] + 3)

    def part_a() -> int:
        diffs = Counter(b - a for a, b in pairs(adapters))
        diffs[adapters[0]] += 1  # wall
        return diffs[1] * diffs[3]

    print(f"part a: {part_a()}")

