"""
Problem 46: Athlete Sort (Stable Sorting on K-th Attribute)
-----------------------------------------------------------
You are given a spreadsheet that contains a list of N athletes and their details
(such as age, height, weight and so on). You are required to sort the data based on
the Kth attribute and print the final resulting table.
Note that K is indexed from 0 to M - 1, where M is the number of attributes.
Note: If two attributes are the same for different rows, print the row that appeared
first in the input (stable sort).

Input Format:
- The first line contains N and M separated by a space.
- The next N lines each contain M elements.
- The last line contains K.

Constraints:
- 1 <= N, M <= 1000
- 0 <= K < M
- Each element <= 1000

Output Format:
- Print the N lines of the sorted table. Each line should contain the space separated elements.

Sample Input:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""

import sys


def sort_athlete_table(table: list[list[int]], k: int) -> list[list[int]]:
    """
    Sorts a 2D table of athlete records stably according to the k-th attribute.

    Approach:
    ---------
    Python's built-in `sorted()` and `.sort()` use Timsort, which is guaranteed
    to be a stable sort (elements with equal keys retain their relative initial order).
    By providing `key=lambda row: row[k]`, rows are sorted purely by their k-th element.

    Time Complexity:
    ----------------
    - O(N log N) comparison time for N rows using Timsort.

    Space Complexity:
    -----------------
    - O(N * M) to hold and return the sorted records.
    """
    return sorted(table, key=lambda row: row[k])


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n, m = map(int, lines[0].split())
    table = [list(map(int, lines[1 + i].split())) for i in range(n)]
    k = int(lines[1 + n].strip())
    sorted_table = sort_athlete_table(table, k)
    for row in sorted_table:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    sample_table = [
        [10, 2, 5],
        [7, 1, 0],
        [9, 9, 9],
        [1, 23, 12],
        [6, 5, 9],
    ]
    k = 1
    sorted_res = sort_athlete_table(sample_table, k)
    expected = [
        [7, 1, 0],
        [10, 2, 5],
        [6, 5, 9],
        [9, 9, 9],
        [1, 23, 12],
    ]
    print(f"Sorted on K={k}:")
    for r in sorted_res:
        print(" ".join(map(str, r)))
    assert sorted_res == expected, f"Mismatch in sorted table!"
    print("Athlete sort test passed successfully!")
