# first-match — implementation notes

`first_match(items, target)` returns the index of the first element equal
to `target`, or `None` when nothing matches (including an empty list).

Approach:
- Validate the full contract first: `items` must be a `list`, `target`
  must be a `str`, and every element must be a `str`. Any violation
  raises `TypeError` before searching, so a non-string element raises
  even when a match appears earlier in the list.
- Then a single linear scan returns the first index whose element
  equals `target` (exact, case-sensitive string equality; subclasses
  of `list`/`str` are accepted via `isinstance`).
- The input list is only read, never mutated, and the returned index
  is a plain `int`.

Verified locally with the pinned public checker:
`python3 tasks/first-match/check.py --solution tasks/first-match/first_match.py` → PASS.
