"""
Problem 52: Compress the String! (Run-Length Encoding via itertools.groupby)
--------------------------------------------------------------------------
You are given a string S. Suppose a character 'c' occurs consecutively X times
in the string. Replace these consecutive occurrences of the character 'c' with (X, c)
in the string.

Input Format:
- A single line of input consisting of the string S.

Constraints:
- All the characters of S denote integers between 0 and 9.
- 1 <= |S| <= 10^4

Output Format:
- A single line of output consisting of the modified string with space-separated tuples.

Sample Input:
1222311

Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)
"""

import sys
from itertools import groupby


def compress_string(s: str) -> list[tuple[int, int]]:
    """
    Performs run-length compression on consecutive characters using itertools.groupby.

    Approach:
    ---------
    `itertools.groupby(s)` aggregates consecutive identical keys:
    For each key `k` and its consecutive group `g`, the count is `len(list(g))`.
    We convert `k` to integer (as per sample format: (count, int_val)).

    Time Complexity:
    ----------------
    - O(N) where N = len(S). The string is traversed linearly once.

    Space Complexity:
    -----------------
    - O(N) to produce the grouped tuples and formatted string.
    """
    compressed = []
    for key, group in groupby(s):
        compressed.append((len(list(group)), int(key)))
    return compressed


def format_compressed_string(compressed: list[tuple[int, int]]) -> str:
    """Formats tuples into space-separated string '(count, value)'."""
    return " ".join(f"({count}, {val})" for count, val in compressed)


def main():
    line = sys.stdin.read().strip()
    if line:
        result = compress_string(line)
        print(format_compressed_string(result))


if __name__ == "__main__":
    sample_input = "1222311"
    compressed = compress_string(sample_input)
    formatted = format_compressed_string(compressed)
    expected = "(1, 1) (3, 2) (1, 3) (2, 1)"
    print(f"Input:     '{sample_input}'")
    print(f"Formatted: '{formatted}'")
    print(f"Expected:  '{expected}'")
    assert formatted == expected, f"Mismatch: expected {expected}, got {formatted}"
    print("Compress the string test passed successfully!")
