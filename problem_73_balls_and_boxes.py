"""
Problem 73: Balls and Boxes (Minimum Boxes for Distinct Colors)
---------------------------------------------------------------
There are N different types of colours numbered from 1 to N.
Chef has Ai balls having colour i (1 <= i <= N).

Chef arranges boxes and puts each ball in exactly one of those boxes.
Find the minimum number of boxes Chef needs so that NO box contains two balls
of the same colour.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of 2 lines:
  - First line contains an integer N, denoting the number of colors.
  - Second line contains N space-separated integers A1, A2, ..., AN.

Output Format:
- For each test case, output the minimum number of boxes required.

Constraints:
- 1 <= T <= 1000
- 2 <= N <= 100
- 1 <= Ai <= 10^5

Sample Input:
3
2
8 5
3
5 10 15
4
4 4 4 4

Sample Output:
8
15
4
"""

import sys
from typing import List


def min_boxes_required(balls: List[int]) -> int:
    """
    Computes the minimum number of boxes needed so that no box contains two balls of the same color.

    Algorithmic Insight:
    --------------------
    - By the Pigeonhole Principle, if any color i has A_i balls, each of those A_i balls
      must be placed in a distinct box.
    - Thus, the number of boxes must be at least A_i for all i:
        boxes >= max(A_1, A_2, ..., A_N)
    - Furthermore, max(A) boxes is always sufficient:
      For each color i with A_i balls, we can assign the balls to boxes 1, 2, ..., A_i.
      Since each color assigns at most one ball to any box k, no box ever contains duplicate colors.
    - Therefore, the minimum number of boxes is simply max(A).

    Time Complexity:
    ----------------
    - O(N): Linear scan to find the maximum element.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    return max(balls)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        balls = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(str(min_boxes_required(balls)))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([8, 5], 8),
        ([5, 10, 15], 15),
        ([4, 4, 4, 4], 4),
        ([1, 2, 3], 3),
        ([100], 100),
    ]
    for arr, expected in test_cases:
        res = min_boxes_required(arr)
        print(f"Balls: {arr} -> Boxes: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Balls and Boxes tests passed successfully!")
