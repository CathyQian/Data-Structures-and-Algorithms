"""
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# space complexity: O(n), time complexity: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        visited = set([head])
        cur = head
        while cur.next:
            if cur.next in visited:
                return True
            else:
                visited.add(cur.next)
            cur = cur.next
        return False

# space complexity: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while fast and fast.next: # can't be just fast.next
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False