# knuckledragger/recursion/rssn.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def evaluate(self, depth: int) -> float:
        pass

class AtomicShape(Shape):
    def __init__(self, value: bool):
        self.value = value

    def evaluate(self, depth: int) -> float:
        return 1.0 if self.value else 0.0

class AndShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return min(self.left.evaluate(depth), self.right.evaluate(depth))

class OrShape(Shape):
    def __init__(self, left: Shape, right: Shape):
        self.left = left
        self.right = right

    def evaluate(self, depth: int) -> float:
        return max(self.left.evaluate(depth), self.right.evaluate(depth))

class NotShape(Shape):
    def __init__(self, shape: Shape):
        self.shape = shape

    def evaluate(self, depth: int) -> float:
        return 1.0 - self.shape.evaluate(depth)

class ImpShape(Shape):
    def __init__(self, premise: Shape, conclusion: Shape):
        self.premise = premise
        self.conclusion = conclusion

    def evaluate(self, depth: int) -> float:
        return 1.0 if self.premise.evaluate(depth) <= self.conclusion.evaluate(depth) else 0.0
