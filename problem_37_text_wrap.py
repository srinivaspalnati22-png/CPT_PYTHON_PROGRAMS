"""
Problem 37: Text Wrap
---------------------
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Input Format:
- The first line contains a string, S.
- The second line contains the width, w.

Constraints:
- 0 < len(S) < 1000
- 0 < w < len(S)

Output Format:
- Print the text wrapped paragraph.

Sample Input 0:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

import sys
import textwrap

def wrap(string: str, max_width: int) -> str:
    """
    Paragraph Wrapping:
    -------------------
    Uses Python's standard `textwrap.fill` or chunked slicing to wrap a string into
    lines of length at most `max_width`.

    Custom slicing implementation:
        return "\\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])

    Time Complexity: O(N) where N is len(string).
    Space Complexity: O(N) to hold the output string with newline characters.
    """
    return textwrap.fill(string, max_width)


def wrap_manual(string: str, max_width: int) -> str:
    """Explicit chunking using slice generator."""
    lines = [string[i:i + max_width] for i in range(0, len(string), max_width)]
    return "\n".join(lines)


def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 2:
        string = lines[0]
        max_width = int(lines[1])
        print(wrap(string, max_width))


if __name__ == "__main__":
    sample_s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    sample_w = 4
    print(f"String: {sample_s}, Width: {sample_w}\nWrapped Output:")
    print(wrap(sample_s, sample_w))
