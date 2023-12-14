import pytest

from fun_pckg.fun import foo
from fun_pckg.fun import bar


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1, 2, 3),
        (11, 2, 13),
        (1, 22, 23),
        (0, 2, 2),
        (-11, 2, -9),
    ],
)
def test_foo(x, y, result):
    assert foo(x, y) == result


@pytest.mark.parametrize(
    "x,y,result",
    [
        (1, 2, -1),
        (11, 2, 9),
        (1, 22, -21),
        (0, 2, -2),
        (-11, 2, -13),
    ],
)
def test_bar(x, y, result):
    assert bar(x, y) == result
