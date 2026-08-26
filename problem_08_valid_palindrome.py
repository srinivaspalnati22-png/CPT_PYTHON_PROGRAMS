"""
Problem 8: Valid Palindrome
----------------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

def isPalindrome(s: str) -> bool:
    """
    Two-Pointer Approach (In-Place Character Validation):
    -----------------------------------------------------
    Initialize two pointers: `left` at the beginning and `right` at the end.
    - Advance `left` until an alphanumeric character is found (using .isalnum()).
    - Move `right` backwards until an alphanumeric character is found.
    - Compare lowercase versions of characters at `left` and `right`.
    - If they mismatch, return False.
    - Continue until pointers cross.
    
    Time Complexity: O(n) - Single pass with two pointers.
    Space Complexity: O(1) - No filtered string copies are created.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P",
        "ab_a"
    ]
    for text in test_cases:
        print(f"s = '{text}' -> isPalindrome: {isPalindrome(text)}")
