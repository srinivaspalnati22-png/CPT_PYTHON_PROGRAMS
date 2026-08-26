"""
Problem 9: Pascal's Triangle
----------------------------
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle:
- Each row starts and ends with 1.
- Each interior number is the sum of the two numbers directly above it in the previous row.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
- 1 <= numRows <= 30
"""

from typing import List

def generate(numRows: int) -> List[List[int]]:
    """
    Dynamic Row Generation:
    -----------------------
    We construct the triangle row by row:
    - Row 0 is [1]
    - For row i from 1 to numRows - 1:
        - Row starts with 1
        - Each middle element j (1 <= j < i) is prev_row[j-1] + prev_row[j]
        - Row ends with 1
        
    Time Complexity: O(numRows^2) - Generating 1 + 2 + ... + numRows elements = numRows*(numRows+1)/2 elements.
    Space Complexity: O(1) extra space (excluding the output triangle itself).
    """
    triangle = []
    
    for row_num in range(numRows):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
        
    return triangle


if __name__ == "__main__":
    for n in [1, 5]:
        print(f"numRows = {n}:")
        res = generate(n)
        for r in res:
            print("  ", r)
