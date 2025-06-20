# knuckledragger/rssn/interpreter.py

from knuckledragger.recursion.rssn import *

SYMBOL_MAP = {
    'Atomic': AtomicShape,
    'And': AndShape,
    'Or': OrShape,
    'Not': NotShape,
    'Imp': ImpShape,
    'Xor': XorShape,
    'Equiv': EquivShape,
    'Nand': NandShape,
    'Nor': NorShape,
    'Triangle': TriangleShape,
    'Square': SquareShape,
    'Circle': CircleShape,
    'Pentagon': PentagonShape,
    'Hexagon': HexagonShape,
    'Aether': AetherShape,
}

def parse_expression(expr: str) -> Shape:
    """
    Recursively parses an RSSN symbolic expression like:
    Pentagon(2), Or(Atomic(True), Not(Atomic(False)))
    """
    expr = expr.strip()
    if expr.startswith('Atomic'):
        val = expr[expr.find('(')+1:-1].strip()
        return AtomicShape(val == 'True')

    for key in SYMBOL_MAP:
        if expr.startswith(key):
            args_str = expr[len(key)+1:-1]
            args = split_args(args_str)
            parsed_args = [parse_expression(arg) if not arg.isnumeric() else int(arg) for arg in args]
            return SYMBOL_MAP[key](*parsed_args)

    raise ValueError(f"Unrecognized expression: {expr}")

def split_args(arg_str: str) -> list:
    """
    Handles nested function argument splitting, e.g.
    Or(Atomic(True), Not(Atomic(False))) → ['Atomic(True)', 'Not(Atomic(False))']
    """
    args = []
    depth = 0
    current = []
    for char in arg_str:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if char == ',' and depth == 0:
            args.append(''.join(current).strip())
            current = []
        else:
            current.append(char)
    if current:
        args.append(''.join(current).strip())
    return args

# Example usage:
# shape = parse_expression("Pentagon(2)")
# print(shape.evaluate(5))
