"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = None, head # pre needed (or else, there will be loops in the result); can only initialize to None
        while cur:
            post = cur.next
            cur.next = pre
            pre, cur = cur, post
        return pre
    
# recursive solution:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        root = self.reverseList(head.next)
        cur = root
        while cur.next:
            cur = cur.next
        cur.next = head
        head.next = None
        return root