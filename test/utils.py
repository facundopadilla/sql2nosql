from itertools import chain, combinations
from typing import List, Tuple, Any, Dict


def powerset_dict(iterable: dict) -> List[Dict[Any, Any]]:
    if isinstance(iterable, dict):
        # One line: [{i:iterable[i] for i in key} for key in chain.from_iterable(combinations(iterable, r) for r in range(1,len(iterable)+1))]
        return [
            {i: iterable[i] for i in key}
            for key in chain.from_iterable(
                combinations(iterable, r) for r in range(1, len(iterable) + 1)
            )
        ]
    else:
        raise TypeError(f"The 'iterable' argument is not a dictionary.")
