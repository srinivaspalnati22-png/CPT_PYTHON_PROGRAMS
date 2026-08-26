"""
Problem 26: Richest Person in Iceland
-------------------------------------
Sunil's assets are currently worth A billion dollars. He aims to increase his assets
by X billion dollars per year.
To be the richest person in Iceland, he needs to be worth at least B billion dollars.
How many years will it take Sunil to reach his goal? (Note: X divides B - A).

Input Format:
- The first line contains an integer T — the number of test cases.
- Each test case contains three integers A, B, and X.

Output Format:
- For each test case, output in a single line the number of years required.

Constraints:
- 1 <= T <= 21000
- 100 <= A < B <= 200
- 1 <= X <= 50
- X divides (B - A)

Example:
Input:
3
100 200 10
111 199 11
190 200 10

Output:
10
8
1
"""

import sys

def years_to_target(a: int, b: int, x: int) -> int:
    """
    To reach B from A with an annual increment of X:
    Years = (B - A) // X
    
    Time Complexity: O(1) per test case.
    Space Complexity: O(1).
    """
    return (b - a) // x


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        x = int(input_data[idx + 2])
        idx += 3
        results.append(str(years_to_target(a, b, x)))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [(100, 200, 10), (111, 199, 11), (190, 200, 10)]
    for a, b, x in test_cases:
        print(f"A = {a}, B = {b}, X = {x} -> Years: {years_to_target(a, b, x)}")
