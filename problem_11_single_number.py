"""
Problem 11: Single Number
-------------------------
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    """
    Bitwise XOR Approach:
    ---------------------
    Bitwise XOR has three key properties:
    1. a ^ 0 = a
    2. a ^ a = 0
    3. a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b (Commutative & Associative)
    
    If we XOR all the numbers in the array together:
    - Every number appearing twice cancels out to 0 (x ^ x = 0).
    - The unique single number XORed with 0 remains as the answer.
    
    Time Complexity: O(n) - Single pass through nums.
    Space Complexity: O(1) - Constant auxiliary space.
    """
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [-1, -1, -2]
    ]
    for nums in test_cases:
        print(f"nums = {nums} -> Single Number: {singleNumber(nums)}")
