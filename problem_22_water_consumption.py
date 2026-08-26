"""
Problem 22: Water Consumption
-----------------------------
Recently, Ravi visited his doctor. The doctor advised him to drink at least 2000 ml of water each day.
Ravi drank X ml of water today. Determine if Ravi followed the doctor's advice or not.

Input Format:
- The first line contains a single integer T — the number of test cases.
- The first and only line of each test case contains one integer X — amount of water drank today.

Output Format:
- For each test case, output "YES" if Ravi drank at least 2000 ml of water. Otherwise, output "NO".

Constraints:
- 1 <= T <= 2000
- 1 <= X <= 4000

Example:
Input:
3
2999
1450
2000

Output:
YES
NO
YES
"""

import sys

def check_water_consumption(x: int) -> str:
    """
    Check if water intake meets minimum recommendation (2000 ml).
    
    Time Complexity: O(1) per test case.
    Space Complexity: O(1).
    """
    return "YES" if x >= 2000 else "NO"


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        x = int(input_data[i])
        results.append(check_water_consumption(x))
        
    print("\n".join(results))


if __name__ == "__main__":
    test_cases = [2999, 1450, 2000, 1999, 4000]
    for x in test_cases:
        print(f"Drank {x} ml -> {check_water_consumption(x)}")
