"""
Problem 3: Merge Two Sorted Lists
----------------------------------
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iterative Two-Pointer Approach with Dummy Node:
    ------------------------------------------------
    We use a dummy head to easily build the merged linked list without edge cases
    around initializing the head.
    Compare the current nodes of list1 and list2, attach the smaller node to the merged list,
    and advance the corresponding pointer.
    Once one list is exhausted, attach the remainder of the other list.

    Time Complexity: O(n + m) - where n and m are lengths of list1 and list2.
    Space Complexity: O(1) - Only a few pointers are used (no extra list nodes created).
    """
    dummy = ListNode(-1)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    # Append the remaining elements
    current.next = list1 if list1 is not None else list2
    
    return dummy.next

# Helper functions for demonstration / testing
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([5], [1, 2, 4])
    ]
    for arr1, arr2 in test_cases:
        l1 = build_linked_list(arr1)
        l2 = build_linked_list(arr2)
        merged = mergeTwoLists(l1, l2)
        print(f"list1: {arr1}, list2: {arr2} -> merged: {linked_list_to_list(merged)}")
