"""
Problem 18: Add Strings
-----------------------
Given two non-negative integers, num1 and num2 represented as string, return the sum
of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers
(such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
- 1 <= num1.length, num2.length <= 10^4
- num1 and num2 consist of only digits.
- num1 and num2 don't have any leading zeros except for the zero itself.
"""

def addStrings(num1: str, num2: str) -> str:
    """
    Column-by-Column Elementary School Addition:
    --------------------------------------------
    Start from the rightmost digits (least significant) of both strings using two pointers
    `i` and `j` and maintain a `carry` variable (initially 0).
    
    In each iteration (while `i >= 0`, `j >= 0`, or `carry > 0`):
    - Extract the digit value from num1 (or 0 if exhausted) using `ord(c) - ord('0')`.
    - Extract the digit value from num2 (or 0 if exhausted).
    - Compute total = d1 + d2 + carry.
    - Append `total % 10` to the result list.
    - Update `carry = total // 10`.
    - Move pointers leftward.
    
    Finally, reverse the result list and join into a string.
    
    Time Complexity: O(max(len(num1), len(num2)))
    Space Complexity: O(max(len(num1), len(num2))) - for the output string.
    """
    result = []
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry:
        d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        d2 = ord(num2[j]) - ord('0') if j >= 0 else 0
        
        total = d1 + d2 + carry
        carry = total // 10
        result.append(str(total % 10))
        
        i -= 1
        j -= 1
        
    return "".join(reversed(result))


if __name__ == "__main__":
    test_cases = [
        ("11", "123"),
        ("456", "77"),
        ("0", "0"),
        ("99999999999999999999", "1")
    ]
    for n1, n2 in test_cases:
        print(f"num1 = '{n1}', num2 = '{n2}' -> Sum: '{addStrings(n1, n2)}'")
