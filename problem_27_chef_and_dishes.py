"""
Problem 27: Chef and Dishes
---------------------------
Chef will have N guests in his house today. He wants to serve at least one dish to each guest.
Chef can make two types of dishes:
1. Dish Type 1: 1 Fruit + 1 Vegetable
2. Dish Type 2: 1 Vegetable + 1 Fish

Chef has A fruits, B vegetables, and C fishes in his house.
Can he prepare at least N dishes in total?

Input Format:
- First line contains T — the number of test cases.
- Each test case contains four integers: N, A, B, C.

Output Format:
- For each test case, print "YES" if Chef can prepare at least N dishes, otherwise print "NO".

Constraints:
- 1 <= T <= 100
- 1 <= N, A, B, C <= 100

Example:
Input:
4
2 1 2 1
3 2 2 2
4 2 6 3
3 1 3 1

Output:
YES
NO
YES
NO
"""

import sys

def can_serve_guests(n: int, a: int, b: int, c: int) -> str:
    """
    Analysis:
    ---------
    - Every dish (either Type 1 or Type 2) requires exactly 1 vegetable.
    - Type 1 requires 1 fruit, Type 2 requires 1 fish.
    - Total dishes made cannot exceed total vegetables (B).
    - Total dishes made cannot exceed total fruits + fishes (A + C).
    
    Therefore, Max Dishes = min(B, A + C).
    Chef can serve N guests if min(B, A + C) >= N.
    
    Time Complexity: O(1) per testcase.
    Space Complexity: O(1).
    """
    max_dishes = min(b, a + c)
    return "YES" if max_dishes >= n else "NO"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        a = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        c = int(input_data[idx + 3])
        idx += 4
        results.append(can_serve_guests(n, a, b, c))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        (2, 1, 2, 1),
        (3, 2, 2, 2),
        (4, 2, 6, 3),
        (3, 1, 3, 1)
    ]
    for n, a, b, c in test_cases:
        print(f"N={n}, A={a}, B={b}, C={c} -> {can_serve_guests(n, a, b, c)}")
