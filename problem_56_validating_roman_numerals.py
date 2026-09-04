"""
Problem 56: Validating Roman Numerals (Regex Validation)
-------------------------------------------------------
You are given a string, and you have to validate whether it's a valid Roman numeral.
If it is valid, print True. Otherwise, print False.
Try to create a regular expression for a valid Roman numeral.

Constraints:
- The number will be between 1 and 3999 (both included).

Input Format:
- A single line of input containing a string of Roman characters.

Output Format:
- Output a single line containing True or False.

Sample Input:
CDXXI

Sample Output:
True
"""

import re
import sys


def is_valid_roman_numeral(s: str) -> bool:
    """
    Validates Roman numerals between 1 and 3999 using standard grammatical regex breakdown.

    Grammar Components:
    -------------------
    - Thousands:  M{0,3}                -> Matches 0, 1000 (M), 2000 (MM), 3000 (MMM)
    - Hundreds:   (C[MD]|D?C{0,3})      -> Matches 100-900 (C, CC, CCC, CD, D, DC, DCC, DCCC, CM)
    - Tens:       (X[CL]|L?X{0,3})      -> Matches 10-90 (X, XX, XXX, XL, L, LX, LXX, LXXX, XC)
    - Units:      (I[XV]|V?I{0,3})      -> Matches 1-9 (I, II, III, IV, V, VI, VII, VIII, IX)

    To ensure non-empty strings (since 1 <= N <= 3999), we enforce `len(s) > 0`.

    Time Complexity:
    ----------------
    - O(L) where L is the string length (at most 15 characters for Roman numerals <= 3999).

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    if not s:
        return False

    pattern = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"
    return bool(re.fullmatch(pattern, s))


def main():
    line = sys.stdin.read().strip()
    if line:
        print(is_valid_roman_numeral(line))


if __name__ == "__main__":
    test_cases = [
        ("CDXXI", True),
        ("MMMDCCCLXXXVIII", True),
        ("IV", True),
        ("IX", True),
        ("XL", True),
        ("XC", True),
        ("CD", True),
        ("CM", True),
        ("IIII", False),
        ("VV", False),
        ("LL", False),
        ("MMMM", False),
        ("", False),
        ("ABC", False),
    ]
    for numeral, expected in test_cases:
        res = is_valid_roman_numeral(numeral)
        print(f"Numeral: '{numeral}' -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for '{numeral}': got {res}, expected {expected}"
    print("All Roman numeral tests passed successfully!")
