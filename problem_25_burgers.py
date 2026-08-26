"""
Problem 25: Maximum Burgers
---------------------------
Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty and 1 bun.
Find the maximum number of burgers that Chef can make.

Input Format:
- The first line contains an integer T — the number of test cases.
- Each test case contains two space-separated integers A and B (patties and buns).

Output Format:
- For each test case, output the maximum number of burgers that Chef can make.

Constraints:
- 1 <= T <= 1000
- 1 <= A, B <= 10^5

Example:
Input:
4
2 2
2 3
3 2
23 17

Output:
2
2
2
17
"""

import sys

def max_burgers(a: int, b: int) -> int:
    """
    Since each burger requires 1 patty and 1 bun, the limiting ingredient
    determines the maximum number of burgers made: min(a, b).
    
    Time Complexity: O(1) per test case.
    Space Complexity: O(1).
    """
    return min(a, b)


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
        idx += 2
        results.append(str(max_burgers(a, b)))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [(2, 2), (2, 3), (3, 2), (23, 17)]
    for a, b in test_cases:
        print(f"Patties: {a}, Buns: {b} -> Max Burgers: {max_burgers(a, b)}")
