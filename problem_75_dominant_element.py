"""
Problem 75: Dominant Element
----------------------------
You are given an array A of length N.
An element X is said to be dominant if the frequency of X in A is strictly greater
than the frequency of ANY OTHER element in A.

Find if there exists any dominant element in A.

Input Format:
- The first line contains an integer T — the number of test cases.
- Each test case consists of 2 lines:
  - First line contains N — the size of array A.
  - Second line contains N space-separated integers A1, A2, ..., AN.

Output Format:
- For each test case, output YES if there exists any dominant element in A.
  Otherwise, output NO.

Constraints:
- 1 <= T <= 500
- 1 <= N <= 1000
- 1 <= Ai <= N

Sample Input:
4
5
2 2 2 2 2
4
1 2 3 4
4
3 3 2 1
6
1 1 2 2 3 4

Sample Output:
YES
NO
YES
NO
"""

import sys
from collections import Counter
from typing import List


def has_dominant_element(arr: List[int]) -> str:
    """
    Determines whether there is an element whose frequency strictly exceeds
    the frequency of all other elements in the array.

    Algorithmic Procedure:
    ----------------------
    - Count the occurrence frequencies of all unique elements in A.
    - Sort the frequencies in descending order: f_1 >= f_2 >= ...
    - If there is only 1 distinct element (len(frequencies) == 1), it is trivially dominant -> 'YES'.
    - If there are 2 or more distinct elements:
      - If f_1 > f_2: the top element's frequency is strictly greater than all others -> 'YES'.
      - If f_1 == f_2: at least two elements tie for the highest frequency -> 'NO'.

    Time Complexity:
    ----------------
    - O(N + U log U): Where N is array length and U <= N is number of unique elements.

    Space Complexity:
    -----------------
    - O(U): Storage for frequency counts.
    """
    if not arr:
        return "NO"
    freq = Counter(arr)
    counts = sorted(freq.values(), reverse=True)
    if len(counts) == 1:
        return "YES"
    return "YES" if counts[0] > counts[1] else "NO"


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
        results.append(has_dominant_element(arr))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([2, 2, 2, 2, 2], "YES"),
        ([1, 2, 3, 4], "NO"),
        ([3, 3, 2, 1], "YES"),
        ([1, 1, 2, 2, 3, 4], "NO"),
        ([5], "YES"),
        ([1, 1, 2, 2], "NO"),
    ]
    for arr, expected in test_cases:
        res = has_dominant_element(arr)
        print(f"Array: {arr} -> Dominant: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Dominant Element tests passed successfully!")
