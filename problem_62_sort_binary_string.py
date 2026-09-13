"""
Problem 62: Sort the Binary String (Minimum Operations to Sort)
--------------------------------------------------------------
You have a binary string S of length N. In one operation you can select a
substring of S and reverse it.
For example, on reversing the substring S[2,4] for S = 11000, we change 11000 -> 10010.

Find the minimum number of operations required to sort this binary string (all '0's before '1's).

Input Format:
- The first line of input contains a single integer T, denoting the number of test cases.
- Each test case consists of 2 lines of input:
  - First line: integer N (length of the binary string).
  - Second line: binary string S of length N.

Output Format:
- For each test case, output on a new line the minimum number of operations required.

Constraints:
- 1 <= T <= 2 * 10^5
- 1 <= N <= 2 * 10^5
- Sum of N over all test cases <= 10^6
- String S consists of only '0's and '1's.

Sample Input:
4
3
000
4
1001
4
1010
6
010101

Sample Output:
0
1
2
2
"""

import sys


def min_operations_to_sort(s: str) -> int:
    """
    Computes the minimum number of substring reversal operations needed to sort
    a binary string into non-decreasing order (0s before 1s).

    Algorithmic Insight:
    --------------------
    - A sorted binary string consists of zero or more '0's followed by zero or more '1's (0*1*).
    - Notice that a sorted string contains zero occurrences of the adjacent pair "10".
    - In any unsorted string, an inversion occurs wherever '1' precedes '0'.
    - Each substring reversal can eliminate at most one "10" boundary transition:
      reversing a segment that begins with '1' and ends with '0' swaps the boundary transitions,
      reducing the number of "10" pairs by at most 1.
    - Conversely, choosing the segment starting at any '1' immediately followed by a block of '0's
      and reversing it to bring that block of '0's forward always reduces the count of "10" by exactly 1.
    - Thus, the minimum number of operations is precisely the count of "10" transitions (or occurrences of "10").

    Time Complexity:
    ----------------
    - O(N): A single linear pass through the binary string.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    ops = 0
    for i in range(len(s) - 1):
        if s[i] == "1" and s[i + 1] == "0":
            ops += 1
    return ops


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        results.append(str(min_operations_to_sort(s)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ("000", 0),
        ("1001", 1),
        ("1010", 2),
        ("010101", 2),
        ("101010", 3),
        ("1111", 0),
        ("0011", 0),
        ("11001100", 2),
    ]
    for s_val, expected in test_cases:
        res = min_operations_to_sort(s_val)
        print(f"S: '{s_val}' -> Min Ops: {res} (Expected: {expected})")
        assert res == expected, f"Failed for S={s_val}: got {res}, expected {expected}"
    print("All Sort Binary String tests passed successfully!")
