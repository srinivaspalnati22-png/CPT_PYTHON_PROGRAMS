"""
Problem 31: Triangle Quest (Numerical Triangle)
-----------------------------------------------
You are given a positive integer N. Print a numerical triangle of height N - 1
like the one below:
1
22
333
4444
55555
...

Rules:
- Use only arithmetic operations, a single for loop, and a print statement.
- Use no more than two lines of code (the for loop and the print statement).
- Using anything related to strings (such as str(), string multiplication) will give 0 points.

Input Format:
- A single line containing integer N.

Constraints:
- 1 <= N <= 9

Output Format:
- Print N - 1 lines as explained above.

Sample Input:
5

Sample Output:
1
22
333
4444
"""

import sys

def solve_triangle_quest(n: int) -> list[int]:
    """
    Mathematical Formula for Repunit Multiplication:
    -------------------------------------------------
    The repunit of length i (a number consisting of i ones: 1, 11, 111, 1111...)
    can be generated purely arithmetically using the geometric series sum formula:
        (10^i - 1) // 9  or  (10^i // 9)

    For example:
        i = 1: (10 // 9) * 1 = 1 * 1 = 1
        i = 2: (100 // 9) * 2 = 11 * 2 = 22
        i = 3: (1000 // 9) * 3 = 111 * 3 = 333
        i = 4: (10000 // 9) * 4 = 1111 * 4 = 4444

    Thus, the expression is: (10**i // 9) * i

    Time Complexity: O(N) - Loop runs N-1 times with constant time arithmetic.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    results = []
    for i in range(1, n):
        val = (10**i // 9) * i
        results.append(val)
    return results


def main():
    """HackerRank 2-line solution format."""
    lines = sys.stdin.read().split()
    if not lines:
        return
    n = int(lines[0])
    for i in range(1, n):
        print((10**i // 9) * i)


if __name__ == "__main__":
    test_n = 5
    print(f"--- Numerical Triangle for N = {test_n} ---")
    for row in solve_triangle_quest(test_n):
        print(row)
