"""
Problem 50: Set .add() (Distinct Country Stamps)
-----------------------------------------------
Rupal has a huge collection of country stamps. She decided to count the total
number of distinct country stamps in her collection.
She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.

Input Format:
- The first line contains an integer N, the total number of country stamps.
- The next N lines contain the name of the country where the stamp is from.

Constraints:
- 0 < N < 1000

Output Format:
- Output the total number of distinct country stamps on a single line.

Sample Input:
7
UK
China
USA
France
New Zealand
UK
France

Sample Output:
5
"""

import sys


def count_distinct_stamps(stamps: list[str]) -> int:
    """
    Finds the number of unique country stamps using a set collection.

    Approach:
    ---------
    Sets in Python store only unique elements using an underlying hash table.
    We can insert each stamp into a set using `.add()` or by converting the list to a set.
    The cardinality `len(distinct_stamps)` gives the answer.

    Time Complexity:
    ----------------
    - O(N * L) where N is the number of stamps and L is the average string length.
      Each hash lookup and insertion takes O(L) on average.

    Space Complexity:
    -----------------
    - O(U * L) where U <= N is the number of unique countries.
    """
    distinct_stamps = set()
    for stamp in stamps:
        distinct_stamps.add(stamp.strip())
    return len(distinct_stamps)


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    stamps = [lines[1 + i] for i in range(n) if 1 + i < len(lines)]
    print(count_distinct_stamps(stamps))


if __name__ == "__main__":
    sample_stamps = [
        "UK",
        "China",
        "USA",
        "France",
        "New Zealand",
        "UK",
        "France",
    ]
    result = count_distinct_stamps(sample_stamps)
    print(f"Stamps: {sample_stamps}")
    print(f"Distinct Count: {result} (Expected: 5)")
    assert result == 5, f"Expected 5, got {result}"
    print("Distinct stamps test passed successfully!")
