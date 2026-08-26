"""
Problem 15: Power of Two
------------------------
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true (2^0 = 1)

Example 2:
Input: n = 16
Output: true (2^4 = 16)

Example 3:
Input: n = 3
Output: false

Constraints:
- -2^31 <= n <= 2^31 - 1
"""

def isPowerOfTwo(n: int) -> bool:
    """
    Bitwise Trick Approach:
    -----------------------
    A positive integer n is a power of 2 if and only if:
    1. n > 0
    2. Its binary representation has exactly one set bit ('1').
    
    Subtracting 1 from a power of 2 turns that single '1' bit into '0' and all trailing '0's into '1's.
    For example:
        16  = 10000 (binary)
        15  = 01111 (binary)
        16 & 15 = 00000 (0)
        
    Therefore, `n & (n - 1) == 0` strictly holds for all powers of two.
    
    Time Complexity: O(1) - Single bitwise operation.
    Space Complexity: O(1) - Constant space.
    """
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    test_cases = [1, 16, 3, 0, -16, 64, 218]
    for num in test_cases:
        print(f"n = {num:<5} -> isPowerOfTwo: {isPowerOfTwo(num)}")
