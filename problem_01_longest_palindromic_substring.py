"""
Problem 1: Longest Palindromic Substring
-----------------------------------------
Given a string s, return the longest Palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab" (or "aba")

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.
"""

def longestPalindrome(s: str) -> str:
    """
    Expand Around Center Approach:
    -------------------------------
    A palindrome mirrors around its center. A string of length n has 2n - 1 centers:
    - n single-character centers (odd-length palindromes, e.g. "aba" centered at 'b')
    - n - 1 between-character centers (even-length palindromes, e.g. "abba" centered between 'b' and 'b')
    
    We expand around each potential center and keep track of the maximum length palindrome found.
    
    Time Complexity: O(n^2) - There are 2n - 1 centers, and expanding can take up to O(n).
    Space Complexity: O(1) - Constant extra space used.
    """
    if not s or len(s) < 1:
        return ""
    
    start, max_len = 0, 0

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # The length of the palindrome is (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1

    for i in range(len(s)):
        # Odd-length palindrome check (center at i)
        len1 = expand_around_center(i, i)
        # Even-length palindrome check (center between i and i + 1)
        len2 = expand_around_center(i, i + 1)
        
        curr_len = max(len1, len2)
        if curr_len > max_len:
            max_len = curr_len
            # Calculate starting index based on length
            start = i - (curr_len - 1) // 2

    return s[start : start + max_len]


if __name__ == "__main__":
    test_cases = ["babad", "cbbd", "a", "ac", "racecar"]
    for test in test_cases:
        print(f"Input: s = '{test}' -> Longest Palindrome: '{longestPalindrome(test)}'")
