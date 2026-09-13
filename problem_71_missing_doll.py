"""
Problem 71: Missing Doll (Chef and Dolls)
----------------------------------------
Swathi is a fan of pairs and likes all things that come in pairs.
He has a doll collection in which the dolls come in pairs.
One day while going through his collection he found an odd number of dolls.
Someone had stolen a doll!
Find which type of doll is missing (i.e. does not have a pair).

Input Format:
- The first line contains an integer T, the number of test cases.
- For each test case:
  - The first line contains an integer N, the number of dolls remaining.
  - The next N lines contain the types of dolls.

Output Format:
- For each test case, display the type of doll that doesn't have a pair.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 100000 (10^5)
- 0 <= type <= 100000

Sample Input:
1
3
1
2
1

Sample Output:
2
"""

import sys
from typing import List


def find_missing_doll(dolls: List[int]) -> int:
    """
    Finds the doll type that appears an odd number of times using bitwise XOR.

    Algorithmic Principle:
    ----------------------
    - Every doll type that comes in pairs appears an even number of times.
    - Exactly one doll type appears an odd number of times (missing its partner).
    - By the algebraic properties of XOR:
        x ^ x = 0 (pairs cancel each other out)
        x ^ 0 = x
    - Taking the cumulative XOR of all doll types yields the unique unpaired doll type:
        result = doll_1 ^ doll_2 ^ ... ^ doll_N

    Time Complexity:
    ----------------
    - O(N): Single pass through the list of doll types.

    Space Complexity:
    -----------------
    - O(1): Only a single accumulator variable.
    """
    unpaired = 0
    for doll in dolls:
        unpaired ^= doll
    return unpaired


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
        dolls = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(str(find_missing_doll(dolls)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 1], 2),
        ([5], 5),
        ([1, 1, 2, 2, 3], 3),
        ([10, 20, 30, 20, 10], 30),
        ([4, 4, 4], 4),
    ]
    for arr, expected in test_cases:
        res = find_missing_doll(arr)
        print(f"Dolls: {arr} -> Missing: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Missing Doll tests passed successfully!")
