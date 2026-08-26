"""
Problem 12: Find the Index of the First Occurrence in a String
--------------------------------------------------------------
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
Input: haystack = "PythonCode", needle = "Pythoc"
Output: -1
Explanation: "Pythoc" did not occur in "PythonCode", so we return -1.

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.
"""

def strStr(haystack: str, needle: str) -> int:
    """
    Sliding Window / Knuth-Morris-Pratt (KMP) or Direct Substring Comparison:
    --------------------------------------------------------------------------
    We iterate i from 0 up to len(haystack) - len(needle).
    At each position, check if the substring haystack[i : i + len(needle)] == needle.
    If match is found, return i.
    If the loop finishes without a match, return -1.
    
    For larger inputs or O(N + M) strictly, KMP prefix function is standard.
    Given N, M <= 10^4, direct window slicing or KMP is suitable.
    
    Time Complexity: O((N - M + 1) * M) worst-case with sliding window; O(N + M) with KMP.
    Space Complexity: O(1) auxiliary space with direct window.
    """
    n, m = len(haystack), len(needle)
    if m > n:
        return -1
    
    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i
            
    return -1


# KMP Algorithm implementation (Linear Time O(N + M))
def strStr_KMP(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    
    # Compute longest prefix suffix (LPS) array for needle
    lps = [0] * len(needle)
    prev_lps, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prev_lps]:
            lps[i] = prev_lps + 1
            prev_lps += 1
            i += 1
        elif prev_lps == 0:
            lps[i] = 0
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]
            
    # Search needle in haystack using LPS
    i = 0  # index in haystack
    j = 0  # index in needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
                
        if j == len(needle):
            return i - len(needle)
            
    return -1


if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad"),
        ("PythonCode", "Pythoc"),
        ("leetcode", "leeto"),
        ("hello", "ll")
    ]
    for h, n in test_cases:
        print(f"haystack = '{h}', needle = '{n}' -> Index: {strStr(h, n)} (KMP: {strStr_KMP(h, n)})")
