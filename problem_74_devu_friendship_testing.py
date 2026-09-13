"""
Problem 74: Devu and Friendship Testing
---------------------------------------
Devu has n weird friends. Today is his birthday.
His friends will break their friendship unless Devu gives them a grand party on their chosen day.
The i-th friend will break friendship if he does not receive a grand party on day d_i.

Devu can give AT MOST ONE grand party daily, and can invite ONLY ONE person per party.
Find the maximum number of friendships Devu can save.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of 2 lines:
  - First line contains integer n (number of friends).
  - Second line contains n space-separated integers d1, d2, ..., dn.

Output Format:
- For each test case, print a single line corresponding to the maximum friendships saved.

Constraints:
- 1 <= T <= 10^4
- 1 <= n <= 50
- 1 <= di <= 100

Sample Input:
2
2
3 2
2
1 1

Sample Output:
2
1
"""

import sys
from typing import List


def max_friendships_saved(days: List[int]) -> int:
    """
    Computes the maximum friendships saved by hosting at most one party per day for one friend.

    Algorithmic Insight:
    --------------------
    - Each friend demands a party on day d_i.
    - If multiple friends demand a party on the EXACT same day, Devu can invite at most ONE
      of them on that day.
    - Conversely, for every distinct day requested, Devu can host a party and save one friend.
    - Therefore, the maximum number of friends Devu can save is simply the number of UNIQUE days:
        max_saved = len(set(days))

    Time Complexity:
    ----------------
    - O(N): Constructing a set of days.

    Space Complexity:
    -----------------
    - O(N): Storage for unique days in the hash set.
    """
    return len(set(days))


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
        days = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(str(max_friendships_saved(days)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([3, 2], 2),
        ([1, 1], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 5, 5, 5], 1),
        ([10, 20, 10, 30, 20], 3),
    ]
    for days_list, expected in test_cases:
        res = max_friendships_saved(days_list)
        print(f"Days: {days_list} -> Max Saved: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {days_list}: got {res}, expected {expected}"
    print("All Devu Friendship Testing tests passed successfully!")
