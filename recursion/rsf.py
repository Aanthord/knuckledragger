# knuckledragger/recursion/rsf.py

from knuckledragger.recursion.rssn import Shape, AndShape, OrShape, NotShape, AtomicShape
from typing import Callable

# Recursive generation rule: takes depth and returns a Shape
def generate_structure(base: Shape, rule: Callable[[Shape, int], Shape], max_depth: int = 5) -> Shape:
    shape = base
    for depth in range(1, max_depth + 1):
        shape = rule(shape, depth)
    return shape

# Example generation rules
def alternate_and_or(shape: Shape, depth: int) -> Shape:
    if depth % 2 == 0:
        return AndShape(shape, AtomicShape(depth % 3 == 0))
    else:
        return OrShape(shape, AtomicShape(depth % 2 == 1))

def invert_every_n(shape: Shape, depth: int, n: int = 3) -> Shape:
    return NotShape(shape) if depth % n == 0 else shape

# Composite generator rule using both alternation and inversion
def composite_rule(shape: Shape, depth: int) -> Shape:
    shaped = alternate_and_or(shape, depth)
    return invert_every_n(shaped, depth)

# Example usage:
# from knuckledragger.recursion.rsf import *
# s = generate_structure(AtomicShape(True), composite_rule, max_depth=5)
# print(s.evaluate(5))
