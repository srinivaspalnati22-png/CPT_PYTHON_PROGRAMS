"""
Problem 13: Search Insert Position
-----------------------------------
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    """
    Binary Search Approach:
    -----------------------
    Because `nums` is sorted in ascending order and we require O(log n) time,
    we use binary search:
    - Maintain search boundaries `left = 0` and `right = len(nums) - 1`.
    - Compute `mid = (left + right) // 2`.
    - If `nums[mid] == target`, target is found at index `mid`.
    - If `nums[mid] < target`, search the right half: `left = mid + 1`.
    - If `nums[mid] > target`, search the left half: `right = mid - 1`.
    - When `left > right`, `left` represents the exact insertion position.
    
    Time Complexity: O(log n) - Halves the search space each step.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0)
    ]
    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target} -> Insert Index: {searchInsert(nums, target)}")
