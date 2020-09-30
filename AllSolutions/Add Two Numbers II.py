"""
Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the 
two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# reverse linked list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        Dummy = ListNode(-1)
        cur = Dummy
        residual = 0
        while l1 or l2:
            total = residual
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            cur.next = ListNode(total%10)
            cur = cur.next
            residual = total//10
        if residual > 0:
            cur.next = ListNode(residual)
        return self.reverse(Dummy.next)
    
    def reverse(self, root):
        pre, cur = None, root
        while cur:
            post = cur.next
            cur.next = pre
            pre, cur = cur, post
        return pre


# follow up, not modify the linked list, use stack instead (preferred)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        cur = None
        residual = 0
        while stack1 or stack2:
            total = residual
            if stack1:
                v1 = stack1.pop(-1)
                total += v1
            if stack2:
                v2 = stack2.pop(-1)
                total += v2
            newnode = ListNode(total%10, cur) # build a linked list reversely
            cur = newnode
            residual = total//10
        if residual > 0: #
            newnode = ListNode(residual, cur)
            cur = newnode

        return cur 
