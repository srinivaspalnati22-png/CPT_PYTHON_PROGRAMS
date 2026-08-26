"""
Problem 23: Good Turn
---------------------
Sita and Geetha are playing with dice. In one turn, both of them roll their dice at once.
They consider a turn to be good if the sum of the numbers on their dice is strictly greater than 6.

Given X and Y on their respective dice, find whether the turn was good.

Input Format:
- The first line contains a single integer T — the number of test cases.
- Each test case contains two space-separated integers X and Y.

Output Format:
- For each test case, output "YES" if the turn was good and "NO" otherwise.

Constraints:
- 1 <= T <= 100
- 1 <= X, Y <= 6

Example:
Input:
4
1 4
3 4
4 2
2 6

Output:
NO
YES
NO
YES
"""

import sys

def is_good_turn(x: int, y: int) -> str:
    """
    Check if the sum of dice rolls exceeds 6.
    
    Time Complexity: O(1) per test case.
    Space Complexity: O(1).
    """
    return "YES" if (x + y) > 6 else "NO"


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
        results.append(is_good_turn(x, y))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [(1, 4), (3, 4), (4, 2), (2, 6)]
    for x, y in test_cases:
        print(f"X = {x}, Y = {y}, Sum = {x + y} -> {is_good_turn(x, y)}")
