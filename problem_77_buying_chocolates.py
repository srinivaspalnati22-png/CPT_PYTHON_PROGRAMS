"""
Problem 77: Buying Chocolates for Chefina
-----------------------------------------
Alex has X 5-rupee coins and Y 10-rupee coins.
Alex goes to a shop to buy chocolates for Chefina where each chocolate costs Z rupees.
Find the maximum number of chocolates that Alex can buy for Chefina.

Input Format:
- The first line contains an integer T — the number of test cases.
- Each test case consists of a single line with three integers X, Y, and Z.

Output Format:
- For each test case, output the maximum number of chocolates that Alex can buy.

Constraints:
- 1 <= T <= 100
- 1 <= X, Y, Z <= 1000

Sample Input:
4
10 10 10
3 1 8
8 1 3
4 4 1000

Sample Output:
15
3
16
0
"""

import sys


def max_chocolates(x: int, y: int, z: int) -> int:
    """
    Calculates the maximum chocolates Alex can purchase given his coin denominations.

    Formulation:
    ------------
    - Alex has X 5-rupee coins: Value = 5 * X rupees.
    - Alex has Y 10-rupee coins: Value = 10 * Y rupees.
    - Total money available = 5 * X + 10 * Y rupees.
    - Each chocolate costs Z rupees.
    - Maximum chocolates purchasable:
        count = (5 * X + 10 * Y) // Z

    Time Complexity:
    ----------------
    - O(1): Constant time arithmetic.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    total_money = 5 * x + 10 * y
    return total_money // z


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
        results.append(str(max_chocolates(x, y, z)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ((10, 10, 10), 15),
        ((3, 1, 8), 3),
        ((8, 1, 3), 16),
        ((4, 4, 1000), 0),
        ((1, 1, 5), 3),
    ]
    for (x_val, y_val, z_val), expected in test_cases:
        res = max_chocolates(x_val, y_val, z_val)
        print(f"(X={x_val}, Y={y_val}, Z={z_val}) -> Chocolates: {res} (Expected: {expected})")
        assert res == expected, f"Failed for ({x_val}, {y_val}, {z_val}): got {res}, expected {expected}"
    print("All Buying Chocolates tests passed successfully!")
