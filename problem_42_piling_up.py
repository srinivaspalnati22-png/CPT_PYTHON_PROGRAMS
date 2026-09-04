"""
Problem 42: Piling Up! (Stacking Cubes)
---------------------------------------
There is a horizontal row of n cubes. The length of each cube is given.
You need to create a new vertical pile of cubes.
The new pile should follow these directions:
if cube[i] is on top of cube[j] then sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost
cube each time. Print 'Yes' if it is possible to stack the cubes. Otherwise, print 'No'.

Input Format:
- The first line contains a single integer T, the number of test cases.
- For each test case, there are 2 lines:
  - First line: n, the number of cubes.
  - Second line: n space-separated integers denoting side lengths of each cube.

Constraints:
- 1 <= T <= 5
- 1 <= n <= 10^5
- 1 <= sideLength < 2^31

Output Format:
- For each test case, output a single line containing either 'Yes' or 'No'.

Sample Input:
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output:
Yes
No
"""

import sys


def can_pile_cubes(cubes: list[int]) -> str:
    """
    Determines if cubes can be stacked vertically using a greedy two-pointer strategy.

    Approach:
    ---------
    At each step, we must pick the larger of the two available ends (leftmost or rightmost),
    because picking a smaller cube when a larger one is available might make it impossible
    to place the larger one later (since the stack must be non-increasing in size).
    If the chosen maximum end is strictly greater than the top of the stack (previously chosen cube),
    then it is impossible to stack the cubes -> return 'No'.
    If we can successfully pick all cubes without violation, return 'Yes'.

    Time Complexity:
    ----------------
    - O(n) per test case, where n is the number of cubes. Each element is inspected once.

    Space Complexity:
    -----------------
    - O(1) auxiliary space beyond the input list.
    """
    left = 0
    right = len(cubes) - 1
    previous = float("inf")

    while left <= right:
        if cubes[left] >= cubes[right]:
            chosen = cubes[left]
            left += 1
        else:
            chosen = cubes[right]
            right -= 1

        if chosen > previous:
            return "No"

        previous = chosen

    return "Yes"


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    line_idx = 1
    for _ in range(t):
        if line_idx < len(lines):
            _n = int(lines[line_idx].strip())
            line_idx += 1
            cubes = list(map(int, lines[line_idx].split()))
            line_idx += 1
            print(can_pile_cubes(cubes))


if __name__ == "__main__":
    test_cases = [
        ([4, 3, 2, 1, 3, 4], "Yes"),
        ([1, 3, 2], "No"),
        ([1, 2, 3, 8, 7], "No"),
        ([1, 2, 3, 7, 8], "Yes"),
    ]
    for cubes, expected in test_cases:
        res = can_pile_cubes(cubes)
        print(f"Cubes: {cubes} -> Result: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {cubes}: got {res}, expected {expected}"
    print("All test cases passed successfully!")
