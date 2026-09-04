"""
Problem 44: The Captain's Room (Set Arithmetic & Frequency Analysis)
--------------------------------------------------------------------
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel:
- A Captain (given a separate room).
- An unknown group of families consisting of K members per group (K != 1), where each family
  shares one room.

The list of room numbers shows each family room number appearing exactly K times, while the
Captain's room number appears only once.
Find the Captain's room number.

Input Format:
- The first line consists of an integer, K, the size of each group.
- The second line contains the unordered elements of the room number list.

Constraints:
- 1 < K < 1000

Output Format:
- Output the Captain's room number.

Sample Input:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output:
8
"""

import sys
from collections import Counter


def find_captains_room_math(k: int, rooms: list[int]) -> int:
    """
    Finds the Captain's room number using mathematical set manipulation.

    Mathematical Derivation:
    ------------------------
    Let U be the set of unique rooms, and C be the Captain's room.
    Total rooms sum:
        sum(rooms) = K * sum(family_rooms) + C
    Unique rooms sum:
        sum(set(rooms)) = sum(family_rooms) + C
    Multiplying unique sum by K:
        K * sum(set(rooms)) = K * sum(family_rooms) + K * C
    Subtracting total rooms sum from K * unique sum:
        K * sum(set(rooms)) - sum(rooms) = (K - 1) * C
    Therefore:
        C = (K * sum(set(rooms)) - sum(rooms)) // (K - 1)

    Time Complexity: O(N) where N is total room entries.
    Space Complexity: O(U) where U is the number of distinct rooms.
    """
    unique_rooms = set(rooms)
    return (k * sum(unique_rooms) - sum(rooms)) // (k - 1)


def find_captains_room_counter(k: int, rooms: list[int]) -> int:
    """
    Alternative approach using collections.Counter.
    Finds the room with count == 1.

    Time Complexity: O(N)
    Space Complexity: O(U)
    """
    counts = Counter(rooms)
    for room, count in counts.items():
        if count != k:
            return room
    return -1


def main():
    lines = sys.stdin.read().splitlines()
    if len(lines) >= 2:
        k = int(lines[0].strip())
        rooms = list(map(int, lines[1].split()))
        print(find_captains_room_math(k, rooms))


if __name__ == "__main__":
    k = 5
    rooms = [
        1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2
    ]
    ans_math = find_captains_room_math(k, rooms)
    ans_counter = find_captains_room_counter(k, rooms)
    print(f"K: {k}")
    print(f"Math Method Result: {ans_math}")
    print(f"Counter Method Result: {ans_counter}")
    assert ans_math == 8, f"Expected 8, got {ans_math}"
    assert ans_counter == 8, f"Expected 8, got {ans_counter}"
    print("All Captain's Room tests passed successfully!")
