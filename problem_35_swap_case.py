"""
Problem 35: sWAP cASE
---------------------
You are given a string and your task is to swap cases. In other words, convert
all lowercase letters to uppercase letters and vice versa.

Function Description:
Complete the swap_case function.
swap_case has the following parameters:
- string s: the string to modify

Returns:
- string: the modified string

Input Format:
- A single line containing a string s.

Constraints:
- 0 < len(s) <= 1000

Sample Input 0:
NriiT PresEnts CodinG ClaSses

Sample Output 0:
nRIIt pRESeNTS cODINg cLAsSES
"""

import sys

def swap_case(s: str) -> str:
    """
    Case Swapping:
    --------------
    Iterate over each character in the string:
    - If uppercase, convert to lowercase.
    - If lowercase, convert to uppercase.
    - Non-alphabetic characters remain unchanged.

    Can be implemented via `s.swapcase()` or explicitly via ASCII / character comparisons:
        ''.join(c.lower() if c.isupper() else c.upper() for c in s)

    Time Complexity: O(N) where N is the length of string s.
    Space Complexity: O(N) to store the resulting transformed string.
    """
    return s.swapcase()


def swap_case_manual(s: str) -> str:
    """Manual character-by-character transformation demonstration."""
    result = []
    for char in s:
        if 'a' <= char <= 'z':
            result.append(chr(ord(char) - 32))
        elif 'A' <= char <= 'Z':
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return ''.join(result)


def main():
    s = sys.stdin.read().rstrip('\r\n')
    if s:
        print(swap_case(s))


if __name__ == "__main__":
    sample_inputs = [
        "NriiT PresEnts CodinG ClaSses",
        "HackerRank.com presents 'Pythonist 2'.",
        "Hello World 123!"
    ]
    for text in sample_inputs:
        print(f"Original: {text}")
        print(f"Swapped:  {swap_case(text)}\n")
