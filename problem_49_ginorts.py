"""
Problem 49: ginortS (Custom Multi-Criteria String Sorting)
---------------------------------------------------------
You are given a string S containing alphanumeric characters only.
Your task is to sort the string in the following manner:
1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.

Input Format:
- A single line of input contains the string S.

Constraints:
- 0 < len(S) < 1000

Output Format:
- Output the sorted string S.

Sample Input:
Sorting1234

Sample Output:
ginortS1324
"""

import sys


def sort_ginorts(s: str) -> str:
    """
    Sorts alphanumeric characters using custom composite priority keys.

    Sorting Criteria:
    -----------------
    We assign a category rank to each character `c`:
    - Rank 0: Lowercase letters (c.islower())
    - Rank 1: Uppercase letters (c.isupper())
    - Rank 2: Odd digits (c.isdigit() and int(c) % 2 != 0)
    - Rank 3: Even digits (c.isdigit() and int(c) % 2 == 0)

    The sort key is `(category_rank, c)`.
    Since Python sorts tuples lexicographically, it first orders by rank (0 < 1 < 2 < 3),
    and within the same rank, orders characters in ascending ASCII / natural order.

    Time Complexity:
    ----------------
    - O(L log L) where L = len(S), via Timsort.

    Space Complexity:
    -----------------
    - O(L) to construct the output string.
    """
    def get_char_key(c: str):
        if c.islower():
            return (0, c)
        elif c.isupper():
            return (1, c)
        elif c.isdigit() and int(c) % 2 != 0:
            return (2, c)
        else:
            return (3, c)

    return "".join(sorted(s, key=get_char_key))


def main():
    line = sys.stdin.read().strip()
    if line:
        print(sort_ginorts(line))


if __name__ == "__main__":
    sample_input = "Sorting1234"
    result = sort_ginorts(sample_input)
    expected = "ginortS1324"
    print(f"Input:    '{sample_input}'")
    print(f"Result:   '{result}'")
    print(f"Expected: '{expected}'")
    assert result == expected, f"Mismatch: expected {expected}, got {result}"
    print("ginortS test passed successfully!")
