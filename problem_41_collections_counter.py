"""
Problem 41: Collections.Counter (Raghu's Shoe Shop)
---------------------------------------------------
Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing
the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if
they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.

Input Format:
- The first line contains X, the number of shoes.
- The second line contains the space separated list of all the shoe sizes in the shop.
- The third line contains N, the number of customers.
- The next N lines contain the space separated values of the shoe size desired by the
  customer and xi, the price of the shoe.

Constraints:
- 0 < X < 10^3
- 0 < N <= 10^3
- 20 < xi < 100
- 2 < shoe size < 20

Output Format:
- Print the amount of money earned by Raghu.

Sample Input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output:
200
"""

import sys
from collections import Counter


def compute_shoe_earnings(shoe_sizes: list[int], orders: list[tuple[int, int]]) -> int:
    """
    Computes total revenue generated from shoe sales using frequency counting.

    Approach:
    ---------
    1. Count available shoe sizes using `collections.Counter`.
    2. For each customer requesting (desired_size, price):
       - If desired_size count > 0, deduct 1 from count and add price to total earnings.
       - Otherwise, customer cannot purchase the shoe.

    Time Complexity:
    ----------------
    - O(X + N) where X is the number of shoes and N is the number of customer requests.
      Counter initialization is O(X), and each customer check/decrement is O(1).

    Space Complexity:
    -----------------
    - O(U) where U is the number of unique shoe sizes stored in Counter (U <= X).
    """
    inventory = Counter(shoe_sizes)
    total_earnings = 0

    for size, price in orders:
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1

    return total_earnings


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x = int(input_data[0])
    idx = 1
    shoe_sizes = [int(input_data[i]) for i in range(idx, idx + x)]
    idx += x
    n = int(input_data[idx])
    idx += 1
    orders = []
    for _ in range(n):
        size = int(input_data[idx])
        price = int(input_data[idx + 1])
        orders.append((size, price))
        idx += 2

    earnings = compute_shoe_earnings(shoe_sizes, orders)
    print(earnings)


if __name__ == "__main__":
    sample_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    sample_orders = [
        (6, 55),
        (6, 45),
        (6, 55),
        (4, 40),
        (18, 60),
        (10, 50),
    ]
    earnings = compute_shoe_earnings(sample_sizes, sample_orders)
    print(f"Sample Inventory: {sample_sizes}")
    print(f"Sample Orders: {sample_orders}")
    print(f"Total Earnings: {earnings}")
    assert earnings == 200, f"Expected 200, got {earnings}"
    print("Test passed successfully!")
