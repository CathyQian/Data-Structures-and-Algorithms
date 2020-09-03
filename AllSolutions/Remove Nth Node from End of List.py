"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Accepted
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # one-pass solution
        dummy = ListNode(0) # dummy needed because head may be deleted
        dummy.next = head
        pre, fast, slow = dummy, head, head
        count = 0
        
        # fast pointer go to the nth element
        while count < n:
            fast = fast.next
            count += 1
        
        # move fast and slow pointer together until the fast pointer to the end of the list
        
        while fast:
            pre = slow
            slow, fast = slow.next, fast.next
        
        # delete curr
        pre.next = slow.next
       
        return dummy.next