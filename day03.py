from math import prod


with open("inputs/day03.txt", 'r') as f:
    data = [[i == "#" for i in r.strip()] for r in f]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    x_len = len(data[0])

    def trees_on_slope(dx: int, dy: int) -> int:
        return sum(row[i * dx % x_len] for i, row in enumerate(data[::dy]))

    part_a = trees_on_slope(3, 1)
    print(f"part a: {part_a}")

    part_b = prod(trees_on_slope(*i) for i in slopes)
    print(f"part b: {part_b}")
