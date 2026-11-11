"""first_match(items, target): index of the first element equal to target.

Contract (from SPEC.md and the task harness semantics):
- items must be a list of strings, target must be a string; the whole
  input is validated before searching, so a non-string element anywhere
  in the list raises TypeError even if a match sits before it.
- Returns the index (exact int) of the first element equal to target,
  or None when no element matches (including an empty list).
- The input list is never mutated.
"""


def first_match(items, target):
    if not isinstance(items, list):
        raise TypeError("items must be a list of strings")
    if not isinstance(target, str):
        raise TypeError("target must be a string")
    for element in items:
        if not isinstance(element, str):
            raise TypeError("items must be a list of strings")
    for index, element in enumerate(items):
        if element == target:
            return index
    return None
