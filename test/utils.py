from itertools import chain, combinations
from typing import List, Tuple, Any, Dict

def powerset(iterable) -> List[Tuple[Any]]:
    try:
        iter(iterable)
    except TypeError:
        print(f"The {iterable} object cannot be iterable")
        raise
    else:
        iter_list = list(iterable)
        return chain.from_iterable(combinations(iter_list, r) for r in range(len(iter_list) + 1))

def powerset_dict(iterable: dict) -> List[Dict[Any, Any]]:
    if isinstance(iterable, dict):
        return [{i:iterable[i] for i in key} for key in chain.from_iterable(combinations(iterable, r) for r in range(1,len(iterable)+1))]
    else:
        raise TypeError(f"The {iterable} argument is not a dictionary.")