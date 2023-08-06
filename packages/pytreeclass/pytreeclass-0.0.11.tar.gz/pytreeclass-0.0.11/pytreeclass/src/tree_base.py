from __future__ import annotations

from dataclasses import MISSING, field
from typing import Any

import jax.numpy as jnp
import jax.tree_util as jtu

from pytreeclass.src.tree_util import is_treeclass, static_value
from pytreeclass.src.tree_viz import (
    tree_box,
    tree_diagram,
    tree_repr,
    tree_str,
    tree_summary,
)

PyTree = Any


class fieldDict(dict):
    # dict will throw
    # `ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()``
    # while this implementation will not.
    # relevant issue : https://github.com/google/jax/issues/11089
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class treeBase:
    def __new__(cls, *args, **kwargs):
        # register dataclass fields to instance dict
        # otherwise will raise undeclared error for non defined
        # init classes.
        obj = super().__new__(cls)

        for field_item in cls.__dataclass_fields__.values():
            if field_item.default is not MISSING:
                object.__setattr__(obj, field_item.name, field_item.default)
        return obj

    @property
    def frozen(self) -> bool:
        """Show treeclass frozen status.

        Returns:
            Frozen state boolean.
        """
        return True if hasattr(self, "__frozen_fields__") else False

    def tree_flatten(self):
        """Flatten rule for `jax.tree_flatten`

        Returns:
            Tuple of dynamic values and (dynamic keys,static dict)
        """
        dynamic, static = self.__treeclass_structure__

        if self.frozen:
            return (), ((), {"__frozen_fields__": (dynamic, static)})

        else:
            return dynamic.values(), (dynamic.keys(), static)

    @classmethod
    def tree_unflatten(cls, treedef, children):
        """Unflatten rule for `jax.tree_unflatten`

        Args:
            treedef:
                Pytree definition
                includes Dynamic nodes keys , static dictionary and frozen state
            children:
                Dynamic nodes values

        Returns:
            New class instance
        """

        new_cls = cls.__new__(cls)

        tree_fields = treedef[1].get("__frozen_fields__", None)

        if tree_fields is not None:
            object.__setattr__(new_cls, "__frozen_fields__", tree_fields)
            dynamic, static = tree_fields
            attrs = {**dynamic, **static}

        else:

            dynamic_vals, dynamic_keys = children, treedef[0]
            static_keys, static_vals = treedef[1].keys(), treedef[1].values()

            attrs = dict(
                zip(
                    (*dynamic_keys, *static_keys),
                    (*dynamic_vals, *static_vals),
                )
            )

        for k, v in attrs.items():
            object.__setattr__(new_cls, k, v)
        return new_cls

    def __hash__(self):
        return hash(tuple(*jtu.tree_flatten(self)))

    def asdict(self) -> dict[str, Any]:
        """Dictionary representation of dataclass_fields"""
        dynamic, static = self.__treeclass_structure__
        static.pop("__treeclass_fields__", None)
        static.pop("__immutable_treeclass__", None)
        return {
            **dynamic,
            **jtu.tree_map(
                lambda x: x.value if isinstance(x, static_value) else x, dict(static)
            ),
        }

    def register_node(
        self, node: Any, *, name: str, static: bool = False, repr: bool = True
    ) -> Any:
        """Add item to dataclass fields to bee seen by jax computations"""
        all_fields = {
            **self.__dataclass_fields__,
            **self.__dict__.get("__treeclass_fields__", {}),
        }

        if name not in all_fields:
            # create field
            field_value = field(repr=repr, metadata={"static": static})

            object.__setattr__(field_value, "name", name)
            object.__setattr__(field_value, "type", type(node))

            # register it to class
            __treeclass_fields__ = self.__dict__.get("__treeclass_fields__", {})
            __treeclass_fields__[name] = field_value
            object.__setattr__(self, "__treeclass_fields__", __treeclass_fields__)
            object.__setattr__(self, name, node)

        return self.__dict__[name]

    def __repr__(self):
        return tree_repr(self)

    def __str__(self):
        return tree_str(self)

    def summary(self, array: jnp.ndarray = None) -> str:
        return tree_summary(self, array)

    def tree_diagram(self) -> str:
        return tree_diagram(self)

    def tree_box(self, array: jnp.ndarray = None) -> str:
        return tree_box(self, array)

    def __generate_tree_fields__(self) -> tuple[dict[str, Any], dict[str, Any]]:
        dynamic, static = fieldDict(), fieldDict()
        # register other variables defined in other context
        # if their value is an instance of treeclass
        # to avoid redefining them as dataclass fields.

        # register *all* dataclass fields
        treeclass_fields = self.__dict__.get("__treeclass_fields__", {})

        all_fields = {**self.__dataclass_fields__, **treeclass_fields}

        for fi in all_fields.values():
            # field value is defined in class dict
            if fi.name in self.__dict__:
                value = self.__dict__[fi.name]
            else:
                # the user did not declare a variable defined in field
                raise ValueError(f"field={fi.name} is not declared.")

            excluded_by_meta = fi.metadata.get("static", False)
            excluded_by_type = isinstance(value, static_value)

            if excluded_by_type or excluded_by_meta:
                static[fi.name] = value

            else:
                dynamic[fi.name] = value

        static["__treeclass_fields__"] = treeclass_fields
        static["__immutable_treeclass__"] = self.__dict__.get(
            "__immutable_treeclass__", False
        )

        return (dynamic, static)


class explicitTreeBase:
    """ "Register  dataclass fields only"""

    @property
    def __treeclass_structure__(self):
        """Computes the dynamic and static fields.

        Returns:
            Pair of dynamic and static dictionaries.
        """
        if self.__dict__.get("__frozen_fields__", None) is not None:
            return self.__frozen_fields__
        else:
            return self.__generate_tree_fields__()

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)


class implicitTreeBase:
    """Register dataclass fields and treeclass instance variables"""

    def __register_treeclass_instance_variables__(self) -> None:

        __treeclass_fields__ = {}

        for var_name, var_value in self.__dict__.items():
            # check if a variable in self.__dict__ is treeclass
            # that is not defined in fields
            if (
                isinstance(var_name, str)
                and is_treeclass(var_value)
                and var_name not in self.__dataclass_fields__
            ):

                field_value = field()

                object.__setattr__(field_value, "name", var_name)
                object.__setattr__(field_value, "type", type(var_value))

                # register it to class
                __treeclass_fields__.update({var_name: field_value})

        if len(__treeclass_fields__) > 0:
            object.__setattr__(self, "__treeclass_fields__", __treeclass_fields__)

    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)
        self.__register_treeclass_instance_variables__()

    @property
    def __treeclass_structure__(self):
        """Computes the dynamic and static fields.

        Returns:
            Pair of dynamic and static dictionaries.
        """
        if self.__dict__.get("__frozen_fields__", None) is not None:
            return self.__frozen_fields__

        else:
            return self.__generate_tree_fields__()
