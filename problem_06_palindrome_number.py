"""
Problem 6: Palindrome Number
----------------------------
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right: -121. From right to left: 121-. Not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left.

Constraints:
- -2^31 <= x <= 2^31 - 1
"""

def isPalindrome(x: int) -> bool:
    """
    Mathematical Half-Reversal Approach (Without String Conversion):
    -----------------------------------------------------------------
    1. Negative numbers can never be palindromes (due to leading '-').
    2. Numbers ending in 0 (except 0 itself) cannot be palindromes (leading 0 is invalid).
    3. We can reverse only the second half of the number and compare it with the first half.
       When `x <= reversed_half`, we have reached the middle!
    4. For even length (e.g. 1221), x == reversed_half (12 == 12).
       For odd length (e.g. 12321), x == reversed_half // 10 (12 == 123 // 10).
    
    Time Complexity: O(log10(n)) - We divide the number by 10 in every step.
    Space Complexity: O(1) - No string conversion or extra memory.
    """
    # Negative numbers or numbers ending with 0 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
        
    # Check for both even-digit and odd-digit numbers
    return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    test_cases = [121, -121, 10, 0, 1221, 1234321, 1000021]
    for num in test_cases:
        print(f"x = {num:<10} -> isPalindrome: {isPalindrome(num)}")
