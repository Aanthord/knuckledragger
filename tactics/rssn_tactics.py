# knuckledragger/tactics/rssn_tactic.py

from knuckledragger.recursion.ftc import compute_density, is_critical, is_converging
from knuckledragger.recursion.rssn import Shape
from knuckledragger.rssn.interpreter import parse_expression
from knuckledragger.core.goal import Goal
from knuckledragger.core.tactic import Tactic

class RSSNEvalTactic(Tactic):
    def __init__(self, expr: str, max_depth: int = 10):
        self.expr = expr
        self.max_depth = max_depth

    def apply(self, goal: Goal):
        shape = parse_expression(self.expr)
        density = compute_density(shape, self.max_depth)
        summary = {
            'expr': self.expr,
            'density': density,
            'is_critical': is_critical(shape, self.max_depth),
            'is_converging': is_converging(shape, self.max_depth),
        }
        return summary

# Example usage:
# tactic = RSSNEvalTactic("Pentagon(2)")
# result = tactic.apply(None)
# print(result)
