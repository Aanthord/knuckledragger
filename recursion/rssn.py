# knuckledragger/recursion/rssn.py

from abc import ABC, abstractmethod
from typing import Union
from knuckledragger.recursion.ftc import compute_density

class Shape(ABC):
    def __init__(self):
        self.metadata = {}

    @abstractmethod
    def evaluate(self, depth: int) -> float:
        pass

    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)

class AtomicShape(Shape):
    def __init__(self, value: bool):
        super().__init__()
        self.value = value

    def evaluate(self, depth: int) -> float:
        return 1.0 if self.value else 0.0

class AndShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return min(self.left.evaluate(depth), self.right.evaluate(depth))

class OrShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return max(self.left.evaluate(depth), self.right.evaluate(depth))

class NotShape(Shape):
    def __init__(self, shape: Shape):
        super().__init__()
        self.shape = shape

    def evaluate(self, depth: int) -> float:
        return 1.0 - self.shape.evaluate(depth)

class ImpShape(Shape):
    def __init__(self, premise: Shape, conclusion: Shape):
        super().__init__()
        self.premise = premise
        self.conclusion = conclusion

    def evaluate(self, depth: int) -> float:
        return 1.0 if self.premise.evaluate(depth) <= self.conclusion.evaluate(depth) else 0.0

class XorShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return abs(self.left.evaluate(depth) - self.right.evaluate(depth))

class EquivShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return 1.0 if abs(self.left.evaluate(depth) - self.right.evaluate(depth)) < 1e-6 else 0.0

class NandShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return 1.0 - min(self.left.evaluate(depth), self.right.evaluate(depth))

class NorShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return 1.0 - max(self.left.evaluate(depth), self.right.evaluate(depth))

class TriangleShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        return float(self.n ** self.n) if depth == 1 else TriangleShape(self.n).evaluate(depth - 1)

class SquareShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        val = self.n
        for _ in range(min(depth, self.n)):
            val = val ** val
        return float(val)

class CircleShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        val = self.n
        for _ in range(min(depth, self.n)):
            val = SquareShape(val).evaluate(1)
        return float(val)

class PentagonShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        d3 = compute_density(CircleShape(self.n), max_depth=3)
        effective_depth = int(depth * d3)
        val = self.n
        for _ in range(effective_depth):
            val = CircleShape(val).evaluate(1)
        return float(val)

class HexagonShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        d4 = compute_density(PentagonShape(self.n), max_depth=4)
        effective_depth = int(depth * d4)
        val = self.n
        for _ in range(effective_depth):
            val = PentagonShape(val).evaluate(1)
        return float(val)

class AetherShape(Shape):
    def __init__(self, n: int):
        super().__init__()
        self.n = n

    def evaluate(self, depth: int) -> float:
        val = self.n
        for k in range(1, depth + 1):
            val = TriangleShape(val).evaluate(1)
        return float(val)
