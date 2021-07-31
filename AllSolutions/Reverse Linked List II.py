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

# easier to understand

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        count = 0
        cur = dummy
        
        while count < left:
            pre_l, cur = cur, cur.next
            count += 1
        node_l = cur
        
        while count < right:
            cur = cur.next
            count += 1
        node_r = cur
        post_r = cur.next
        
        newhead, newtail = self.reverse(node_l, node_r)
        pre_l.next = newhead
        newtail.next = post_r
        
        return dummy.next
        
    def reverse(self, head, tail):
        # reverse list
        dummy = None
        pre, cur = dummy, head
        
        while cur and pre != tail:
            post = cur.next
            cur.next = pre
            pre, cur = cur, post
            
        return pre, head
        
