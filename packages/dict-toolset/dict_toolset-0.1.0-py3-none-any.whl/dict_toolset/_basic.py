from typing import Callable


def get_key(data, key_extractors: list[Callable]):
    for key_extractor in key_extractors:
        if key := key_extractor(data):
            return key

def list_to_dict(input: list, key_extractors: list[Callable] = []) -> dict:
    rtn = {}
    for index, entry in enumerate(input):
        index = get_key(entry, key_extractors) or index
        rtn[f"[{index}]"] = entry
    return rtn

def extend_list(input: list, index: int):
    if (diff := (index + 1) - len(input)) > 0:
        input.extend([None for i in range(diff)])
    return input[index]
    
