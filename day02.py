import re

r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def part_a_test(low: str, high: str, char: str, pw: str) -> bool:
    return int(low) <= pw.count(char) <= int(high)


def part_b_test(low: str, high: str, char: str, pw: str) -> bool:
    return (pw[int(low)-1] == char) ^ (pw[int(high)-1] == char)


with open("inputs/day02.txt", 'r') as f:
    data = [g := r.match(item).groups() for item in f]

    part_a = sum(1 for i in data if part_a_test(*i))
    print(f"part_a: {part_a}")

    part_b = sum(1 for i in data if part_b_test(*i))
    print(f"part_b: {part_b}")
