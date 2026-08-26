"""
Problem 19: Valid Parentheses
-----------------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    """
    Stack-Based Approach:
    ---------------------
    A Last-In-First-Out (LIFO) stack is well suited for verifying matching parentheses.
    - When encountering an opening bracket, push it onto the stack.
    - When encountering a closing bracket:
        - If the stack is empty, return False (unmatched closing bracket).
        - If the top of the stack matches the closing bracket's type, pop it.
        - Otherwise, return False (mismatched bracket type).
    - After processing the whole string, return True if the stack is empty, False otherwise.
    
    Time Complexity: O(n) - Single pass through the string.
    Space Complexity: O(n) - Stack can hold up to n characters in worst case (e.g. "(((((").
    """
    matching = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in matching:
            # Closing bracket encountered
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            # Opening bracket encountered
            stack.append(char)
            
    return len(stack) == 0


if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "(("]
    for s in test_cases:
        print(f"s = '{s:<8}' -> isValid: {isValid(s)}")
