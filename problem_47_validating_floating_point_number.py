"""
Problem 47: Validating Floating Point Number (Regular Expressions)
-----------------------------------------------------------------
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:
1. Number can start with +, - or . symbol.
   Valid: +4.50, -1.0, .5, -.7, +.4
   Invalid: -+4.5
2. Number must contain at least 1 decimal value after the decimal point:
   Invalid: 12.
   Valid: 12.0
3. Number must have exactly one '.' symbol.
4. Number must not give any exceptions when converted using float(N).

Input Format:
- The first line contains an integer T, the number of test cases.
- The next T lines contain a string N.

Constraints:
- 0 < T < 10

Output Format:
- Output True or False for each test case.

Sample Input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output:
False
True
True
False
"""

import re
import sys


def is_valid_float(s: str) -> bool:
    """
    Validates if a given string represents a valid floating-point number.

    Regex Breakdown:
    ----------------
    r'^[+-]?[0-9]*\.[0-9]+$'
    - ^[+-]?     : Starts with an optional '+' or '-' sign.
    - [0-9]*     : Followed by zero or more digits before the decimal point (e.g. '.5' is valid).
    - \.         : Exactly one literal '.' decimal point.
    - [0-9]+$    : At least one digit after the decimal point up to the end of string.

    We also wrap float(s) conversion in a try/except block to ensure valid numeric conversion.

    Time Complexity:
    ----------------
    - O(L) where L is the length of string s.

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    pattern = r"^[+-]?[0-9]*\.[0-9]+$"
    if not re.match(pattern, s):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    for i in range(1, t + 1):
        if i < len(lines):
            print(is_valid_float(lines[i].strip()))


if __name__ == "__main__":
    sample_tests = [
        ("4.0O0", False),
        ("-1.00", True),
        ("+4.54", True),
        ("SomeRandomStuff", False),
        (".5", True),
        ("-.7", True),
        ("+.4", True),
        ("12.", False),
        ("-+4.5", False),
    ]
    for test_str, expected in sample_tests:
        res = is_valid_float(test_str)
        print(f"'{test_str}' -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for {test_str}: got {res}, expected {expected}"
    print("All float validation tests passed successfully!")
