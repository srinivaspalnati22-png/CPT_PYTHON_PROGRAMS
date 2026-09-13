"""
Problem 80: Valid Phone Number Bill
-----------------------------------
In Chefland, a valid phone number consists of exactly 5 digits with no leading zeros.
For example, 98765, 10000, and 71023 are valid phone numbers,
while 04123, 9231, and 872310 are not.

Chef went to a store and purchased N items, where the cost of each item is X.
Find whether the total bill is equivalent to a valid phone number (i.e. a 5-digit number without leading zeros).

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of two space-separated integers N and X.

Output Format:
- For each test case, output on a new line YES if the total bill is equivalent to a valid
  phone number, and NO otherwise.

Constraints:
- 1 <= T <= 100
- 1 <= N, X <= 1000

Sample Input:
4
25 785
402 11
100 100
333 333

Sample Output:
YES
NO
YES
NO
"""

import sys


def is_valid_phone_bill(n: int, x: int) -> str:
    """
    Checks if total bill N * X represents a valid 5-digit number without leading zeros.

    Criteria:
    ---------
    - A valid 5-digit number with no leading zeros must lie strictly in the range:
        10000 <= Total Bill <= 99999
    - Any number < 10000 has fewer than 5 digits.
    - Any number >= 100000 has 6 or more digits.

    Time Complexity:
    ----------------
    - O(1): Constant time multiplication and comparison.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    total_bill = n * x
    return "YES" if 10000 <= total_bill <= 99999 else "NO"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx + 1])
        idx += 2
        results.append(is_valid_phone_bill(n, x))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ((25, 785), "YES"),    # 25 * 785 = 19625 (5 digits)
        ((402, 11), "NO"),     # 402 * 11 = 4422 (4 digits)
        ((100, 100), "YES"),   # 100 * 100 = 10000 (5 digits)
        ((333, 333), "NO"),    # 333 * 333 = 110889 (6 digits)
        ((10, 1000), "YES"),   # 10000
        ((1, 9999), "NO"),     # 9999
        ((100, 999), "YES"),   # 99900
    ]
    for (n_val, x_val), expected in test_cases:
        res = is_valid_phone_bill(n_val, x_val)
        print(f"N={n_val}, X={x_val} -> Bill: {n_val * x_val} -> Valid: {res} (Expected: {expected})")
        assert res == expected, f"Failed for ({n_val}, {x_val}): got {res}, expected {expected}"
    print("All Valid Phone Number Bill tests passed successfully!")
