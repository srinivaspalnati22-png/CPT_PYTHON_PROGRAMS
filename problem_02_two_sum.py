"""
Problem 2: Two Sum
------------------
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Hash Map (One-Pass) Approach:
    ------------------------------
    As we iterate through the list, for each element `num`, we compute its complement:
    `complement = target - num`.
    
    If `complement` exists in our hash map, we have found our pair and return their indices.
    Otherwise, we store `num` with its current index in the hash map.
    
    Time Complexity: O(n) - Single pass through the list. Hash map lookups and insertions are O(1) on average.
    Space Complexity: O(n) - To store up to n elements in the dictionary.
    """
    seen = {}  # maps number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, -2, -3, -4, -5], -8)
    ]
    for nums, target in test_cases:
        result = twoSum(nums, target)
        print(f"nums = {nums}, target = {target} -> indices: {result}")
