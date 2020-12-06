"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        count = 0
        
        while count < m:
            left_tail, cur = cur, cur.next
            count += 1
        
        mid_tail = cur
        mid_head = None
        
        while count < n+1:
            post = cur.next
            cur.next = mid_head
            mid_head, cur = cur, post
            count += 1
        left_tail.next = mid_head
        mid_tail.next = cur
        
        return dummy.next
