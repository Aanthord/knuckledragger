# knuckledragger/recursion/ftc.py

from knuckledragger.recursion.rssn import Shape
from typing import List

# Computes the density of a recursive shape across increasing depth levels
def compute_density(shape: Shape, max_depth: int = 10) -> float:
    total_density = 0.0
    for d in range(1, max_depth + 1):
        total_density += shape.evaluate(d)
    return total_density / max_depth

# Logs the density of a shape at each level
def compute_density_log(shape: Shape, max_depth: int = 10) -> List[float]:
    densities = []
    for d in range(1, max_depth + 1):
        val = shape.evaluate(d)
        densities.append(val)
    return densities

# Computes a weighted (harmonic decay) density average
def compute_weighted_density(shape: Shape, max_depth: int = 10) -> float:
    weighted_sum = 0.0
    weight_total = 0.0
    for d in range(1, max_depth + 1):
        weight = 1.0 / d
        weighted_sum += shape.evaluate(d) * weight
        weight_total += weight
    return weighted_sum / weight_total

# Checks if the density appears to be converging
def is_converging(shape: Shape, max_depth: int = 10, epsilon: float = 0.01) -> bool:
    values = compute_density_log(shape, max_depth)
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return all(diff < epsilon for diff in diffs[-3:])  # last 3 steps stable

# Checks if a shape is at critical (0.5) density
def is_critical(shape: Shape, depth: int = 10, threshold: float = 0.01) -> bool:
    density = compute_density(shape, depth)
    return abs(density - 0.5) < threshold

# Verifies implication holds across recursive depths
def implication_valid(premise: Shape, conclusion: Shape, depth: int = 10) -> bool:
    return all(premise.evaluate(d) <= conclusion.evaluate(d) for d in range(1, depth + 1))

# Detects oscillation or stability in recursive density (Fractal Closure)
def is_stable(shape: Shape, max_depth: int = 20, epsilon: float = 0.01) -> bool:
    values = compute_density_log(shape, max_depth)
    trend = [values[i] - values[i-1] for i in range(1, len(values))]
    oscillations = [t1 * t2 < 0 for t1, t2 in zip(trend[:-1], trend[1:])]
    return not any(oscillations[-3:]) and is_converging(shape, max_depth, epsilon)

# Example usage:
# from knuckledragger.recursion.rssn import *
# from knuckledragger.recursion.ftc import compute_density, is_critical, implication_valid
# s = AndShape(AtomicShape(True), NotShape(AtomicShape(False)))
# print(compute_density(s))
# print(is_critical(s))
# print(implication_valid(s, AtomicShape(True)))
