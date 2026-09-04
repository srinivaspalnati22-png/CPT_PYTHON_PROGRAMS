"""
Problem 57: Validating Phone Numbers (Regex Mobile Validation)
--------------------------------------------------------------
You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7, 8 or 9.

Input Format:
- The first line contains an integer N, the number of inputs.
- N lines follow, each containing some string.

Constraints:
- 1 <= N <= 10
- 2 <= len(Number) <= 15

Output Format:
- For every string listed, print 'YES' if it is a valid mobile number and 'NO' if it is not.

Sample Input:
2
9587456281
1252478965

Sample Output:
YES
NO
"""

import re
import sys


def is_valid_mobile_number(number_str: str) -> str:
    """
    Validates a 10-digit mobile number starting with 7, 8, or 9.

    Regex Breakdown:
    ----------------
    r"^[789]\\d{9}$"
    - ^[789]  : First character must be 7, 8, or 9.
    - \\d{9}$ : Followed by exactly 9 digits, ending the string (total length = 10 digits).

    Time Complexity:
    ----------------
    - O(1) string pattern matching.

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    pattern = r"^[789]\d{9}$"
    if re.match(pattern, number_str.strip()):
        return "YES"
    return "NO"


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    for i in range(1, n + 1):
        if i < len(lines):
            print(is_valid_mobile_number(lines[i]))


if __name__ == "__main__":
    test_cases = [
        ("9587456281", "YES"),
        ("1252478965", "NO"),
        ("7894561230", "YES"),
        ("8956231470", "YES"),
        ("958745628", "NO"),       # 9 digits
        ("95874562812", "NO"),     # 11 digits
        ("78945a1230", "NO"),      # Non-digit
    ]
    for number, expected in test_cases:
        res = is_valid_mobile_number(number)
        print(f"Number: '{number}' -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for {number}: got {res}, expected {expected}"
    print("All phone number validation tests passed successfully!")
