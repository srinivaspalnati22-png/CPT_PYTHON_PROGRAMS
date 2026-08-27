"""
Problem 39: Designer Door Mat
------------------------------
Mr. Vincent works in a door mat manufacturing company. One day, he designed a
new door mat with the following specifications:
- Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use '|', '.' and '-' characters.

Input Format:
- A single line containing the space separated values of N and M.

Constraints:
- 5 < N < 101
- 15 < M < 303

Output Format:
- Output the design pattern.

Sample Input:
9 27

Sample Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

import sys

def generate_door_mat(n: int, m: int) -> list[str]:
    """
    Door Mat Pattern Generation:
    ----------------------------
    Pattern consists of 3 sections:
    1. Top half (rows i from 1 to N-1, step 2):
       - Pattern repeated `i` times: '.|.' * i
       - Centered in width M padded with '-': (pattern).center(m, '-')
    2. Center line (row (N+1)//2):
       - 'WELCOME' centered in width M padded with '-': 'WELCOME'.center(m, '-')
    3. Bottom half (rows i from N-2 down to 1, step 2):
       - Mirror image of the top half.

    Time Complexity: O(N * M) - Generating N lines each of length M.
    Space Complexity: O(N * M) - Storing the grid lines.
    """
    pattern = '.|.'
    mat_lines = []
    
    # Top half
    for i in range(1, n, 2):
        mat_lines.append((pattern * i).center(m, '-'))
        
    # Center line
    mat_lines.append("WELCOME".center(m, '-'))
    
    # Bottom half
    for i in range(n - 2, 0, -2):
        mat_lines.append((pattern * i).center(m, '-'))
        
    return mat_lines


def main():
    lines = sys.stdin.read().split()
    if len(lines) >= 2:
        n = int(lines[0])
        m = int(lines[1])
        for row in generate_door_mat(n, m):
            print(row)


if __name__ == "__main__":
    test_n, test_m = 7, 21
    print(f"--- Door Mat ({test_n} x {test_m}) ---")
    for row in generate_door_mat(test_n, test_m):
        print(row)

    print()
    test_n2, test_m2 = 9, 27
    print(f"--- Door Mat ({test_n2} x {test_m2}) ---")
    for row in generate_door_mat(test_n2, test_m2):
        print(row)
