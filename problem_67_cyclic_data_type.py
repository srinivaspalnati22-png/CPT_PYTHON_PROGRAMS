"""
Problem 67: Cyclic Data Type
-----------------------------
Hari wants to store numerical data on his computer.
He is using a new data type that can store values only from 0 till N both inclusive.
If this data type receives a value greater than N, it is cyclically converted to fit into the range 0 to N:
- Value N + 1 is stored as 0
- Value N + 2 is stored as 1
and so on...

Given N and X, determine what will be the actual value stored in memory.

Input Format:
- First line contains T, the number of test cases.
- Each test case contains two space-separated integers N and X.

Output Format:
- For each test case, output in a single line the value stored in memory.

Constraints:
- 1 <= T <= 3000
- 1 <= N <= 50
- 0 <= X <= 50

Sample Input:
5
15 0
15 10
11 12
27 37
50 49

Sample Output:
0
10
0
9
49
"""

import sys


def cyclic_storage_value(n: int, x: int) -> int:
    """
    Computes the cyclic value stored in a register with capacity [0, N].

    Mathematical Insight:
    ---------------------
    - The available values are 0, 1, 2, ..., N, which totals (N + 1) distinct states.
    - Whenever the counter reaches N + 1, it wraps around to 0.
    - Therefore, the value stored is isomorphic to modular arithmetic with modulus (N + 1):
        stored_value = X % (N + 1)

    Time Complexity:
    ----------------
    - O(1): Constant time modulo operation.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    return x % (n + 1)


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
        results.append(str(cyclic_storage_value(n, x)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ((15, 0), 0),
        ((15, 10), 10),
        ((11, 12), 0),
        ((27, 37), 9),
        ((50, 49), 49),
        ((5, 6), 0),
        ((5, 11), 5),
    ]
    for (n_val, x_val), expected in test_cases:
        res = cyclic_storage_value(n_val, x_val)
        print(f"N: {n_val}, X: {x_val} -> Stored: {res} (Expected: {expected})")
        assert res == expected, f"Failed for N={n_val}, X={x_val}: got {res}, expected {expected}"
    print("All Cyclic Data Type tests passed successfully!")
