# knuckledragger/core/goal.py

from knuckledragger.recursion.rssn import Shape

class Goal:
    """
    A recursive logic goal, defined not by Boolean satisfaction,
    but by achieving sufficient truth-density.
    """
    def __init__(self, shape: Shape, threshold: float = 0.95, max_depth: int = 10):
        self.shape = shape
        self.threshold = threshold
        self.max_depth = max_depth

    def is_satisfied(self) -> bool:
        from knuckledragger.recursion.ftc import compute_density
        density = compute_density(self.shape, self.max_depth)
        return density >= self.threshold

    def __repr__(self):
        return f"Goal(shape={self.shape}, threshold={self.threshold})"
