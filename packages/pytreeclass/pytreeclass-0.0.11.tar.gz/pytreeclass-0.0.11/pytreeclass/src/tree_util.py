from __future__ import annotations

import dataclasses
import sys
from dataclasses import field
from typing import Any

import jax
import jax.numpy as jnp
import jax.tree_util as jtu
import numpy as np

from pytreeclass.src.tree_viz_util import _format_node_repr, _format_node_str

PyTree = Any


class static_value:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"*{_format_node_repr(self.value,0)}"

    def __str__(self):
        return f"*{_format_node_str(self.value,0)}"


def static_field(**kwargs):
    """ignore from pytree computations"""
    return field(**{**kwargs, **{"metadata": {"static": True}}})


def is_treeclass(tree):
    """check if a class is treeclass"""
    return hasattr(tree, "__treeclass_structure__")


def is_treeclass_leaf_bool(node):
    """assert if treeclass leaf is boolean (for boolen indexing)"""
    if isinstance(node, jnp.ndarray):
        return node.dtype == "bool"
    else:
        return isinstance(node, bool)


def is_treeclass_leaf(tree):
    """assert if a node is treeclass leaf"""
    if is_treeclass(tree):

        all_fields = {
            **tree.__dataclass_fields__,
            **tree.__dict__.get("__treeclass_fields__", {}),
        }

        return is_treeclass(tree) and not any(
            [is_treeclass(tree.__dict__[fi.name]) for fi in all_fields.values()]
        )
    else:
        return False


def is_treeclass_non_leaf(tree):
    return is_treeclass(tree) and not is_treeclass_leaf(tree)


def is_treeclass_equal(lhs, rhs):
    """Assert if two treeclasses are equal"""
    lhs_leaves, lhs_treedef = jtu.tree_flatten(lhs)
    rhs_leaves, rhs_treedef = jtu.tree_flatten(rhs)

    def is_node_equal(lhs_node, rhs_node):
        if isinstance(lhs_node, jnp.ndarray) and isinstance(rhs_node, jnp.ndarray):
            return jnp.array_equal(lhs_node, rhs_node)
        else:
            return lhs_node == rhs_node

    return (lhs_treedef == rhs_treedef) and all(
        [is_node_equal(lhs_leaves[i], rhs_leaves[i]) for i in range(len(lhs_leaves))]
    )


def is_excluded(field_item: dataclasses.field, node_item: Any) -> bool:
    """Check if a field is excluded

    Returns:
        bool: boolean if the field should be excluded or not.
    """
    excluded_by_meta = field_item.metadata.get("static", False)
    excluded_by_type = isinstance(node_item, static_value)
    return excluded_by_meta or excluded_by_type


def sequential_tree_shape_eval(tree, array):
    """Evaluate shape propagation of assumed sequential modules"""

    # all dynamic/static leaves
    all_leaves = (
        *tree.__treeclass_structure__[0].values(),
        *tree.__treeclass_structure__[1].values(),
    )
    leaves = [leaf for leaf in all_leaves if is_treeclass(leaf)]

    shape = [jax.eval_shape(lambda x: x, array)]
    for leave in leaves:
        shape += [jax.eval_shape(leave, shape[-1])]
    return shape


def tree_copy(tree):
    return jtu.tree_unflatten(*jtu.tree_flatten(tree)[::-1])


def _node_count_and_size(node: Any) -> tuple[complex, complex]:
    """Calculate number and size of `trainable` and `non-trainable` parameters

    Args:
        node (Any): treeclass node

    Returns:
        complex: Complex number of (inexact, non-exact) parameters for count/size
    """

    node = node.value if isinstance(node, static_value) else node

    if isinstance(node, (jnp.ndarray, np.ndarray)):
        # inexact(trainable) array
        if jnp.issubdtype(node, jnp.inexact):
            count = complex(int(jnp.array(node.shape).prod()), 0)
            size = complex(int(node.nbytes), 0)

        # exact paramter
        else:
            count = complex(0, int(jnp.array(node.shape).prod()))
            size = complex(0, int(node.nbytes))

    # inexact non-array (array_like)
    elif isinstance(node, (float, complex)):
        count = complex(1, 0)
        size = complex(sys.getsizeof(node), 0)

    # exact non-array
    elif isinstance(node, int):
        count = complex(0, 1)
        size = complex(0, sys.getsizeof(node))

    # exclude others
    else:
        count = complex(0, 0)
        size = complex(0, 0)

    return (count, size)


def _reduce_count_and_size(leaf):
    """reduce params count and params size of a tree of leaves"""

    def reduce_func(acc, node):
        lhs_count, lhs_size = acc
        rhs_count, rhs_size = _node_count_and_size(node)
        return (lhs_count + rhs_count, lhs_size + rhs_size)

    return jtu.tree_reduce(reduce_func, leaf, (complex(0, 0), complex(0, 0)))


def _freeze_nodes(tree):
    """inplace freezing"""
    if is_treeclass(tree):
        object.__setattr__(tree, "__frozen_fields__", None)

        all_fields = {
            **tree.__dataclass_fields__,
            **tree.__dict__.get("__treeclass_fields__", {}),
        }

        for kw, leaf in all_fields.items():
            _freeze_nodes(tree.__dict__[kw])
    return tree


def _unfreeze_nodes(tree):
    """inplace unfreezing"""
    if is_treeclass(tree):
        if hasattr(tree, "__frozen_fields__"):
            object.__delattr__(tree, "__frozen_fields__")

        all_fields = {
            **tree.__dataclass_fields__,
            **tree.__dict__.get("__treeclass_fields__", {}),
        }

        for kw, leaf in all_fields.items():
            _unfreeze_nodes(tree.__dict__[kw])
    return tree


class mutableContext:
    """Allow mutable behvior within this context"""

    def __init__(self, instance):
        assert is_treeclass(instance), "instance must be a treeclass"
        self.instance = instance

    def __enter__(self):
        object.__setattr__(self.instance, "__immutable_treeclass__", False)

    def __exit__(self, type_, value, traceback):
        object.__setattr__(self.instance, "__immutable_treeclass__", True)
