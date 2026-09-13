"""
Problem 65: John's Final Position on X-Axis
------------------------------------------
Initially, John is at coordinate 0 on the X-axis.
For each i = 1, 2, ..., N in order:
- If John is at a non-negative coordinate (pos >= 0), he moves i steps backward:
    pos -= i
- Otherwise (pos < 0), he moves i steps forward:
    pos += i

Given integer N, find the final position of John on the X-axis after N operations.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of a single line containing an integer N.

Output Format:
- For each test case, output in a single line the final position after N operations.

Constraints:
- 1 <= T <= 10^5
- 1 <= N <= 10^9

Sample Input:
3
1
2
3

Sample Output:
-1
1
-2
"""

import sys


def final_position(n: int) -> int:
    """
    Computes John's coordinate on the X-axis after N alternating operations.

    Pattern Derivation:
    -------------------
    Let's trace the state (i, pos_after_i) starting at coordinate 0:
    - Initially: pos = 0 (>= 0)
    - i = 1: pos >= 0 -> pos = 0 - 1 = -1  (< 0)
    - i = 2: pos < 0  -> pos = -1 + 2 = +1 (>= 0)
    - i = 3: pos >= 0 -> pos = 1 - 3 = -2  (< 0)
    - i = 4: pos < 0  -> pos = -2 + 4 = +2 (>= 0)
    - i = 5: pos >= 0 -> pos = 2 - 5 = -3  (< 0)
    - i = 6: pos < 0  -> pos = -3 + 6 = +3 (>= 0)
    - i = 7: pos >= 0 -> pos = 3 - 7 = -4  (< 0)
    - i = 8: pos < 0  -> pos = -4 + 8 = +4 (>= 0)

    Closed-form Invariant:
    ----------------------
    - If N is even: pos = N // 2
    - If N is odd:  pos = -((N + 1) // 2)

    Time Complexity:
    ----------------
    - O(1): Closed-form arithmetic expression.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return -((n + 1) // 2)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str(final_position(n)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        (1, -1),
        (2, 1),
        (3, -2),
        (4, 2),
        (5, -3),
        (6, 3),
        (7, -4),
        (10**9, 500000000),
        (10**9 + 1, -500000001),
    ]
    for n_val, expected in test_cases:
        res = final_position(n_val)
        print(f"N: {n_val} -> Final Pos: {res} (Expected: {expected})")
        assert res == expected, f"Failed for N={n_val}: got {res}, expected {expected}"
    print("All Final Position on X-axis tests passed successfully!")
