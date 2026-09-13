"""
Problem 64: Hidden Numbers Tuple (min(A,B), min(B,C), min(C,A))
---------------------------------------------------------------
There are 3 hidden numbers A, B, C.
You somehow found out the values of min(A,B), min(B,C), and min(C,A).
Determine whether there exists any tuple (A, B, C) that satisfies the given values.

Input Format:
- The first line contains a single integer T, denoting the number of test cases.
- The first and only line of each test case contains 3 space-separated integers
  denoting min(A,B), min(B,C), and min(C,A).

Output Format:
- For each test case, output YES if there exists any valid tuple (A, B, C), and NO otherwise.

Constraints:
- 1 <= T <= 1000
- 1 <= min(A,B), min(B,C), min(C,A) <= 10^9

Sample Input:
3
5 5 5
2 3 4
2 2 4

Sample Output:
YES
NO
YES
"""

import sys
from typing import Tuple


def can_form_tuple(x: int, y: int, z: int) -> str:
    """
    Checks if there exists a 3-tuple (A, B, C) such that:
        min(A, B) = x, min(B, C) = y, min(C, A) = z.

    Mathematical Insight:
    ---------------------
    - Consider any three numbers sorted in ascending order: u <= v <= w.
    - The pairwise minimums are:
        min(u, v) = u
        min(u, w) = u
        min(v, w) = v
    - Regardless of which variables (A, B, C) take the values u, v, w, the three
      pairwise minimums MUST consist of two copies of the smallest value u, and
      one value v such that v >= u.
    - In other words, when the three input values are sorted in non-decreasing order:
        val_1 <= val_2 <= val_3
      We must have:
        val_1 == val_2
    - Conversely, if val_1 == val_2 <= val_3, we can always choose:
        A = val_3, B = val_1, C = val_3 (or corresponding assignment)
      which yields exactly min(A,B) = val_1, min(B,C) = val_1, min(C,A) = val_3.

    Time Complexity:
    ----------------
    - O(1): Sorting 3 integers.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    vals = sorted([x, y, z])
    return "YES" if vals[0] == vals[1] else "NO"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        z = int(input_data[idx + 2])
        idx += 3
        results.append(can_form_tuple(x, y, z))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ((5, 5, 5), "YES"),
        ((2, 3, 4), "NO"),
        ((2, 2, 4), "YES"),
        ((10, 4, 4), "YES"),
        ((7, 8, 9), "NO"),
        ((1, 1, 100), "YES"),
    ]
    for (x, y, z), expected in test_cases:
        res = can_form_tuple(x, y, z)
        print(f"Inputs: ({x}, {y}, {z}) -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for ({x}, {y}, {z}): got {res}, expected {expected}"
    print("All Hidden Numbers tests passed successfully!")
