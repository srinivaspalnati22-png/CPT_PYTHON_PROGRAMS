"""
Problem 54: Collections.OrderedDict (Supermarket Net Price)
----------------------------------------------------------
You are the manager of a supermarket.
You have a list of items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item (may consist of multiple words).
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:
- The first line contains the number of items, N.
- The next N lines contain the item's name and price, separated by a space.

Constraints:
- 0 < N <= 100

Output Format:
- Print the item_name and net_price in order of its first occurrence.

Sample Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

import sys
from collections import OrderedDict


def compute_supermarket_totals(transactions: list[str]) -> OrderedDict[str, int]:
    """
    Aggregates net price per item while preserving first-seen insertion order.

    Approach:
    ---------
    - Each line ends with the price, while the preceding tokens represent the item name
      (which can be multi-word, such as "BANANA FRIES").
    - Using `line.rsplit(' ', 1)` splits cleanly into `(item_name, price)`.
    - We use an `OrderedDict` to accumulate cumulative expenditure for each item.

    Time Complexity:
    ----------------
    - O(N * L) where N is number of transactions and L is the length of the string.
      Dictionary lookup and update are O(1) on average.

    Space Complexity:
    -----------------
    - O(U * L) where U is the number of unique items.
    """
    totals: OrderedDict[str, int] = OrderedDict()
    for line in transactions:
        line = line.strip()
        if not line:
            continue
        item_name, price_str = line.rsplit(" ", 1)
        price = int(price_str)
        totals[item_name] = totals.get(item_name, 0) + price
    return totals


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    n = int(lines[0].strip())
    transactions = lines[1 : 1 + n]
    result = compute_supermarket_totals(transactions)
    for item, net_price in result.items():
        print(f"{item} {net_price}")


if __name__ == "__main__":
    sample_data = [
        "BANANA FRIES 12",
        "POTATO CHIPS 30",
        "APPLE JUICE 10",
        "CANDY 5",
        "APPLE JUICE 10",
        "CANDY 5",
        "CANDY 5",
        "CANDY 5",
        "POTATO CHIPS 30",
    ]
    totals = compute_supermarket_totals(sample_data)
    expected = [
        ("BANANA FRIES", 12),
        ("POTATO CHIPS", 60),
        ("APPLE JUICE", 20),
        ("CANDY", 20),
    ]
    print("Computed Totals:")
    for item, net in totals.items():
        print(f"{item} {net}")
    assert list(totals.items()) == expected, "Mismatch in supermarket totals!"
    print("Supermarket OrderedDict test passed successfully!")
