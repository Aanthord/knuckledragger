# knuckledragger/recursion/rsf.py

from knuckledragger.recursion.rssn import (
    Shape, AtomicShape, AndShape, OrShape, NotShape, ImpShape, XorShape, EquivShape,
    NandShape, NorShape, TriangleShape, SquareShape, CircleShape,
    PentagonShape, HexagonShape, AetherShape
)
from typing import List, Callable, Any, Dict

class RecursiveSet:
    def __init__(self, generator: Callable[[int], List[Any]]):
        self.generator = generator

    def generate_members(self, depth: int) -> List[Any]:
        return self.generator(depth)

    def contains(self, x: Any, depth: int = 10) -> bool:
        return x in self.generate_members(depth)

def generate_structure(shape: Shape, depth: int = 3) -> List[Any]:
    return [shape.evaluate(i) for i in range(1, depth + 1)]

class RSFSchema:
    def __init__(self, shape: Shape):
        self.shape = shape
        self.schema = generate_structure(shape, depth=4)

    def describe(self) -> str:
        return f"RSFSchema[{self.shape.__class__.__name__} → {self.schema}]"

# Rule templates for logical and structural interpretation

def truth_static(n: int) -> List[bool]:
    return [True for _ in range(n)]

def truth_alternating(n: int) -> List[bool]:
    return [i % 2 == 0 for i in range(n)]

def truth_inverted(n: int) -> List[bool]:
    return [not (i % 2 == 0) for i in range(n)]

def implication_chain(n: int) -> List[str]:
    return ["p → q" if i % 2 == 0 else "q → p" for i in range(n)]

def xor_balance(n: int) -> List[bool]:
    return [(i % 3) == 1 for i in range(n)]

def nand_or_gate(n: int) -> List[str]:
    return ["NAND" if i % 2 == 0 else "NOR" for i in range(n)]

def exponential_growth(n: int) -> List[int]:
    return [2 ** i for i in range(n)]

def triangular_growth(n: int) -> List[int]:
    return [i * (i + 1) // 2 for i in range(n)]

def square_compound(n: int) -> List[int]:
    return [sum([j ** 2 for j in range(1, i + 1)]) for i in range(n)]

def circle_nested(n: int) -> List[int]:
    return [sum([2 ** (j ** 2) for j in range(1, i + 1)]) for i in range(n)]

def pentagon_structured(n: int) -> List[str]:
    return ["META" if i % 2 == 0 else "SELF" for i in range(n)]

def hexagon_fusion(n: int) -> List[str]:
    return ["CONVERGE" if i % 3 == 0 else "DIVERGE" for i in range(n)]

def aether_field(n: int) -> List[str]:
    return ["∞" for _ in range(n)]

def describe_structure(shape: Shape, depth: int = 3) -> str:
    trace = generate_structure(shape, depth)
    return f"Trace[{shape.__class__.__name__} @ depth {depth}]: {trace}"

# Full RSF rule registry for programmatic access

RSF_RULES: Dict[str, Callable[[int], List[Any]]] = {
    'Atomic': truth_static,
    'And': truth_static,
    'Or': truth_alternating,
    'Not': truth_inverted,
    'Imp': implication_chain,
    'Xor': xor_balance,
    'Equiv': truth_static,
    'Nand': nand_or_gate,
    'Nor': nand_or_gate,
    'Triangle': exponential_growth,
    'Square': square_compound,
    'Circle': circle_nested,
    'Pentagon': pentagon_structured,
    'Hexagon': hexagon_fusion,
    'Aether': aether_field,
}
