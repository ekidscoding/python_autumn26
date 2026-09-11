# NamedTuple

bad_list: list[str | int | bool] = [
    "John",
    38,
    True,
    "Jane",
    35,
    False,
    "Sarah",
    30,
    True,
]

from typing import NamedTuple

# ruff: disable[UP014]

# This creates a new NamedTuple type named "Human" assigned to the variable Human
Human = NamedTuple("Human", [("Name", str), ("Age", int), ("kids", bool)])

good_list: list[Human] = [
    Human("John", 38, True),
    Human("Jane", 35, False),
    Human("Sarah", 30, True),
]


# Advanced optional syntax

type PersonalFlag = bool | None

HumanOptional = NamedTuple(
    "Human", [("Name", str), ("Age", int), ("kids", PersonalFlag)]
)

good_list_optional: list[Human] = [
    Human("John", 38, True),
    Human("Jane", 35, False),
    Human("Sarah", 30),
]
