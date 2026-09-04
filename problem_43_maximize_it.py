"""
Problem 43: Maximize It! (itertools.product & Modular Arithmetic)
-----------------------------------------------------------------
You are given a function f(X) = X^2. You are also given K lists.
The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(X1) + f(X2) + . . . + f(Xk)) % M

Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element.

Input Format:
- The first line contains 2 space separated integers K and M.
- The next K lines each contain an integer Ni, denoting the number of elements in the ith list,
  followed by Ni space-separated integers denoting the elements in the list.

Constraints:
- 1 <= K <= 7
- 1 <= M <= 1000
- 1 <= Ni <= 7
- 1 <= Magnitude of elements in list <= 10^9

Output Format:
- Output a single integer denoting the value Smax.

Sample Input:
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Sample Output:
206
"""

import sys
from itertools import product


def maximize_expression(k: int, m: int, lists: list[list[int]]) -> int:
    """
    Computes the maximum possible value of (sum(X_i^2)) % M by choosing one element from each list.

    Approach:
    ---------
    Since K <= 7 and Ni <= 7, the total number of combinations is at most 7^7 = 823,543.
    This search space is small enough to explore completely using Cartesian product (`itertools.product`).
    For each combination (x_1, x_2, ..., x_k), we evaluate:
        (sum(x_i^2 for x_i in combo)) % M
    and track the maximum value found.

    Time Complexity:
    ----------------
    - O(prod(N_i) * K) <= O(7^7 * 7) ≈ O(5.7 * 10^6) operations, comfortably runs within milliseconds.

    Space Complexity:
    -----------------
    - O(K) space for the generator tuple in `itertools.product`.
    """
    max_val = 0
    for combo in product(*lists):
        current_sum = sum(x * x for x in combo) % m
        if current_sum > max_val:
            max_val = current_sum
        if max_val == m - 1:  # Modulo cannot exceed m - 1
            break

    return max_val


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    k, m = map(int, lines[0].split())
    lists = []
    for i in range(1, k + 1):
        if i < len(lines):
            row = list(map(int, lines[i].split()))
            # row[0] is Ni, row[1:] are the elements
            lists.append(row[1:])

    ans = maximize_expression(k, m, lists)
    print(ans)


if __name__ == "__main__":
    k, m = 3, 1000
    sample_lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10],
    ]
    result = maximize_expression(k, m, sample_lists)
    print(f"K = {k}, M = {m}")
    print(f"Lists: {sample_lists}")
    print(f"Maximized Value S_max: {result}")
    assert result == 206, f"Expected 206, got {result}"
    print("Test passed successfully!")
