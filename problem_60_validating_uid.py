"""
Problem 60: Validating UID (Unique Identification Number)
---------------------------------------------------------
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:
1. It must contain at least 2 uppercase English alphabet characters ([A-Z]).
2. It must contain at least 3 digits (0 - 9).
3. It should only contain alphanumeric characters (a-z, A-Z, & 0-9).
4. No character should repeat (all characters must be unique).
5. There must be exactly 10 characters in a valid UID.

Input Format:
- The first line contains an integer T, the number of test cases.
- The next T lines contain an employee's UID.

Output Format:
- For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid'.

Sample Input:
2
B1CD102354
B1CDEF2354

Sample Output:
Invalid
Valid
"""

import sys


def validate_uid(uid: str) -> str:
    """
    Validates employee UID against all company specifications.

    Rules Checked:
    --------------
    1. Exact length of 10: `len(uid) == 10`
    2. Only alphanumeric: `uid.isalnum()`
    3. No repeated characters: `len(set(uid)) == 10`
    4. At least 2 uppercase characters: `sum(1 for c in uid if c.isupper()) >= 2`
    5. At least 3 digits: `sum(1 for c in uid if c.isdigit()) >= 3`

    Time Complexity:
    ----------------
    - O(1): String length is fixed at 10.

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    uid = uid.strip()

    # Rule 5: Exactly 10 characters
    if len(uid) != 10:
        return "Invalid"

    # Rule 3: Only alphanumeric
    if not uid.isalnum():
        return "Invalid"

    # Rule 4: No repeated characters
    if len(set(uid)) != 10:
        return "Invalid"

    # Rule 1: At least 2 uppercase characters
    uppercase_count = sum(1 for c in uid if c.isupper())
    if uppercase_count < 2:
        return "Invalid"

    # Rule 2: At least 3 digits
    digit_count = sum(1 for c in uid if c.isdigit())
    if digit_count < 3:
        return "Invalid"

    return "Valid"


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    for i in range(1, t + 1):
        if i < len(lines):
            print(validate_uid(lines[i]))


if __name__ == "__main__":
    test_cases = [
        ("B1CD102354", "Invalid"),  # '1' repeated
        ("B1CDEF2354", "Valid"),    # Meets all rules
        ("B1CDEF235", "Invalid"),   # 9 characters
        ("b1cdef2354", "Invalid"),  # No uppercase
        ("B1cdefghij", "Invalid"),  # Less than 2 uppercase, less than 3 digits
        ("B1CD@EF235", "Invalid"),  # Special character '@'
    ]
    for uid, expected in test_cases:
        res = validate_uid(uid)
        print(f"UID: '{uid}' -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for {uid}: got {res}, expected {expected}"
    print("All UID validation tests passed successfully!")
