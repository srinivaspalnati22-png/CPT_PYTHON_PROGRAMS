"""
Problem 68: Gift Anu Distinct Integers with Mean X
--------------------------------------------------
It is Anu's birthday. Anu's favourite number is X. Anu loves averages.
Therefore you decide to gift 3 integers A1, A2, A3 such that:
1. The mean of A1, A2, A3 is X: (A1 + A2 + A3) / 3 = X  <=>  A1 + A2 + A3 = 3 * X
2. 1 <= A1, A2, A3 <= 1000
3. A1, A2, and A3 are distinct.

Output any suitable triplet A1, A2, A3.

Input Format:
- First line contains an integer T, denoting the number of test cases.
- Each test case consists of a single integer X.

Output Format:
- For each test case, one line containing 3 space-separated integers A1, A2, A3.

Constraints:
- 1 <= T <= 100
- 2 <= X <= 100

Sample Input:
3
3
5
5

Sample Output:
1 3 5
1 6 8
3 5 7
"""

import sys
from typing import Tuple


def find_average_triplet(x: int) -> Tuple[int, int, int]:
    """
    Finds three distinct integers A1, A2, A3 in [1, 1000] whose arithmetic mean is X.

    Mathematical Construction:
    --------------------------
    We require:
        A1 + A2 + A3 = 3 * X
        A1 < A2 < A3
        1 <= A1, A2, A3 <= 1000

    Since X >= 2:
        Choose A1 = X - 1
        Choose A2 = X
        Choose A3 = X + 1

    Properties:
    -----------
    1. Sum: (X - 1) + X + (X + 1) = 3 * X
    2. Mean: (3 * X) / 3 = X
    3. Distinctness: X - 1 < X < X + 1 (all strictly different)
    4. Bounds: Since 2 <= X <= 100, we have 1 <= X - 1 < X + 1 <= 101 <= 1000.
    Thus, (X - 1, X, X + 1) is universally valid for all test cases.

    Time Complexity:
    ----------------
    - O(1): Closed-form arithmetic computation.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    return (x - 1, x, x + 1)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        x = int(input_data[i])
        a1, a2, a3 = find_average_triplet(x)
        results.append(f"{a1} {a2} {a3}")
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [2, 3, 5, 10, 50, 100]
    for x_val in test_cases:
        a1, a2, a3 = find_average_triplet(x_val)
        print(f"X={x_val} -> Triplet: ({a1}, {a2}, {a3})")
        assert len({a1, a2, a3}) == 3, f"Not distinct: {a1}, {a2}, {a3}"
        assert (a1 + a2 + a3) == 3 * x_val, f"Mean not {x_val}: {a1}, {a2}, {a3}"
        assert 1 <= a1 <= 1000 and 1 <= a2 <= 1000 and 1 <= a3 <= 1000, "Out of bounds"
    print("All Favourite Number Average tests passed successfully!")
