# knuckledragger/core/proof_state.py

from knuckledragger.core.goal import Goal
from knuckledragger.recursion.rssn import Shape

class ProofState:
    """
    Represents the evolving state of a recursive proof
    through transformations of logical shapes.
    """
    def __init__(self, goal: Goal):
        self.goal = goal
        self.history = [goal.shape]

    def apply_tactic(self, tactic):
        """
        Applies a tactic, transforming the shape and recording history.
        Tactic must return a new Shape.
        """
        new_shape = tactic.apply(self.goal)
        self.history.append(new_shape)
        self.goal.shape = new_shape

    def is_proven(self) -> bool:
        return self.goal.is_satisfied()

    def __repr__(self):
        return f"ProofState(goal={self.goal}, steps={len(self.history)})"
