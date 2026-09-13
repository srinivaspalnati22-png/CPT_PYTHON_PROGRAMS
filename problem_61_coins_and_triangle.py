"""
Problem 61: Coins And Triangle (Chef and Gold Coins Triangle)
------------------------------------------------------------
Ravi belongs to a very rich family which owns many gold mines.
Today, he brought N gold coins and decided to form a triangle using these coins.
He puts:
- 1 coin in the 1st row
- 2 coins in the 2nd row
- 3 coins in the 3rd row
... and so on.

Ravi wants to form a triangle with maximum possible height using at most N coins.
Find the maximum possible height H such that:
    H * (H + 1) / 2 <= N

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of a single line with an integer N.

Output Format:
- For each test case, output an integer corresponding to the maximum possible height.

Constraints:
- 1 <= T <= 100
- 1 <= N <= 10^9

Sample Input:
3
3
5
7

Sample Output:
2
2
3
"""

import math
import sys


def max_triangle_height(n: int) -> int:
    """
    Computes the maximum height H of a triangle that can be formed using at most N coins.

    Mathematical Formulation:
    -------------------------
    The number of coins in a triangle of height H is the sum of the first H positive integers:
        Coins(H) = H * (H + 1) // 2

    We require:
        H * (H + 1) / 2 <= N
        H^2 + H - 2N <= 0

    Solving the quadratic equation:
        H = (-1 + sqrt(1 + 8N)) / 2

    Using integer square root `math.isqrt` ensures exact calculation without floating point precision issues:
        H = (isqrt(1 + 8 * N) - 1) // 2

    Time Complexity:
    ----------------
    - O(1): Constant time arithmetic and integer square root computation.

    Space Complexity:
    -----------------
    - O(1): Auxiliary storage.
    """
    if n <= 0:
        return 0
    return (math.isqrt(1 + 8 * n) - 1) // 2


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str(max_triangle_height(n)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        (3, 2),
        (5, 2),
        (7, 3),
        (1, 1),
        (6, 3),
        (10, 4),
        (10**9, 44720),
    ]
    for n_val, expected in test_cases:
        res = max_triangle_height(n_val)
        print(f"N: {n_val} -> Height: {res} (Expected: {expected})")
        assert res == expected, f"Failed for N={n_val}: got {res}, expected {expected}"
    print("All Coins And Triangle tests passed successfully!")
