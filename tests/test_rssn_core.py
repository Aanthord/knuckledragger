import pytest
from knuckledragger.recursion.rssn import (
    TriangleShape,
    SquareShape,
    CircleShape,
    PentagonShape,
    HexagonShape,
    AetherShape
)

@pytest.mark.parametrize("n,expected", [(2, 4), (3, 27), (4, 256)])
def test_triangle_evaluation_depth_1(n, expected):
    shape = TriangleShape(n)
    assert shape.evaluate(1) == expected

def test_triangle_evaluation_depth_2():
    shape = TriangleShape(2)
    result = shape.evaluate(2)
    assert result > 100, "Expected Triangle^2(2) to be > 100"

def test_triangle_density_range():
    shape = TriangleShape(3)
    d = shape.density(10)
    assert 0 < d <= 1

def test_square_evaluation_nested_triangle():
    shape = SquareShape(2)
    result = shape.evaluate(1)
    assert result == 256

def test_square_density_convergence():
    shape = SquareShape(3)
    d = shape.density(5)
    assert 0 < d < 1

def test_circle_growth_behavior():
    shape = CircleShape(2)
    val = shape.evaluate(1)
    assert val > 1e10

def test_circle_density_shape():
    shape = CircleShape(2)
    d = shape.density(4)
    assert isinstance(d, float)
    assert 0 < d < 1

def test_pentagon_hexagon_are_finite():
    pent = PentagonShape(2)
    hexg = HexagonShape(2)
    assert pent.evaluate(1) > 0
    assert hexg.evaluate(1) > 0

def test_aether_outputs_number():
    aether = AetherShape(2)
    val = aether.evaluate(1)
    assert isinstance(val, (int, float))

def test_invalid_depth_raises():
    shape = TriangleShape(2)
    with pytest.raises(ValueError):
        shape.evaluate(-1)

def test_zero_input_behaves():
    t = TriangleShape(1)
    assert t.evaluate(1) == 1
    assert t.density(3) == 1.0

def test_dense_limit_consistency():
    t = TriangleShape(5)
    d3 = t.density(3)
    d6 = t.density(6)
    assert abs(d6 - d3) < 0.1, "Expected density to converge slowly"
