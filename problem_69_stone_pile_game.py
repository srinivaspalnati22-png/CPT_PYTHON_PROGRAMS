"""
Problem 69: Stone Pile Game (Zack and Ryan)
-------------------------------------------
There are N piles where the i-th pile consists of Ai stones.
Zack and Ryan play a game taking alternate turns, with Zack starting first.

In their turn, a player chooses any non-empty pile and removes exactly 1 stone from it.
The game ends when EXACTLY 1 pile becomes empty.
The player who made the last move wins.

Determine the winner if both players play optimally.

Input Format:
- The first line contains an integer T, denoting the number of test cases.
- Each test case consists of 2 lines:
  - First line: integer N (number of piles).
  - Second line: N space-separated integers A1, A2, ..., AN.

Output Format:
- For each test case, output 'Zack' if Zack wins, otherwise 'Ryan'.

Constraints:
- 1 <= T <= 1000
- 1 <= N <= 10^5
- 1 <= Ai <= 10^9
- Sum of N over all test cases <= 2 * 10^5

Sample Input:
3
2
2 2
1
10
3
1 5 6

Sample Output:
Ryan
Ryan
Zack
"""

import sys
from typing import List


def determine_winner(piles: List[int]) -> str:
    """
    Determines the winner of the stone pile game under optimal play.

    Game Theory Analysis:
    ---------------------
    1. Winning Condition:
       - The game immediately ends as soon as any pile is reduced to 0 stones.
       - The player who removes the last stone from a pile with 1 stone wins instantly.

    2. Immediate Win Case:
       - If initially min(A) == 1, Zack can immediately choose this pile, remove its 1 stone,
         making it 0, and win on turn 1!
       - Thus, if min(piles) == 1 -> Zack wins.

    3. Normal Game (min(A) >= 2):
       - If a player reduces any pile to 1 stone, the opposing player can immediately take that 1 stone
         and win on the very next turn.
       - Therefore, neither player will willingly reduce any pile to 1 stone unless forced to do so.
       - Each pile A_i can safely have stones removed until it reaches size 2 without giving away an immediate win.
       - The number of safe moves on pile i is (A_i - 2).
       - Total safe moves across all N piles = sum(A_i - 2) = sum(A_i) - 2 * N.
       - Notice that 2 * N is always an even integer!
       - Thus:
           (sum(A_i) - 2 * N) % 2 == sum(A_i) % 2
       - Once all safe moves are exhausted, every pile has exactly 2 stones.
       - The player whose turn it is is now forced to make a losing move (decrementing a 2 to 1),
         allowing the other player to empty that pile on the next move and win.
       - Consequently, if sum(A_i) is odd, Zack plays the last safe move, forcing Ryan into the losing position.
         Hence, Zack wins.
       - If sum(A_i) is even, Ryan plays the last safe move, forcing Zack into the losing position.
         Hence, Ryan wins.

    Summary:
    --------
    - If min(A) == 1: "Zack"
    - Else if sum(A) % 2 == 1: "Zack"
    - Else: "Ryan"

    Time Complexity:
    ----------------
    - O(N): A single pass to compute the minimum and sum modulo 2.

    Space Complexity:
    -----------------
    - O(1): Auxiliary space.
    """
    min_pile = min(piles)
    if min_pile == 1:
        return "Zack"

    total_sum_mod2 = sum(piles) % 2
    return "Zack" if total_sum_mod2 == 1 else "Ryan"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        piles = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        results.append(determine_winner(piles))
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [
        ([2, 2], "Ryan"),
        ([10], "Ryan"),
        ([1, 5, 6], "Zack"),
        ([2, 3], "Zack"),
        ([3, 3, 3], "Zack"),
        ([2, 2, 2], "Ryan"),
        ([5], "Zack"),
        ([1], "Zack"),
    ]
    for arr, expected in test_cases:
        res = determine_winner(arr)
        print(f"Piles: {arr} -> Winner: {res} (Expected: {expected})")
        assert res == expected, f"Failed for {arr}: got {res}, expected {expected}"
    print("All Stone Pile Game tests passed successfully!")
