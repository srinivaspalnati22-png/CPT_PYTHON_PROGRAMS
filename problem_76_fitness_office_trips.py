"""
Problem 76: Fit (Office Trips Walking Distance)
-----------------------------------------------
Siva wants to become fit, for which he decided to walk to the office and return home by walking.
It is known that Siva's office is X km away from his home.
If his office is open 5 days in a week, find the number of kilometers Siva travels
through office trips in a week.

Input Format:
- First line will contain T, number of test cases.
- Each test case consists of a single line with an integer X.

Output Format:
- For each test case, output the number of kilometers Siva travels through office trips in a week.

Constraints:
- 1 <= T <= 10
- 1 <= X <= 10

Sample Input:
4
1
3
7
10

Sample Output:
10
30
70
100
"""

import sys


def weekly_walking_distance(x: int) -> int:
    """
    Computes total kilometers walked in a 5-day week for office commute.

    Calculation:
    ------------
    - Distance to office: X km
    - Return distance: X km
    - Total round-trip per day = 2 * X km
    - In 5 working days per week:
        Weekly Distance = 5 * (2 * X) = 10 * X km

    Time Complexity:
    ----------------
    - O(1): Single multiplication.

    Space Complexity:
    -----------------
    - O(1): Auxiliary storage.
    """
    return 10 * x


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        x = int(input_data[i])
        results.append(str(weekly_walking_distance(x)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        (1, 10),
        (3, 30),
        (7, 70),
        (10, 100),
        (0, 0),
        (5, 50),
    ]
    for x_val, expected in test_cases:
        res = weekly_walking_distance(x_val)
        print(f"X: {x_val} km -> Weekly Distance: {res} km (Expected: {expected})")
        assert res == expected, f"Failed for X={x_val}: got {res}, expected {expected}"
    print("All Fitness Office Trips tests passed successfully!")
