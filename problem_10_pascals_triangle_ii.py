"""
Problem 10: Pascal's Triangle II
---------------------------------
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
- 0 <= rowIndex <= 33
"""

from typing import List

def getRow(rowIndex: int) -> List[int]:
    """
    In-Place Single Array / Combinatorial Approach:
    ------------------------------------------------
    Method 1 (In-Place Array Updates):
    We maintain a single array `row` of size `rowIndex + 1`, initialized to [1] + [0]*rowIndex.
    For each step i from 1 to rowIndex, we update values backward from i down to 1:
    `row[j] = row[j] + row[j-1]`.
    
    Method 2 (Combinatorics):
    Element at index k in row n is C(n, k) = n! / (k! * (n-k)!).
    We can compute C(n, k) iteratively: C(n, k) = C(n, k-1) * (n - k + 1) / k.
    
    Both achieve O(rowIndex) space. Below is the combinatorial O(n) time & O(1) extra space method.

    Time Complexity: O(rowIndex)
    Space Complexity: O(1) extra space (excluding the returned row).
    """
    row = [1] * (rowIndex + 1)
    for k in range(1, rowIndex + 1):
        row[k] = row[k - 1] * (rowIndex - k + 1) // k
    return row


if __name__ == "__main__":
    for idx in range(6):
        print(f"rowIndex = {idx} -> {getRow(idx)}")
