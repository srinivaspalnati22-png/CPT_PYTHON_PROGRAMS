"""
Problem 32: Triangle Quest 2 (Palindromic Triangle)
---------------------------------------------------
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321

Rules:
- Complete the code using no more than two lines (the for-statement and exactly one print statement).
- Note: Using anything related to strings will result in a score of 0.
- Using more than one for-statement will result in a score of 0.

Input Format:
- A single line of input containing the integer N.

Constraints:
- 0 < N < 10

Output Format:
- Print the palindromic triangle of size N as explained above.

Sample Input:
5

Sample Output:
1
121
12321
1234321
123454321
"""

import sys

def solve_triangle_quest_2(n: int) -> list[int]:
    """
    Mathematical Formula for Palindromic Numbers (Demlo Numbers):
    --------------------------------------------------------------
    The square of a repunit (a number consisting solely of ones: 1, 11, 111, ...)
    yields a palindromic number sequence for lengths <= 9:
        1^2      = 1
        11^2     = 121
        111^2    = 12321
        1111^2   = 1234321
        11111^2  = 123454321

    The repunit of length i can be generated arithmetically as:
        (10^i - 1) // 9

    Squaring it gives:
        ((10**i - 1) // 9) ** 2

    Time Complexity: O(N) - Loop runs N times with O(1) arithmetic operations.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    results = []
    for i in range(1, n + 1):
        val = ((10**i - 1) // 9) ** 2
        results.append(val)
    return results


def main():
    """HackerRank 2-line solution format."""
    lines = sys.stdin.read().split()
    if not lines:
        return
    n = int(lines[0])
    for i in range(1, n + 1):
        print(((10**i - 1) // 9) ** 2)


if __name__ == "__main__":
    test_n = 5
    print(f"--- Palindromic Triangle for N = {test_n} ---")
    for row in solve_triangle_quest_2(test_n):
        print(row)
