"""
Problem 79: Alice, Bob, and Charlie's Favorite Numbers
-----------------------------------------------------
Alice likes numbers which are even and are a multiple of 7.
Bob likes numbers which are odd and are a multiple of 9.
Alice, Bob, and Charlie find a number A.
- If Alice likes A, Alice takes home the number.
- If Bob likes A, Bob takes home the number.
- If neither Alice nor Bob likes the number, Charlie takes it home.

Given A, find who takes it home: "Alice", "Bob", or "Charlie".
Note: No integer can be liked by both Alice and Bob since Alice requires even numbers
while Bob requires odd numbers.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of a single integer A.

Output Format:
- For each test case, output on a new line who takes the number home:
  "Alice", "Bob", or "Charlie".

Constraints:
- 1 <= T <= 100
- 1 <= A <= 1000

Sample Input:
8
7
14
21
18
27
63
126
8

Sample Output:
Charlie
Alice
Charlie
Charlie
Bob
Bob
Alice
Charlie
"""

import sys


def who_takes_number(a: int) -> str:
    """
    Determines whether Alice, Bob, or Charlie takes home number A.

    Rules:
    ------
    - Alice: a % 2 == 0 and a % 7 == 0 (equivalently, a % 14 == 0)
    - Bob: a % 2 != 0 and a % 9 == 0
    - Charlie: Otherwise

    Time Complexity:
    ----------------
    - O(1): Modulo operations.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    if a % 2 == 0 and a % 7 == 0:
        return "Alice"
    elif a % 2 != 0 and a % 9 == 0:
        return "Bob"
    else:
        return "Charlie"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        a = int(input_data[i])
        results.append(who_takes_number(a))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        (7, "Charlie"),
        (14, "Alice"),
        (21, "Charlie"),
        (18, "Charlie"),
        (27, "Bob"),
        (63, "Bob"),
        (126, "Alice"),
        (8, "Charlie"),
        (9, "Bob"),
        (28, "Alice"),
    ]
    for a_val, expected in test_cases:
        res = who_takes_number(a_val)
        print(f"A: {a_val} -> Recipient: {res} (Expected: {expected})")
        assert res == expected, f"Failed for A={a_val}: got {res}, expected {expected}"
    print("All Alice, Bob, and Charlie tests passed successfully!")
