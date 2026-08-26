"""
Problem 24: Count Total Words in a Book
---------------------------------------
Harsh was recently gifted a book consisting of N pages. Each page contains
exactly M words printed on it.
Help Harsh find the total number of words in the book.

Input Format:
- The first line of input contains a single integer T — the number of test cases.
- Each test case consists of two space-separated integers: N (pages) and M (words per page).

Output Format:
- For each test case, output on a new line, the total number of words in the book.

Constraints:
- 1 <= T <= 100
- 1 <= N <= 100
- 1 <= M <= 100

Example:
Input:
4
1 1
4 2
2 4
95 42

Output:
1
8
8
3990
"""

import sys

def total_words(n: int, m: int) -> int:
    """
    Calculate total words by multiplying pages by words per page.
    
    Time Complexity: O(1) per testcase.
    Space Complexity: O(1).
    """
    return n * m


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        results.append(str(total_words(n, m)))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [(1, 1), (4, 2), (2, 4), (95, 42)]
    for n, m in test_cases:
        print(f"Pages: {n}, Words/page: {m} -> Total words: {total_words(n, m)}")
