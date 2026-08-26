"""
Problem 20: Repeated Substring Pattern
---------------------------------------
Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: Substring "abc" 4 times or "abcabc" twice.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
"""

def repeatedSubstringPattern(s: str) -> bool:
    """
    String Doubling / Rotation Trick:
    ---------------------------------
    If a string `s` is composed of repeating copies of a substring `p` (i.e. s = p * k for k >= 2),
    then concatenating `s` with itself (`s + s`) will contain copies of `s` starting at shifts that
    are multiples of len(p).
    
    If we remove the very first and very last characters from `s + s` (i.e. `(s + s)[1:-1]`),
    the original string `s` will STILL be found inside if and only if `s` is periodic!
    
    Why?
    - If s is periodic, the next period appears at index len(p) < len(s), which is inside (s + s)[1:-1].
    - If s is not periodic, the only occurrences of s in s + s are at index 0 and index len(s),
      both of which are invalidated by slicing [1:-1].
      
    Time Complexity: O(n) - String concatenation and substring search.
    Space Complexity: O(n) - To create the concatenated string.
    """
    return s in (s + s)[1:-1]


# Alternative approach using divisors & KMP LPS array
def repeatedSubstringPattern_KMP(s: str) -> bool:
    n = len(s)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    longest_prefix_suffix = lps[-1]
    # Check if remainder length divides n
    return longest_prefix_suffix > 0 and n % (n - longest_prefix_suffix) == 0


if __name__ == "__main__":
    test_cases = ["abab", "aba", "abcabcabcabc", "a", "abac"]
    for text in test_cases:
        print(f"s = '{text:<14}' -> repeated: {repeatedSubstringPattern(text)} (KMP: {repeatedSubstringPattern_KMP(text)})")
