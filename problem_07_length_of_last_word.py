"""
Problem 7: Length of Last Word
-------------------------------
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.
"""

def lengthOfLastWord(s: str) -> int:
    """
    Reverse Traversal Approach:
    ----------------------------
    Start scanning from the end of the string.
    1. Skip any trailing whitespace characters.
    2. Count characters until another space is encountered or the beginning of the string is reached.
    
    Time Complexity: O(n) - Single backward pass over characters in worst case.
    Space Complexity: O(1) - Constant space without creating split lists or new strings.
    """
    length = 0
    i = len(s) - 1
    
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
        
    # Count characters of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
        
    return length


if __name__ == "__main__":
    test_cases = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
        "a",
        "    day   "
    ]
    for text in test_cases:
        print(f"s = '{text}' -> length of last word: {lengthOfLastWord(text)}")
