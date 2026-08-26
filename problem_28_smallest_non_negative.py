"""
Problem 28: Smallest Non-Negative Value
---------------------------------------
You are given two integers N and K. You may perform the following operation
any number of times (including zero): change N to N - K.
Find the smallest non-negative integer value of N you can obtain this way.

Input Format:
- The first line contains a single integer T — the number of test cases.
- Each test case contains two space-separated integers N and K.

Output Format:
- For each test case, print a single line containing one integer — the smallest value obtained.

Constraints:
- 1 <= T <= 10^5
- 1 <= N <= 10^9
- 0 <= K <= 10^9

Example:
Input:
3
5 2
4 4
2 5

Output:
1
0
2
"""

import sys

def smallest_non_negative(n: int, k: int) -> int:
    """
    Mathematical Modulo Approach:
    ------------------------------
    Repeatedly subtracting K from N until N < K (while remaining >= 0) is the definition
    of the remainder of integer division (modulo operation).
    - If K == 0, no subtraction is possible (or subtract 0), so answer is N.
    - If K > 0, the smallest non-negative value is N % K.
    
    Time Complexity: O(1) per test case.
    Space Complexity: O(1).
    """
    if k == 0:
        return n
    return n % k


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        results.append(str(smallest_non_negative(n, k)))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [(5, 2), (4, 4), (2, 5), (10, 0), (100, 30)]
    for n, k in test_cases:
        print(f"N = {n}, K = {k} -> Smallest non-negative: {smallest_non_negative(n, k)}")
