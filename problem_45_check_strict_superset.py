"""
Problem 45: Check Strict Superset
---------------------------------
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset,
meaning:
1. Every element of the subset must exist in set A.
2. The subset must not be equal to set A (i.e., len(subset) < len(A)).
In Python, this is directly evaluated by the strict superset operator `A > other_set`.

Input Format:
- The first line contains the space-separated elements of set A.
- The second line contains integer n, the number of other sets.
- The next n lines contain the space-separated elements of the other sets.

Constraints:
- 0 < len(set(A)) < 500
- 0 < N < 20
- 0 < len(otherSets) < 100

Output Format:
- Print True if set A is a strict superset of all other N sets. Otherwise, print False.

Sample Input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output:
False
"""

import sys


def is_strict_superset_of_all(set_a: set, other_sets: list[set]) -> bool:
    """
    Checks if set_a is a strict superset of all other sets in other_sets.

    Approach:
    ---------
    In Python, the `>` operator between two sets checks strict superset:
        `A > B` is True if and only if B is a subset of A and A != B (A contains all elements of B plus at least one more).
    We can iterate through all other sets; if any set violates `set_a > s`, we can immediately return False.

    Time Complexity:
    ----------------
    - O(sum(len(other_set))) across all N sets. Checking subset/superset is O(len(subset)).

    Space Complexity:
    -----------------
    - O(|A| + sum(|other_set|)) to store sets.
    """
    for s in other_sets:
        if not (set_a > s):
            return False
    return True


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    set_a = set(lines[0].split())
    n = int(lines[1].strip())
    other_sets = [set(lines[2 + i].split()) for i in range(n) if 2 + i < len(lines)]
    print(is_strict_superset_of_all(set_a, other_sets))


if __name__ == "__main__":
    sample_a = set("1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78".split())
    test_1_others = [
        set("1 2 3 4 5".split()),
        set("100 11 12".split()),
    ]
    res1 = is_strict_superset_of_all(sample_a, test_1_others)
    print(f"Sample 1 Result: {res1} (Expected: False)")
    assert res1 is False

    test_2_others = [
        set("1 2 3".split()),
        set("4 5 6".split()),
    ]
    res2 = is_strict_superset_of_all(sample_a, test_2_others)
    print(f"Sample 2 Result: {res2} (Expected: True)")
    assert res2 is True

    print("All strict superset tests passed successfully!")
