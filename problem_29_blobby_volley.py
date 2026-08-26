"""
Problem 29: Blobby Volley Scores
--------------------------------
Alice and Bob are playing a game of Blobby Volley.
- Initially, Alice is the server and Bob is the receiver.
- If the server wins the point: their score increases by 1, and they remain the server.
- If the receiver wins the point: their score does NOT increase, but they become the server.

Given a string S of length N ('A' for Alice winning the point, 'B' for Bob winning),
determine the final scores of Alice and Bob.

Input Format:
- First line contains T — the number of test cases.
- Each test case consists of two lines:
    1. Integer N (number of turns).
    2. String S of length N.

Output Format:
- For each test case, output two space-separated integers: Alice's score and Bob's score.

Constraints:
- 1 <= T <= 1000
- 1 <= N <= 1000
- S consists only of 'A' and 'B'.

Example:
Input:
4
3
AAA
4
BBBB
5
ABABB
5
BABAB

Output:
3 0
0 3
1 1
0 0
"""

import sys
from typing import Tuple

def calculate_scores(n: int, s: str) -> Tuple[int, int]:
    """
    Simulation Approach:
    --------------------
    Track the current server ('A' initially) and both scores.
    For each winner in string S:
    - If winner == server:
        - Increment winner's score.
    - If winner != server:
        - Winner becomes the new server (no point awarded).
        
    Time Complexity: O(N) per testcase.
    Space Complexity: O(1).
    """
    alice_score = 0
    bob_score = 0
    server = 'A'
    
    for winner in s:
        if winner == server:
            if server == 'A':
                alice_score += 1
            else:
                bob_score += 1
        else:
            server = winner
            
    return alice_score, bob_score


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        a_score, b_score = calculate_scores(n, s)
        results.append(f"{a_score} {b_score}")
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = ["AAA", "BBBB", "ABABB", "BABAB"]
    for s in test_cases:
        a_score, b_score = calculate_scores(len(s), s)
        print(f"S = '{s:<6}' -> Alice: {a_score}, Bob: {b_score}")
