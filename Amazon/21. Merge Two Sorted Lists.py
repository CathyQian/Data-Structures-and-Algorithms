"""
[Leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur, p1, p2 = dummy, l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        elif p2:
            cur.next = p2
        return dummy.next
        
# more concise solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next
        cur.next = l1 or l2 # this is awesome!
        return head.next