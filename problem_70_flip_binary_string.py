"""
Problem 70: Flip Binary String (Non-Adjacent Indices)
-----------------------------------------------------
You are given a binary string S of length N. You can perform the following operation:
- Pick any set of indices such that no two picked indices are adjacent.
- Flip the values at the picked indices (change '0' to '1' and '1' to '0').

Find the minimum number of operations required to convert all the characters of S to '0'.

Input Format:
- The first line contains an integer T - the number of test cases.
- Each test case consists of 2 lines:
  - First line contains N - the length of S.
  - Second line contains the binary string S.

Output Format:
- For each test case, output the minimum number of operations required.

Constraints:
- 1 <= T <= 100
- 1 <= N <= 100

Sample Input:
3
6
101001
5
00000
3
111

Sample Output:
1
0
2
"""

import sys


def min_operations_to_zeros(s: str) -> int:
    """
    Computes minimum operations to flip all '1's to '0' where each operation can only
    flip a set of mutually non-adjacent indices.

    Algorithmic Analysis:
    ---------------------
    - Case 0: The string contains no '1's (all '0's).
      0 operations are needed.

    - Case 1: The string contains at least one '1', but NO two '1's are adjacent.
      That means "11" does not appear anywhere in S.
      The set of all indices with '1' is an independent set (no two indices adjacent).
      We can select all of these indices in a single operation and flip them to '0'.
      Exactly 1 operation is needed.

    - Case 2: The string contains adjacent '1's ("11" is present in S).
      Can we do it in 1 operation?
      No, because adjacent '1's cannot be chosen in the same operation.
      Can we always do it in 2 operations?
      Yes! The indices of the string can be partitioned into:
        1. Even indices (0, 2, 4, ...)
        2. Odd indices (1, 3, 5, ...)
      No two even indices are adjacent, and no two odd indices are adjacent.
      In operation 1, flip all '1's located at even indices.
      In operation 2, flip all '1's located at odd indices.
      This clears all '1's in at most 2 operations.
      Thus, exactly 2 operations are needed.

    Time Complexity:
    ----------------
    - O(N): Linear scan to check presence of '1' and "11".

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    if "1" not in s:
        return 0
    if "11" not in s:
        return 1
    return 2


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
        results.append(str(min_operations_to_zeros(s)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ("101001", 1),
        ("00000", 0),
        ("111", 2),
        ("1", 1),
        ("0", 0),
        ("101", 1),
        ("11", 2),
        ("11011", 2),
    ]
    for s_val, expected in test_cases:
        res = min_operations_to_zeros(s_val)
        print(f"S: '{s_val}' -> Min Ops: {res} (Expected: {expected})")
        assert res == expected, f"Failed for S={s_val}: got {res}, expected {expected}"
    print("All Flip Binary String tests passed successfully!")
