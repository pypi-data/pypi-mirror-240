from typing import Callable

from ._key_extractor import default_dict_key_extractor
from ._basic import get_key


def _get_from_list(
    index,
    entries,
    key_extractors: list[Callable]
):
    for entry_index, entry in enumerate(entries):
        entry_key = get_key(entry, key_extractors) or entry_index
        if entry_key == index:
            return entry_index, entry

def merge(
    data_a,
    data_b,
    key_extractors: list[Callable] = [default_dict_key_extractor]
):
    type_a = type(data_a)
    type_b = type(data_b)

    if type_a != type_b:
        raise TypeError('Types a incompatible to merge')

    if type_a == dict:
        for key, value in data_a.items():
            type_a = type(value)
            if type_a in [dict, list]:
                merge(data_a[key], data_b[key])
            else:
                data_b[key] = value
    elif type_a == list:
        for index_a, entry_a in enumerate(data_a):
            index_a = get_key(entry_a, key_extractors) or index_a
            index_b, entry_b = _get_from_list(index_a, data_b, key_extractors)
            if type(entry_a) in [list, dict]:
                merge(entry_a, entry_b, key_extractors)
            else:
                data_b[index_b] = entry_a
