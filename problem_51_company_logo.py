"""
Problem 51: Company Logo (collections.Counter & Secondary Sort)
--------------------------------------------------------------
A newly opened multinational brand has decided to base their company logo on
the three most common characters in the company name.
Given a string s, which is the company name in lowercase letters, your task is to
find the top three most common characters in the string.

Sorting Criteria:
- Sort in descending order of occurrence count (-count).
- If the occurrence count is the same, sort the characters in alphabetical order (+char).

Input Format:
- A single line of input containing the string S.

Constraints:
- 3 < len(S) <= 10^4
- S has at least 3 distinct characters

Output Format:
- Print the three most common characters along with their occurrence count, each on a separate line.

Sample Input:
aabbbccde

Sample Output:
b 3
a 2
c 2
"""

import sys
from collections import Counter


def find_company_logo(s: str) -> list[tuple[str, int]]:
    """
    Finds the top 3 characters by occurrence count, breaking ties alphabetically.

    Approach:
    ---------
    1. Count frequencies using `collections.Counter(s)`.
    2. Sort the `(char, count)` items using a custom key:
           `key=lambda item: (-item[1], item[0])`
       - `-item[1]`: Higher frequency comes first.
       - `item[0]`: For equal frequencies, smaller alphabetical character comes first.
    3. Take the first 3 items of the sorted list.

    Time Complexity:
    ----------------
    - O(N + U log U) where N = len(S) and U <= 26 is the number of distinct characters.
      Since U <= 26, sorting is O(1) in practice.

    Space Complexity:
    -----------------
    - O(U) for the frequency table (at most 26 lowercase English letters).
    """
    counts = Counter(s)
    sorted_chars = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_chars[:3]


def main():
    line = sys.stdin.read().strip()
    if line:
        top3 = find_company_logo(line)
        for char, count in top3:
            print(f"{char} {count}")


if __name__ == "__main__":
    sample_input = "aabbbccde"
    result = find_company_logo(sample_input)
    expected = [("b", 3), ("a", 2), ("c", 2)]
    print(f"Input: '{sample_input}'")
    print("Top 3 Logo Characters:")
    for ch, cnt in result:
        print(f"{ch} {cnt}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("Company logo test passed successfully!")
