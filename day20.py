from math import prod

TileData = tuple[tuple[bool, ...], ...]


class Tile(object):
    def __init__(self, index: int, data: TileData):
        self.index: int = index
        self.data: TileData = data
        self.connections: set[Tile] = set()

    def __str__(self) -> str:
        result = []
        for x in self.data:
            item = "".join("#" if y else "." for y in x)
            result.append(item)
        return "\n".join(result)

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.index == other.index
        return False

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.index)

    def flip_h(self):
        self.data = tuple(i[::-1] for i in self.data)

    def flip_v(self):
        self.data = self.data[::-1]

    def rotate_cw(self):
        self.data = tuple(zip(*self.data[::-1]))

    def rotate_ccw(self):
        self.data = tuple(zip(*self.data))[::-1]

    @property
    def top(self) -> tuple[bool]:
        return self.data[0]

    @property
    def bottom(self) -> tuple[bool]:
        return self.data[-1]

    @property
    def left(self) -> tuple[bool]:
        return tuple(line[0] for line in self.data)

    @property
    def right(self) -> tuple[bool]:
        return tuple(line[-1] for line in self.data)

    @property
    def edges(self) -> list[tuple[bool]]:
        return [self.top, self.bottom, self.left, self.right]


def parse_inputs() -> dict[int, Tile]:
    with open("inputs/day20.txt", 'r') as f:

        tiles: dict[int, Tile] = {}

        for tile in f.read().split("\n\n"):
            lines = tile.splitlines()
            key = int(lines[0].split(maxsplit=1)[1].replace(':', ''))
            data = tuple(tuple(c == '#' for c in line) for line in lines[1:])
            tiles[key] = Tile(key, data)

        return tiles


def can_match(lhs: Tile, rhs: Tile) -> bool:
    for start_edge in lhs.edges:
        other = rhs

        if start_edge in rhs.edges:
            return True

        for _ in range(4):
            other.rotate_cw()
            if start_edge in other.edges:
                return True

        # TODO: might need to nest these checks
        for _ in range(2):
            other.flip_h()
            if start_edge in other.edges:
                return True

        for _ in range(2):
            other.flip_v()
            if start_edge in other.edges:
                return True


def find_connections(tiles: dict[int, Tile]):
    for outer_i, outer_t in tiles.items():
        for inner_i, inner_t in tiles.items():
            if outer_i == inner_i:
                continue

            if can_match(outer_t, inner_t):
                outer_t.connections.add(inner_t)


def solve() -> tuple[int, int]:
    tiles = parse_inputs()
    find_connections(tiles)
    return prod(i.index for i in tiles.values() if len(i.connections) == 2), 0


a, b = solve()
print(f"part a: {a}")
print(f"part b: {b}")
