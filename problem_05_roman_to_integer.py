"""
Problem 5: Roman to Integer
---------------------------
Roman numerals are represented by seven different symbols:
I (1), V (5), X (10), L (50), C (100), D (500), M (1000).

Given a roman numeral string s, convert it to an integer.

Special subtraction rules:
- I before V (5) and X (10) makes 4 and 9.
- X before L (50) and C (100) makes 40 and 90.
- C before D (500) and M (1000) makes 400 and 900.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "LVIII"
Output: 58 (L = 50, V = 5, III = 3)

Example 3:
Input: s = "MCMXCIV"
Output: 1994 (M = 1000, CM = 900, XC = 90, IV = 4)

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- Guaranteed valid roman numeral in the range [1, 3999].
"""

def romanToInt(s: str) -> int:
    """
    Left-to-Right Scan with Subtraction Comparison:
    -----------------------------------------------
    In Roman numerals, if a smaller value precedes a larger value, the smaller
    value is subtracted from the total. Otherwise, it is added.
    
    We map each roman character to its integer value and traverse the string.
    For each character at index i:
    - If value(s[i]) < value(s[i + 1]), subtract value(s[i]).
    - Else, add value(s[i]).
    
    Time Complexity: O(n) - where n is length of string (at most 15).
    Space Complexity: O(1) - fixed lookup map.
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        curr_val = roman_map[s[i]]
        # If the next character has a larger value, subtract current value
        if i + 1 < n and curr_val < roman_map[s[i + 1]]:
            total -= curr_val
        else:
            total += curr_val
            
    return total


if __name__ == "__main__":
    test_cases = ["III", "LVIII", "MCMXCIV", "IV", "IX", "XL", "XC", "CD", "CM"]
    for roman in test_cases:
        print(f"Roman: {roman:<10} -> Integer: {romanToInt(roman)}")
