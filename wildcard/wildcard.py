import fnmatch
from typing import Union


def apply_wildcards_to_vals(vals: Union[str, list[str]],
                            wildcards: Union[str, list[str]]) -> list[str]:
    if isinstance(wildcards, str):
        wildcards = [wildcards]

    if isinstance(vals, str):
        vals = [vals]

    res = set()
    for wd in wildcards:
        matched_vals = fnmatch.filter(vals, wd)
        res.update(set(matched_vals))
    return list(res)


def check_val_by_wildcards(val: str, wildcards: Union[str, list[str]]) -> bool:
    if isinstance(wildcards, str):
        wildcards = [wildcards]

    for wd in wildcards:
        vals = fnmatch.fnmatch(val, wd)
        if vals:
            return True
    return False
