"""
Problem 17: Third Maximum Number
--------------------------------
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: Distinct maxes: 1st is 3, 2nd is 2, 3rd is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: 3rd distinct max does not exist, so max (2) is returned.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: Distinct maxes: 1st is 3, 2nd is 2 (duplicates merged), 3rd is 1.

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List, Optional

def thirdMax(nums: List[int]) -> int:
    """
    Single-Pass Three Variables Approach:
    -------------------------------------
    Keep track of the 3 largest distinct numbers seen so far (first, second, third),
    initialized to None.
    
    For each number in `nums`:
    - Skip if it equals `first`, `second`, or `third` (ignore duplicates).
    - If num > first: third = second, second = first, first = num
    - Else if num > second: third = second, second = num
    - Else if num > third: third = num
    
    At the end, if `third` is not None, return `third`.
    Otherwise, return `first`.
    
    Time Complexity: O(n) - Single pass through the array.
    Space Complexity: O(1) - Three variables only.
    """
    first: Optional[int] = None
    second: Optional[int] = None
    third: Optional[int] = None
    
    for num in nums:
        # Ignore already seen distinct top values
        if num in (first, second, third):
            continue
            
        if first is None or num > first:
            third = second
            second = first
            first = num
        elif second is None or num > second:
            third = second
            second = num
        elif third is None or num > third:
            third = num
            
    return third if third is not None else first  # type: ignore


if __name__ == "__main__":
    test_cases = [
        [3, 2, 1],
        [1, 2],
        [2, 2, 3, 1],
        [1, 2, -2147483648]
    ]
    for nums in test_cases:
        print(f"nums = {nums} -> Third Max: {thirdMax(nums)}")
