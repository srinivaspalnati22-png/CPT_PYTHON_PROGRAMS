"""
Problem 72: Make All Elements Equal (Minimum Operations)
--------------------------------------------------------
You are given an array A of size N. In one operation, you can do the following:
Select indices i and j (i != j) and set A[i] = A[j].

Find the minimum number of operations required to make all elements of the array equal.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of 2 lines:
  - First line contains N — the size of the array.
  - Second line contains N space-separated integers, denoting array A.

Output Format:
- For each test case, output on a new line the minimum number of operations.

Constraints:
- 1 <= T <= 1000
- 1 <= N <= 2 * 10^5
- 1 <= Ai <= N
- The sum of N over all test cases <= 2 * 10^5

Sample Input:
3
3
1 2 3
4
2 2 3 1
4
3 1 2 4

Sample Output:
2
2
3
"""

import sys
from collections import Counter
from typing import List


def min_operations_to_equal(arr: List[int]) -> int:
    """
    Finds the minimum operations to make all elements equal by assigning A[i] = A[j].

    Algorithmic Principle:
    ----------------------
    - In each operation, exactly one element's value is changed to match another element.
    - To minimize the number of modifications, we should preserve the value that already
      appears most frequently in the array.
    - Let max_freq be the maximum occurrence frequency of any element in A.
    - All remaining elements (N - max_freq elements) must each be changed at least once.
    - Each operation can convert one mismatched element into the target element.
    - Therefore, the minimum number of operations required is:
        min_operations = N - max_freq

    Time Complexity:
    ----------------
    - O(N): Counting frequencies across the array of length N.

    Space Complexity:
    -----------------
    - O(U): Auxiliary space for the frequency table where U <= N is the number of distinct elements.
    """
    if not arr:
        return 0
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(str(min_operations_to_equal(arr)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 2),
        ([2, 2, 3, 1], 2),
        ([3, 1, 2, 4], 3),
        ([5, 5, 5, 5], 0),
        ([7], 0),
        ([1, 2, 2, 2, 3, 3], 3),
    ]
    for arr, expected in test_cases:
        res = min_operations_to_equal(arr)
        print(f"Array: {arr} -> Min Ops: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Make All Elements Equal tests passed successfully!")
