from typing import Callable

from ._basic import list_to_dict, extend_list
from ._key_extractor import default_dict_key_extractor


def flat(
    value,
    current_key: list[str] = [],
    key_extractors: list[Callable] = [default_dict_key_extractor],
    exclude_none: bool = False
):
    if value is None:
        if not exclude_none:
            yield (current_key, None)
    elif isinstance(value, dict):
        for entry_key, entry_value in value.items():
            path = current_key + [entry_key]
            yield from flat(
                entry_value,
                path,
                key_extractors
            )
    elif isinstance(value, list):
        list_dict = list_to_dict(value, key_extractors)
        yield from flat(
            list_dict,
            current_key,
            key_extractors
        )
    else:
        yield (current_key, value)

def _unflat_pair(
    keys: list[str],
    value: object,
    return_value: dict = None,
    convert_entries: list = []
):
    if len(keys) < 1:
        return value
    
    key = keys[0]

    if key.startswith("[") and key.endswith("]"):
        midst = key[1:-1]
        return_value = {} if return_value is None else return_value
        if return_value not in convert_entries:
            convert_entries.append(return_value)
        index = int(midst) if midst.isnumeric() else midst
        return_value[index] = _unflat_pair(
            keys[1:], value, return_value.get(index), convert_entries)
    else:
        return_value = {} if return_value is None else return_value
        return_value[key] = _unflat_pair(
            keys[1:], value, return_value.get(key), convert_entries)

    return return_value

def unflat(
    key_values: list[tuple[list[str], object]],
    return_value: dict = None
):
    convert_entries = []

    if return_value is None:
        return_value = {}
    for keys, value in key_values:
        _unflat_pair(keys, value, return_value, convert_entries)
    return return_value

        