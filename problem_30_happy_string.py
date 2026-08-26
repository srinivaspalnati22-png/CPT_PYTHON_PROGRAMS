"""
Problem 30: Happy String (Chef and Happy String / John is Happy)
---------------------------------------------------------------
John has a string S. John is happy if the string contains a contiguous substring
of length strictly greater than 2 (i.e. at least 3 consecutive characters) in which
all characters are vowels ('a', 'e', 'i', 'o', 'u').

Determine whether John is happy or not.

Input Format:
- First line contains T — the number of test cases.
- Each testcase contains a single line of input, a string S.

Output Format:
- For each testcase, print "HAPPY" if John is happy, else print "SAD".

Constraints:
- 1 <= T <= 1000
- 3 <= |S| <= 1000
- S contains only lowercase English letters.

Example:
Input:
4
aeiou
abxy
aebcdefghij
abcdeeafg

Output:
HAPPY
SAD
SAD
HAPPY
"""

import sys

def is_happy_string(s: str) -> str:
    """
    Consecutive Vowels Counter:
    ---------------------------
    We traverse the string while keeping a count of consecutive vowels.
    - If the current character is in {'a', 'e', 'i', 'o', 'u'}:
        - Increment consecutive vowel count.
        - If count > 2 (i.e., at least 3), return "HAPPY".
    - Else (consonant):
        - Reset consecutive vowel count to 0.
    - If loop ends without count > 2, return "SAD".
    
    Time Complexity: O(N) - Single pass through the string of length N.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    vowels = set('aeiou')
    consecutive_vowels = 0
    
    for char in s.lower():
        if char in vowels:
            consecutive_vowels += 1
            if consecutive_vowels > 2:
                return "HAPPY"
        else:
            consecutive_vowels = 0
            
    return "SAD"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        results.append(is_happy_string(s))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = ["aeiou", "abxy", "aebcdefghij", "abcdeeafg", "baeioup"]
    for s in test_cases:
        print(f"s = '{s:<12}' -> {is_happy_string(s)}")
