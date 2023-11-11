from typing import Callable
from enum import Enum, auto

from ._key_extractor import default_dict_key_extractor
from ._basic import list_to_dict


class DifferenceType(Enum):
    TYPE = auto()
    MISSING = auto()
    NOT_EQUAL = auto()

class DifferencePointer(Enum):
    A = auto()
    B = auto()

class Difference:

    __slots__ = (
        "key", "type", "pointer", "value_a", "value_b"
    )

    def __init__(
        self,
        key: list[str],
        type: DifferenceType,
        pointer: DifferencePointer = None,
        value_a = None,
        value_b = None
    ) -> None:
        self.key = key
        self.type = type
        self.pointer = pointer
        self.value_a = value_a
        self.value_b = value_b

    @property
    def key_str(self):
        return ".".join(self.key)
    
    def __repr__(self) -> str:
        return f"{self.type} {self.key_str} {self.value_a}!={self.value_b}"


def get_index(entry: dict, *index_keys) -> str:
    for index_key in index_keys:
        if index := entry.get(index_key):
            return index

def compare(
    data_a,
    data_b,
    current_key: list[str] = None,
    ignore_keys: list[list[str]] = None,
    key_extractors: list[Callable] = [default_dict_key_extractor]
):

    if current_key and ignore_keys and current_key in ignore_keys:
        return

    if data_a == data_b:
        return

    if not current_key:
        current_key = []

    type_a = type(data_a)
    type_b = type(data_b)

    if type_a != type_b:
        yield Difference(
            current_key,
            DifferenceType.TYPE,
            type_a,
            type_b
        )
        return

    if data_a == data_b:
        return

    if type_a == dict:
        keys_a = data_a.keys()
        keys_b = data_b.keys()

        for key in keys_a:
            if not key in keys_b:
                yield Difference(
                    current_key + [key],
                    DifferenceType.MISSING,
                    DifferencePointer.B
                )

        for key in keys_b:
            if not key in keys_a:
                yield Difference(
                    current_key + [key],
                    DifferenceType.MISSING,
                    DifferencePointer.A
                )
            else:
                yield from compare(
                    data_a[key], data_b[key], current_key + [key])
    elif type_a == list:
        list_a = list_to_dict(data_a, key_extractors)
        list_b = list_to_dict(data_b, key_extractors)
        yield from compare(list_a, list_b, current_key)
    else:
        yield Difference(
            current_key,
            DifferenceType.NOT_EQUAL,
            value_a = data_a,
            value_b = data_b
        )
