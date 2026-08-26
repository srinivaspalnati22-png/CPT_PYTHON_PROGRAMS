"""
Problem 14: Longest Common Prefix
----------------------------------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Vertical Scanning Approach:
    ---------------------------
    We inspect characters column-by-column:
    - Take the first string `strs[0]` as reference.
    - For each index `i` and character `c` in `strs[0]`:
        - Check every other string in the list at index `i`.
        - If index `i` is out of bounds for string `s`, or `s[i] != c`,
          then the longest common prefix ends before `i`.
    - If all strings match at all positions up to the end of `strs[0]`,
      `strs[0]` itself is the common prefix.
      
    Time Complexity: O(S) - where S is the sum of all characters in all strings.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    if not strs:
        return ""
    
    first = strs[0]
    for i in range(len(first)):
        char = first[i]
        for s in strs[1:]:
            if i == len(s) or s[i] != char:
                return first[:i]
                
    return first


if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "throne"]
    ]
    for test in test_cases:
        print(f"strs = {test} -> Longest Common Prefix: '{longestCommonPrefix(test)}'")
