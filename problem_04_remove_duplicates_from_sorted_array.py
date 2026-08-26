"""
Problem 4: Remove Duplicates from Sorted Array
-----------------------------------------------
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the
elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k:
- Change the array nums such that the first k elements contain the unique elements
  in the order they were present in nums initially.
- The remaining elements beyond k do not matter.
- Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Two-Pointer In-Place Approach:
    ------------------------------
    Since the array is sorted, duplicates are adjacent to each other.
    We maintain a write pointer `k` (or slow pointer) pointing to the position of the
    last confirmed unique element.
    We iterate through the array using a read pointer `i` (fast pointer). Whenever `nums[i]`
    is different from `nums[k]`, we increment `k` and write `nums[i]` at `nums[k]`.
    
    Time Complexity: O(n) - Single traversal of the array.
    Space Complexity: O(1) - Modification is in-place with no extra memory.
    """
    if not nums:
        return 0
    
    k = 0  # index of last unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
            
    return k + 1


if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        [1, 2, 3, 4, 5]
    ]
    for orig in test_cases:
        nums = list(orig)
        k = removeDuplicates(nums)
        print(f"Original: {orig} -> k = {k}, modified array: {nums[:k]}")
