"""
Problem 40: Cartesian Product (itertools.product)
------------------------------------------------
You are given two lists A and B. Your task is to compute their cartesian product A x B.

Example:
A = [1, 2]
B = [3, 4]
A x B = [(1, 3), (1, 4), (2, 3), (2, 4)]

Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format:
- The first line contains space-separated elements of list A.
- The second line contains space-separated elements of list B.
- Both lists have no duplicate integer elements.

Constraints:
- 0 < len(A) < 30
- 0 < len(B) < 30

Output Format:
- Output the space-separated tuples of the cartesian product.

Sample Input:
1 2
3 4

Sample Output:
(1, 3) (1, 4) (2, 3) (2, 4)
"""

import sys
from itertools import product

def compute_cartesian_product(a: list[int], b: list[int]) -> list[tuple[int, int]]:
    """
    Cartesian Product:
    ------------------
    Generates all ordered pairs (x, y) where x in A and y in B.
    Using `itertools.product(a, b)` generates tuples in lexicographical order.

    Equivalent list comprehension:
        [(x, y) for x in a for y in b]

    Time Complexity: O(|A| * |B|) - Direct combination generation.
    Space Complexity: O(|A| * |B|) - Output storage.
    """
    return list(product(a, b))


def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        a = list(map(int, lines[0].split()))
        b = list(map(int, lines[1].split()))
        prod = compute_cartesian_product(a, b)
        print(" ".join(str(p) for p in prod))


if __name__ == "__main__":
    list_a = [1, 2]
    list_b = [3, 4]
    result = compute_cartesian_product(list_a, list_b)
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print("Cartesian Product:")
    print(" ".join(str(p) for p in result))
