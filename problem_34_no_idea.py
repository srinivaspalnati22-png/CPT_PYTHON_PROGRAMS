"""
Problem 34: No Idea! (Happiness Calculation)
--------------------------------------------
There is an array of n integers. There are also 2 disjoint sets, A and B, each
containing m integers. You like all integers in set A (+1 happiness) and dislike
all integers in set B (-1 happiness). Your initial happiness is 0.

For each integer in the array:
- If it belongs to A, add +1 to happiness.
- If it belongs to B, add -1 to happiness.
- Otherwise, happiness does not change.

Output your final happiness at the end.

Input Format:
- The first line contains integers n and m separated by a space.
- The second line contains n integers, the elements of the array.
- The third and fourth lines contain m integers, set A and set B, respectively.

Constraints:
- 1 <= n <= 10^5
- 1 <= m <= 10^5
- 1 <= Any integer in input <= 10^9

Output Format:
- Output a single integer, your total happiness.

Sample Input:
3 2
1 5 3
3 1
5 7

Sample Output:
1
"""

import sys

def compute_happiness(arr: list[int], set_a: set[int], set_b: set[int]) -> int:
    """
    Hash Set Membership Lookup:
    ----------------------------
    Set lookup in Python runs in average O(1) time.
    By converting A and B into hash sets (hash tables), we can check each element
    in the array in O(1) time.

    Happiness calculation:
        sum((x in set_a) - (x in set_b) for x in arr)

    Time Complexity: O(n + m) - O(m) to build sets, O(n) to iterate through array.
    Space Complexity: O(m) - Space for sets A and B.
    """
    happiness = 0
    for x in arr:
        if x in set_a:
            happiness += 1
        elif x in set_b:
            happiness -= 1
    return happiness


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    offset = 2
    arr = list(map(int, input_data[offset:offset + n]))
    offset += n
    
    set_a = set(map(int, input_data[offset:offset + m]))
    offset += m
    
    set_b = set(map(int, input_data[offset:offset + m]))
    
    print(compute_happiness(arr, set_a, set_b))


if __name__ == "__main__":
    test_arr = [1, 5, 3]
    test_a = {3, 1}
    test_b = {5, 7}
    result = compute_happiness(test_arr, test_a, test_b)
    print(f"Array: {test_arr}, Set A: {test_a}, Set B: {test_b}")
    print(f"Total Happiness: {result}")
