"""
Problem 16: Valid Anagram
-------------------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.
"""

def isAnagram(s: str, t: str) -> bool:
    """
    Frequency Count / Hash Array Approach:
    --------------------------------------
    Two strings are anagrams if and only if they have the exact same length
    and identical character frequency distribution.
    
    We can count character occurrences using a fixed array of size 26 (for 'a' through 'z').
    - Increment count for characters in s.
    - Decrement count for characters in t.
    - If all counts remain 0, they are anagrams.
    
    Time Complexity: O(n) - Single pass through both strings.
    Space Complexity: O(1) - Fixed size array of 26 integers.
    """
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for c1, c2 in zip(s, t):
        count[ord(c1) - ord('a')] += 1
        count[ord(c2) - ord('a')] -= 1
        
    return all(x == 0 for x in count)


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("aacc", "ccac"),
        ("listen", "silent")
    ]
    for s, t in test_cases:
        print(f"s = '{s}', t = '{t}' -> isAnagram: {isAnagram(s, t)}")
