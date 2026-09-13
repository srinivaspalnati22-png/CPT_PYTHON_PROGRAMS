"""
Problem 63: Rearrange to Maximize Longest Alternating Substring
--------------------------------------------------------------
A binary string is called alternating if no two adjacent characters are equal:
T[i] != T[i+1] for each 1 <= i < M.
For example, 0, 1, 01, 10, 101, 010, 1010 are alternating strings,
while 11, 001, 1110 are not.

You are given a binary string S of length N. You can rearrange the characters of S
such that the length of the longest alternating substring of S is maximized.
Find this maximum value.

Input Format:
- The first line of input contains an integer T, denoting the number of test cases.
- Each test case consists of 2 lines:
  - First line contains an integer N (length of S).
  - Second line contains the binary string S.

Output Format:
- For each test case, output the maximum possible length of the longest alternating
  substring after rearrangement.

Constraints:
- 1 <= T <= 10^4
- 1 <= N <= 10^5
- Sum of N over all test cases <= 2 * 10^5
- S contains only '0' and '1'.

Sample Input:
4
3
110
4
1010
4
0000
7
1101101

Sample Output:
3
4
1
5
"""

import sys


def max_alternating_substring_length(s: str) -> int:
    """
    Finds the maximum length of an alternating substring after rearranging the characters of S.

    Algorithmic Insight:
    --------------------
    - In any alternating string, '0's and '1's alternate strictly: 0101... or 1010...
    - The counts of '0's and '1's in an alternating string can differ by at most 1.
    - Let c0 be the total number of '0's in S and c1 be the total number of '1's in S.
    - If c0 == c1:
      We can use all characters to form an alternating string of length c0 + c1 = 2 * c0 = N.
    - If c0 != c1:
      Without loss of generality, assume c0 < c1. We can take all c0 zeros, and at most
      c0 + 1 ones to place around them: 1 0 1 0 1 ... 1.
      The maximum length is c0 + (c0 + 1) = 2 * min(c0, c1) + 1.
      Any remaining extra characters can be placed at the beginning or end of S without
      affecting this contiguous alternating substring.

    Formula:
    --------
    - If c0 == c1: return 2 * c0
    - If c0 != c1: return 2 * min(c0, c1) + 1

    Time Complexity:
    ----------------
    - O(N): Single pass to count '0's and '1's.

    Space Complexity:
    -----------------
    - O(1): Only character counters used.
    """
    c0 = s.count("0")
    c1 = len(s) - c0

    if c0 == c1:
        return 2 * c0
    else:
        return 2 * min(c0, c1) + 1


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
        results.append(str(max_alternating_substring_length(s)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ("110", 3),
        ("1010", 4),
        ("0000", 1),
        ("1101101", 5),
        ("1", 1),
        ("0", 1),
        ("0011", 4),
        ("11111", 1),
    ]
    for s_val, expected in test_cases:
        res = max_alternating_substring_length(s_val)
        print(f"S: '{s_val}' -> Max Alternating Length: {res} (Expected: {expected})")
        assert res == expected, f"Failed for S={s_val}: got {res}, expected {expected}"
    print("All Longest Alternating Substring tests passed successfully!")
