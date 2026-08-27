"""
Problem 36: Merge the Tools!
----------------------------
Consider the following:
A string, s, of length n where s = c_0 c_1 ... c_{n-1}. An integer, k, where k is a factor of n.
We can split s into n/k substrings where each substring, t_i, consists of a contiguous block
of characters in s. Then, use each t_i to create string u_i such that:
- The characters in u_i are a subsequence of the characters in t_i.
- Any repeat occurrence of a character is removed from the string such that each character in u_i
  occurs exactly once (maintaining order of first appearance).

Function Description:
Complete the merge_the_tools function.
merge_the_tools has the following parameters:
- string s: the string to analyze
- int k: the size of substrings to analyze

Prints:
- Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format:
- The first line contains a single string, s.
- The second line contains an integer, k, the length of each substring.

Constraints:
- 1 <= n <= 10^4, where n is the length of s
- 1 <= k <= n
- It is guaranteed that n is a multiple of k.

Sample Input:
AABCAAADA
3

Sample Output:
AB
CA
AD
"""

import sys

def merge_the_tools(string: str, k: int) -> list[str]:
    """
    Subsequence Deduplication via First Occurrence Preservation:
    ------------------------------------------------------------
    1. Slice the string into chunks of length k: string[i:i+k] for i in range(0, len(string), k).
    2. For each chunk, preserve distinct characters in their first encountered order.
       In modern Python (>=3.7), `dict.fromkeys(chunk)` preserves insertion order while removing duplicates.
       Alternatively, use a `seen` set while iterating through the chunk.
    
    Time Complexity: O(N) where N is len(string), as each character is processed once.
    Space Complexity: O(k) auxiliary memory per chunk (O(N) for storing results).
    """
    results = []
    for i in range(0, len(string), k):
        chunk = string[i:i + k]
        # dict.fromkeys maintains insertion order and eliminates duplicates in O(k)
        unique_chars = "".join(dict.fromkeys(chunk))
        results.append(unique_chars)
    return results


def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 2:
        string = lines[0]
        k = int(lines[1])
        for line in merge_the_tools(string, k):
            print(line)


if __name__ == "__main__":
    sample_s = "AABCAAADA"
    sample_k = 3
    print(f"Input: string='{sample_s}', k={sample_k}")
    print("Output:")
    for res in merge_the_tools(sample_s, sample_k):
        print(res)
