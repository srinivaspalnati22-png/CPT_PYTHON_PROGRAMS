"""
Problem 58: Check Subset (Set .issubset() Operations)
-----------------------------------------------------
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.
If set A is a subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format:
- The first line will contain the number of test cases, T.
- For each test case:
  - Line 1: Number of elements in set A.
  - Line 2: Space separated elements of set A.
  - Line 3: Number of elements in set B.
  - Line 4: Space separated elements of set B.

Constraints:
- 0 < T < 21
- 0 < Number of elements in each set < 1001

Output Format:
- Output True or False for each test case on separate lines.

Sample Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output:
True
False
False
"""

import sys


def is_subset(set_a: set, set_b: set) -> bool:
    """
    Determines whether set_a is a subset of set_b.

    Approach:
    ---------
    In Python, `set_a.issubset(set_b)` or `set_a <= set_b` checks if every element
    of set_a is present in set_b.

    Time Complexity:
    ----------------
    - O(|set_a|): Checks membership of each element of A in hash table B in O(1) average time.

    Space Complexity:
    -----------------
    - O(|set_a| + |set_b|) to store the sets.
    """
    return set_a.issubset(set_b)


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    line_idx = 1
    for _ in range(t):
        if line_idx < len(lines):
            _len_a = int(lines[line_idx].strip())
            set_a = set(lines[line_idx + 1].split())
            _len_b = int(lines[line_idx + 2].strip())
            set_b = set(lines[line_idx + 3].split())
            line_idx += 4
            print(is_subset(set_a, set_b))


if __name__ == "__main__":
    test_cases = [
        (set("1 2 3 5 6".split()), set("9 8 5 6 3 2 1 4 7".split()), True),
        (set("2".split()), set("3 6 5 4 1".split()), False),
        (set("1 2 3 5 6 8 9".split()), set("9 8 2".split()), False),
    ]
    for i, (a, b, expected) in enumerate(test_cases, 1):
        res = is_subset(a, b)
        print(f"Test {i}: A is subset of B -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for test {i}"
    print("All subset tests passed successfully!")
