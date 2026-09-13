"""
Problem 78: Candy Store (Daily Goal and Bonus)
---------------------------------------------
Arun has started working at the candy store.
The store has 100 chocolates in total.
Arun's daily goal is to sell X chocolates.
- For each chocolate sold up to X, he gets 1 rupee.
- For each chocolate sold exceeding his daily goal X, he gets 2 rupees per extra chocolate.

If Arun sells Y chocolates in a day, find the total amount he made.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of two space-separated integers X and Y.

Output Format:
- For each test case, output on a new line the total amount Arun made.

Constraints:
- 1 <= T <= 100
- 1 <= X, Y <= 100

Sample Input:
4
3 1
5 5
4 7
2 3

Sample Output:
1
5
10
4
"""

import sys


def calculate_earnings(goal: int, sold: int) -> int:
    """
    Computes Arun's total earnings based on regular and bonus compensation.

    Piecewise Structure:
    --------------------
    - If sold <= goal:
        earnings = sold * 1 = sold
    - If sold > goal:
        earnings = goal * 1 + (sold - goal) * 2 = 2 * sold - goal

    Time Complexity:
    ----------------
    - O(1): Constant time evaluation.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    if sold <= goal:
        return sold
    else:
        return goal + 2 * (sold - goal)


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
        idx += 2
        results.append(str(calculate_earnings(x, y)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ((3, 1), 1),
        ((5, 5), 5),
        ((4, 7), 10),
        ((2, 3), 4),
        ((10, 15), 20),
        ((10, 5), 5),
    ]
    for (g_val, s_val), expected in test_cases:
        res = calculate_earnings(g_val, s_val)
        print(f"Goal: {g_val}, Sold: {s_val} -> Earnings: {res} (Expected: {expected})")
        assert res == expected, f"Failed for ({g_val}, {s_val}): got {res}, expected {expected}"
    print("All Candy Store tests passed successfully!")
