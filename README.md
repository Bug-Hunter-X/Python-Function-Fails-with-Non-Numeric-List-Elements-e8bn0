# Python Function Bug: Handling Non-Numeric Inputs in Average Calculation

This repository demonstrates a common bug in Python functions that involves handling lists containing non-numeric values.  The `calculate_average` function works correctly for empty and zero-filled lists but throws a `TypeError` when encountering non-numeric elements.

The bug is demonstrated in `bug.py` and a corrected version is provided in `bugSolution.py`.

## How to Reproduce

1. Clone this repository.
2. Run `bug.py`. Observe the `TypeError` when the function is called with a list containing a string.