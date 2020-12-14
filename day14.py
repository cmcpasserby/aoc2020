import re
from itertools import product, tee
from typing import Iterable

mem_re = re.compile(r"mem\[(\d+?)]")

_TEST_DATA = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def bits(n: int) -> Iterable[int]:
    while n:
        b = n & (~n+1)
        yield b
        n ^= b


def create_masks(mask: int) -> Iterable[int]:
    mask_bits = [*bits(mask)]
    mask_permutations = [i for i in product((0, 1), repeat=len(mask_bits))]

    for p in mask_permutations:
        value = 0
        for i, b in enumerate(p):
            if b == 1:
                value = value | mask_bits[i]

        yield value


with open("inputs/day14.txt", 'r') as f:
    inputs = [i for i in f.read().splitlines()]
    # inputs = [i for i in _TEST_DATA.splitlines()]

    def solve() -> tuple[int, int]:
        memory_a: dict[int, int] = {}
        memory_b: dict[int, int] = {}

        or_mask = 0x00
        and_mask = 0x00
        float_masks: list[int] = []

        for line in inputs:
            loc, val = line.split(" = ", maxsplit=2)

            if m := mem_re.match(loc):
                loc, val = int(m.group(1)), int(val)
                memory_a[loc] = (val & and_mask) | or_mask

                for m in float_masks:
                    memory_b[loc ^ m] = memory_a[loc]

            else:
                or_mask = int(val.replace("X", "0"), 2)
                and_mask = int(val.replace("X", "1"), 2)
                m = int(val.replace("1", "0").replace("X", "1"), 2)
                float_masks = [*create_masks(m)]

        return sum(memory_a.values()), sum(memory_b.values())


    a, b = solve()
    print(f"part a: {a}")
    print(f"part b: {b}")
