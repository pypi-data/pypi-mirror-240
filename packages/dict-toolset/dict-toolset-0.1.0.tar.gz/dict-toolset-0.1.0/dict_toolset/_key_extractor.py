from typing import Callable


def default_dict_key_extractor(entry):
    if isinstance(entry, dict):
        return (
            entry.get('id')
            or entry.get('ID')
            or entry.get('uuid')
            or entry.get('UUID')
        )
    

