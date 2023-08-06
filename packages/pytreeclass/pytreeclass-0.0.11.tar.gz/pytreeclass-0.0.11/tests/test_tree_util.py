import jax.numpy as jnp
import pytest

import pytreeclass as pytc
from pytreeclass.src.decorator import ImmutableInstanceError
from pytreeclass.src.tree_util import (
    _node_count_and_size,
    is_treeclass,
    is_treeclass_leaf,
    mutableContext,
)


@pytc.treeclass
class Test:
    a: int = 10


a = Test()
b = (1, "s", 1.0, [2, 3])


@pytc.treeclass
class Test2:
    a: int = 1
    b: Test = Test()


def test_is_treeclass():
    assert is_treeclass(a) is True
    assert all(is_treeclass(bi) for bi in b) is False


def test_is_treeclass_leaf():
    assert is_treeclass_leaf(a) is True
    assert all(is_treeclass_leaf(bi) for bi in b) is False
    assert is_treeclass_leaf(Test2()) is False
    assert is_treeclass_leaf(Test2().b) is True


def test__node_count_and_size():
    @pytc.treeclass
    class Test:
        a: jnp.ndarray = jnp.array([1.0, 2.0, 3.0])
        b: int = 1

    t = Test()
    assert _node_count_and_size(t.b) == (complex(0, 1), complex(0, 28))
    assert _node_count_and_size(t.a) == (complex(3, 0), complex(12, 0))

    assert _node_count_and_size(jnp.array([1, 2, 3, 4, 5])) == (
        complex(0, 5),
        complex(0, 20),
    )
    assert _node_count_and_size(3.0) == (complex(1), complex(24))

    @pytc.treeclass
    class x:
        a: int = 1
        b: int = 2

    assert hash(x())

    xx = x()
    # xx.cc = 1
    # assert xx.cc == 1
    xx = xx.at[...].freeze()

    with pytest.raises(ImmutableInstanceError):
        xx.test = 1

    assert _node_count_and_size("string") == (complex(0, 0), complex(0, 0))


def test_mutable_context():
    @pytc.treeclass
    class Test:
        x: int

        def __init__(self, x):
            self.x = x

        def __call__(self, x):
            return self.x + x

    t = Test(1)

    with mutableContext(t):
        t.a = 12

    assert getattr(t, "a") == 12

    with pytest.raises(ImmutableInstanceError):
        t.a = 100

    with pytest.raises(AssertionError):
        with mutableContext(1):
            pass
