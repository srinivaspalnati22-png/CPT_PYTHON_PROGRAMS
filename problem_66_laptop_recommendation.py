"""
Problem 66: Laptop Recommendation
----------------------------------
Ram wants to buy a new laptop. There are 10 different laptops numbered 1 to 10.
He asks his N friends for their recommendations. The i-th friend recommends laptop Ai (1 <= Ai <= 10).

Ram will buy the laptop which is recommended by the maximum number of friends.
Determine which laptop Ram buys.
If there are multiple laptops with the maximum number of recommendations, print CONFUSED.

Input Format:
- The first line contains an integer T - the number of test cases.
- Each test case consists of 2 lines:
  - First line contains N - the number of friends.
  - Second line contains N space-separated integers A1, A2, ..., AN.

Output Format:
- For each test case, output the laptop number or CONFUSED.

Constraints:
- 1 <= T <= 200
- 1 <= N <= 1000
- 1 <= Ai <= 10

Sample Input:
4
5
4 4 4 2 1
7
1 2 3 4 5 6 6
6
2 2 3 3 10 8
4
7 7 8 8

Sample Output:
4
6
CONFUSED
CONFUSED
"""

import sys
from collections import Counter
from typing import List


def best_laptop(recommendations: List[int]) -> str:
    """
    Finds the laptop with the maximum recommendations, or 'CONFUSED' if there is a tie.

    Algorithm:
    ----------
    - Count the frequency of each recommended laptop.
    - Find the maximum frequency.
    - Identify all laptops achieving this maximum frequency.
    - If there is exactly one such laptop, return its ID as string.
    - Otherwise, return 'CONFUSED'.

    Time Complexity:
    ----------------
    - O(N): Linear count of recommendations. Since laptop IDs are in [1, 10], counts take O(N + 10) time.

    Space Complexity:
    -----------------
    - O(1): Fixed hash map size of at most 10 keys.
    """
    freq = Counter(recommendations)
    max_count = max(freq.values())
    top_laptops = [laptop for laptop, count in freq.items() if count == max_count]

    if len(top_laptops) == 1:
        return str(top_laptops[0])
    return "CONFUSED"


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
        recs = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(best_laptop(recs))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([4, 4, 4, 2, 1], "4"),
        ([1, 2, 3, 4, 5, 6, 6], "6"),
        ([2, 2, 3, 3, 10, 8], "CONFUSED"),
        ([7, 7, 8, 8], "CONFUSED"),
        ([1], "1"),
        ([9, 9, 9, 9], "9"),
    ]
    for arr, expected in test_cases:
        res = best_laptop(arr)
        print(f"Recommendations: {arr} -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Laptop Recommendation tests passed successfully!")
