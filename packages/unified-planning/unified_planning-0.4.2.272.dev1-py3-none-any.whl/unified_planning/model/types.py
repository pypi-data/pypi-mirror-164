# Copyright 2021 AIPlan4EU project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""This module defines all the types."""

import unified_planning
from fractions import Fraction
from typing import Iterator, Optional, Dict, Tuple, cast
from unified_planning.exceptions import UPProblemDefinitionError, UPTypeError


class Type:
    """Basic class for representing a type."""

    def is_bool_type(self) -> bool:
        """Returns true iff is boolean type."""
        return False

    def is_user_type(self) -> bool:
        """Returns true iff is a user type."""
        return False

    def is_real_type(self) -> bool:
        """Returns true iff is real type."""
        return False

    def is_int_type(self) -> bool:
        """Returns true iff is integer type."""
        return False

    def is_time_type(self) -> bool:
        """Returns true iff is integer type."""
        return False

    def is_compatible(self, t_right: "Type") -> bool:
        """Returns True if the type t_right can be assigned to a fluent that which type is self."""
        return is_compatible_type(self, t_right)


class _BoolType(Type):
    """Represents the boolean type."""

    def __repr__(self) -> str:
        return "bool"

    def is_bool_type(self) -> bool:
        """Returns true iff is boolean type."""
        return True


class _TimeType(Type):
    """Represent the type for an absolute Time"""

    def __repr__(self) -> str:
        return "time"

    def is_time_type(self) -> bool:
        """Returns true iff is boolean type."""
        return True


class _UserType(Type):
    """Represents the user type."""

    def __init__(self, name: str, father: Optional[Type] = None):
        Type.__init__(self)
        self._name = name
        if father is not None and (not father.is_user_type()):
            raise UPTypeError("father field of a UserType must be a UserType.")
        self._father = father

    def __repr__(self) -> str:
        return (
            self._name
            if self._father is None
            else f"{self._name} - {cast(_UserType, self._father).name}"
        )

    @property
    def name(self) -> str:
        """Returns the type name."""
        return self._name

    @property
    def father(self) -> Optional[Type]:
        """Returns the type s father."""
        return self._father

    @property
    def ancestors(self) -> Iterator[Type]:
        """Returns all the ancestors of the given UserType, including itself."""
        type: Optional[Type] = self
        while type is not None:
            yield type
            type = cast(_UserType, type).father

    def is_user_type(self) -> bool:
        """Returns true iff is a user type."""
        return True

    def is_subtype(self, t: Type) -> bool:
        """Returns true iff is a subtype of the given type."""
        assert t.is_user_type()
        p: Optional[Type] = self
        while p is not None:
            if p == t:
                return True
            p = cast(_UserType, p).father
        return False


class _IntType(Type):
    def __init__(self, lower_bound: int = None, upper_bound: int = None):
        Type.__init__(self)
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound

    def __repr__(self) -> str:
        b = []
        if (not self.lower_bound is None) or (not self.upper_bound is None):
            b.append("[")
            b.append("-inf" if self.lower_bound is None else str(self.lower_bound))
            b.append(", ")
            b.append("inf" if self.upper_bound is None else str(self.upper_bound))
            b.append("]")
        return "integer" + "".join(b)

    @property
    def lower_bound(self) -> Optional[int]:
        return self._lower_bound

    @property
    def upper_bound(self) -> Optional[int]:
        return self._upper_bound

    def is_int_type(self) -> bool:
        return True


class _RealType(Type):
    def __init__(self, lower_bound: Fraction = None, upper_bound: Fraction = None):
        Type.__init__(self)
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound

    def __repr__(self) -> str:
        b = []
        if (not self.lower_bound is None) or (not self.upper_bound is None):
            b.append("[")
            b.append("-inf" if self.lower_bound is None else str(self.lower_bound))
            b.append(", ")
            b.append("inf" if self.upper_bound is None else str(self.upper_bound))
            b.append("]")
        return "real" + "".join(b)

    @property
    def lower_bound(self) -> Optional[Fraction]:
        return self._lower_bound

    @property
    def upper_bound(self) -> Optional[Fraction]:
        return self._upper_bound

    def is_real_type(self) -> bool:
        return True


BOOL = _BoolType()
TIME = _TimeType()


class TypeManager:
    def __init__(self):
        self._bool = BOOL
        self._ints: Dict[Tuple[Optional[int], Optional[int]], Type] = {}
        self._reals: Dict[Tuple[Optional[Fraction], Optional[Fraction]], Type] = {}
        self._user_types: Dict[Tuple[str, Optional[Type]], Type] = {}

    def has_type(self, type: Type) -> bool:
        if type.is_bool_type():
            return type == self._bool
        elif type.is_int_type():
            assert isinstance(type, _IntType)
            return self._ints.get((type.lower_bound, type.upper_bound), None) == type
        elif type.is_real_type():
            assert isinstance(type, _RealType)
            return self._reals.get((type.lower_bound, type.upper_bound), None) == type
        elif type.is_time_type():
            return type == TIME
        elif type.is_user_type():
            assert isinstance(type, _UserType)
            return self._user_types.get((type.name, type.father), None) == type
        else:
            raise NotImplementedError

    def BoolType(self) -> Type:
        return self._bool

    def IntType(self, lower_bound: int = None, upper_bound: int = None) -> Type:
        k = (lower_bound, upper_bound)
        if k in self._ints:
            return self._ints[k]
        else:
            it = _IntType(lower_bound, upper_bound)
            self._ints[k] = it
            return it

    def RealType(
        self, lower_bound: Fraction = None, upper_bound: Fraction = None
    ) -> Type:
        k = (lower_bound, upper_bound)
        if k in self._reals:
            return self._reals[k]
        else:
            rt = _RealType(lower_bound, upper_bound)
            self._reals[k] = rt
            return rt

    def UserType(self, name: str, father: Optional[Type] = None) -> Type:
        if (name, father) in self._user_types:
            return self._user_types[(name, father)]
        else:
            if father is not None:
                assert isinstance(father, _UserType)
                if any(
                    cast(_UserType, ancestor).name == name
                    for ancestor in father.ancestors
                ):
                    raise UPTypeError(
                        f"The name: {name} is already used. A UserType and one of his ancestors can not share the name."
                    )
            ut = _UserType(name, father)
            self._user_types[(name, father)] = ut
            return ut


def domain_size(
    objects_set: "unified_planning.model.mixins.ObjectsSetMixin",
    typename: "unified_planning.model.types.Type",
) -> int:
    """Returns the domain size of the given type."""
    if typename.is_bool_type():
        return 2
    elif typename.is_user_type():
        return len(list(objects_set.objects(typename)))
    elif typename.is_int_type():
        typename = cast(_IntType, typename)
        lb = typename.lower_bound
        ub = typename.upper_bound
        if lb is None or ub is None:
            raise UPProblemDefinitionError("Parameter not groundable!")
        return ub - lb
    else:
        raise UPProblemDefinitionError("Parameter not groundable!")


def domain_item(
    objects_set: "unified_planning.model.mixins.ObjectsSetMixin",
    typename: "unified_planning.model.types.Type",
    idx: int,
) -> "unified_planning.model.fnode.FNode":
    """Returns the ith domain item of the given type."""
    if typename.is_bool_type():
        return objects_set.env.expression_manager.Bool(idx == 0)
    elif typename.is_user_type():
        return objects_set.env.expression_manager.ObjectExp(
            list(objects_set.objects(typename))[idx]
        )
    elif typename.is_int_type():
        typename = cast(_IntType, typename)
        lb = typename.lower_bound
        ub = typename.upper_bound
        if lb is None or ub is None:
            raise UPProblemDefinitionError("Parameter not groundable!")
        return objects_set.env.expression_manager.Int(lb + idx)
    else:
        raise UPProblemDefinitionError("Parameter not groundable!")


def is_compatible_type(
    t_left: "Type",
    t_right: "Type",
) -> bool:
    """Returns True if the type t_right can be assigned to a typed up object that has type t_left.
    :param t_left: the target type for the assignment.
    :param t_right: the type of the element that wants to be assigned to the element of type t_left.
    :return: True if the element of type t_left can be assigned to the element of type t_right; False otherwise."""
    if t_left == t_right:
        return True
    if t_left.is_user_type() and t_right.is_user_type():
        assert isinstance(t_left, _UserType) and isinstance(t_right, _UserType)
        return t_right in t_left.ancestors
    if not (
        (t_left.is_int_type() and t_right.is_int_type())
        or (t_left.is_real_type() and t_right.is_real_type())
        or (t_left.is_real_type() and t_right.is_int_type())
    ):
        return False
    assert isinstance(t_left, _IntType) or isinstance(t_left, _RealType)
    assert isinstance(t_right, _IntType) or isinstance(t_right, _RealType)
    left_lower = -float("inf") if t_left.lower_bound is None else t_left.lower_bound
    left_upper = float("inf") if t_left.upper_bound is None else t_left.upper_bound
    right_lower = -float("inf") if t_right.lower_bound is None else t_right.lower_bound
    right_upper = float("inf") if t_right.upper_bound is None else t_right.upper_bound
    if right_upper < left_lower or right_lower > left_upper:
        return False
    else:
        return True
