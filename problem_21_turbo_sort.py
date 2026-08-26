"""
Problem 21: Turbo Sort
----------------------
Given a list of numbers, you have to sort them in non-decreasing order.

Input Format:
- The first line contains a single integer N, denoting the number of integers in the list.
- The next N lines contain a single integer each, denoting the elements of the list.

Output Format:
- Output N lines, containing one integer each, in non-decreasing order.

Constraints:
- 1 <= N <= 10^6
- 0 <= elements of the list <= 10^6

Example:
Input:
5
5
3
6
7
1

Output:
1
3
5
6
7
"""

import sys
from typing import List

def turbo_sort(arr: List[int]) -> List[int]:
    """
    Sorting Approach:
    -----------------
    Since Python's built-in Timsort (`sort()` or `sorted()`) is implemented in highly
    optimized C, it executes in O(N log N) time and is extremely fast.
    
    For competitive programming with N up to 10^6 and range <= 10^6, Counting Sort
    can also be used for O(N + MaxVal) linear time.
    
    Time Complexity: O(N log N) using Timsort, or O(N + M) using Counting Sort.
    Space Complexity: O(N) auxiliary space.
    """
    return sorted(arr)


def solve_counting_sort(arr: List[int], max_val: int = 1000000) -> List[int]:
    """Counting sort implementation for large N with bounded values."""
    counts = [0] * (max_val + 1)
    for x in arr:
        counts[x] += 1
    
    sorted_arr = []
    for val, count in enumerate(counts):
        if count:
            sorted_arr.extend([val] * count)
    return sorted_arr


def main():
    # Competitive programming fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = [int(x) for x in input_data[1:n+1]]
    
    sorted_nums = turbo_sort(numbers)
    
    sys.stdout.write("\n".join(map(str, sorted_nums)) + "\n")


if __name__ == "__main__":
    # Demonstration test
    sample_input = [5, 3, 6, 7, 1]
    print("Original:", sample_input)
    print("Sorted:  ", turbo_sort(sample_input))
