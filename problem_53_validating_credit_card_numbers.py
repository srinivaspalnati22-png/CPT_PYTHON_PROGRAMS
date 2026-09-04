"""
Problem 53: Validating Credit Card Numbers (Regex Pattern Matching)
-------------------------------------------------------------------
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not.

A valid credit card from ABCD Bank has the following characteristics:
- It must start with a 4, 5, or 6.
- It must contain exactly 16 digits.
- It must only consist of digits (0-9).
- It may have digits in groups of 4, separated by one hyphen '-'.
- It must NOT use any other separator like ' ', '_', etc.
- It must NOT have 4 or more consecutive repeated digits (consecutively across separators).

Input Format:
- The first line contains an integer N.
- The next N lines contain credit card numbers.

Constraints:
- 0 < N < 100

Output Format:
- Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'.

Sample Input:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid
"""

import re
import sys


def validate_credit_card(card: str) -> str:
    """
    Validates a credit card number against structure and repetition constraints.

    Validation Rules:
    -----------------
    1. Structure Check:
       `r"^[456](\\d{15}|\\d{3}(-\\d{4}){3})$"`
       - Must start with 4, 5, or 6.
       - Must either be 16 consecutive digits or four blocks of 4 digits separated by single hyphens.
    2. Consecutive Repetition Check:
       Strip all hyphens, then check for 4 or more identical consecutive digits:
       `r"(\\d)\\1{3}"`
       If any match is found, the card is invalid.

    Time Complexity:
    ----------------
    - O(L) where L is the length of the credit card string (around 16-19 chars) -> O(1).

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    structure_pattern = r"^[456](\d{15}|\d{3}(-\d{4}){3})$"
    if not re.match(structure_pattern, card):
        return "Invalid"

    cleaned_digits = card.replace("-", "")
    consecutive_repeat_pattern = r"(\d)\1{3}"
    if re.search(consecutive_repeat_pattern, cleaned_digits):
        return "Invalid"

    return "Valid"


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    for i in range(1, n + 1):
        if i < len(lines):
            print(validate_credit_card(lines[i].strip()))


if __name__ == "__main__":
    test_cards = [
        ("4123456789123456", "Valid"),
        ("5123-4567-8912-3456", "Valid"),
        ("61234-567-8912-3456", "Invalid"),
        ("4123356789123456", "Valid"),
        ("5133-3367-8912-3456", "Invalid"),
        ("5123 - 3567 - 8912 - 3456", "Invalid"),
        ("4424444424442444", "Invalid"),
        ("0525362587961578", "Invalid"),
    ]
    for card, expected in test_cards:
        res = validate_credit_card(card)
        print(f"Card: '{card}' -> {res} (Expected: {expected})")
        assert res == expected, f"Failed for {card}: got {res}, expected {expected}"
    print("Credit card validation tests passed successfully!")
