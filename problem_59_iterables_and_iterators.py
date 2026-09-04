"""
Problem 59: Iterables and Iterators (Probability of Letter Selection)
---------------------------------------------------------------------
You are given a list of N lowercase English letters. For a given integer K,
you can select any K indices (assume 1-based indexing) with uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format:
- Line 1: N, denoting the length of the list.
- Line 2: N space-separated lowercase English letters.
- Line 3: K, denoting the number of indices to be selected.

Constraints:
- 1 <= N <= 10
- 1 <= K <= N
- All letters are lowercase English letters.

Output Format:
- Output a single line consisting of the probability that at least one of the K indices
  selected contains the letter 'a' (formatted to 4 decimal places).

Sample Input:
4
a a c d
2

Sample Output:
0.8333
"""

import math
import sys
from itertools import combinations


def calculate_letter_probability(letters: list[str], k: int, target: str = "a") -> float:
    """
    Calculates probability that at least one chosen index contains `target`.

    Two Approaches:
    ---------------
    Method 1: Combinatorics (Complement rule)
        Total combinations: C(N, K)
        Combinations without 'a': C(N - count('a'), K)
        P(at least one 'a') = 1 - C(N - count('a'), K) / C(N, K)

    Method 2: Itertools combinations simulation
        Generate all index combinations: list(combinations(range(N), K))
        Count those that have at least one index where letters[idx] == target.

    Time Complexity:
    ----------------
    - Combinatorics: O(1) arithmetic operations.
    - Itertools: O(C(N, K)) <= O(C(10, 5)) = 252 operations.

    Space Complexity:
    -----------------
    - O(1) auxiliary space.
    """
    n = len(letters)
    non_target_count = sum(1 for ch in letters if ch != target)

    if non_target_count < k:
        return 1.0

    total_combinations = math.comb(n, k)
    unfavorable_combinations = math.comb(non_target_count, k)

    probability = 1.0 - (unfavorable_combinations / total_combinations)
    return probability


def calculate_via_itertools(letters: list[str], k: int, target: str = "a") -> float:
    """Computes probability directly by enumerating all index tuples."""
    n = len(letters)
    all_combos = list(combinations(range(n), k))
    favorable = sum(1 for combo in all_combos if any(letters[idx] == target for idx in combo))
    return favorable / len(all_combos)


def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 3:
        _n = int(lines[0].strip())
        letters = lines[1].split()
        k = int(lines[2].strip())
        prob = calculate_letter_probability(letters, k)
        print(f"{prob:.4f}")


if __name__ == "__main__":
    sample_letters = ["a", "a", "c", "d"]
    k = 2
    prob_math = calculate_letter_probability(sample_letters, k)
    prob_iter = calculate_via_itertools(sample_letters, k)
    print(f"Letters: {sample_letters}, K: {k}")
    print(f"Math Method:      {prob_math:.4f}")
    print(f"Itertools Method: {prob_iter:.4f}")
    assert round(prob_math, 4) == 0.8333
    assert round(prob_iter, 4) == 0.8333
    print("Probability calculation tests passed successfully!")
