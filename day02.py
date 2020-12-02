import re

r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def test_pw(matches: re.Match) -> bool:
    low, high, char, pw = matches.groups()
    return int(low) <= pw.count(char) <= int(high)


with open("inputs/day02.txt", 'r') as f:
    data = [r.match(item) for item in f.readlines()]

    part_a = sum(1 for i in data if test_pw(i))
    print(f"part_a: {part_a}")
