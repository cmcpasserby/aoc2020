from typing import Dict, Callable, Tuple, List, Set


class Machine(object):
    def __init__(self, ins: List[Tuple[str, int]]):
        self.ptr: int = 0
        self.acc: int = 0
        self.visited: Set[int] = set()

        self.instructions = ins
        self.ops: Dict[str, Callable[[int], None]] = {
            "nop": self.op_nop,
            "acc": self.op_acc,
            "jmp": self.op_jmp,
        }

    def op_nop(self, _: int):
        self.ptr += 1

    def op_acc(self, x: int):
        self.acc += x
        self.ptr += 1

    def op_jmp(self, x: int):
        self.ptr += x

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.instructions)

    def __next__(self):
        if self.ptr >= len(self):
            raise StopIteration()

        if self.ptr in self.visited:
            raise ValueError("infinite loop detected")
        self.visited.add(self.ptr)

        op, arg = self.instructions[self.ptr]
        self.ops[op](arg)

        return self.acc


with open("inputs/day08.txt", 'r') as f:
    instructions = ((*line.split(maxsplit=1),) for line in f.read().splitlines())
    instructions = [(op, int(arg)) for op, arg in instructions]

    try:
        acc = 0
        for i in Machine(instructions[:]):
            acc = i
    except ValueError:
        print(f"part a: {acc}")

    for i, op, arg in ((i, *ins) for i, ins in enumerate(instructions) if ins[0] in ("nop", "jmp")):
        new_op = "nop" if op == "jmp" else "jmp"

        new_instructions = instructions[:]
        new_instructions[i] = (new_op, arg)

        try:
            acc = 0
            for a in Machine(new_instructions):
                acc = a
            print(f"part b: {acc}")
        except ValueError:
            pass
