"""
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 0
        temp = head
        
        while temp:
            temp = temp.next
            length += 1
        
        rotateTimes = k%length
        if k == 0 or rotateTimes == 0:
            return head
        
        fastPointer, slowPointer = head, head
        while rotateTimes > 0:
            fastPointer = fastPointer.next
            rotateTimes -= 1
        
        while fastPointer.next:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
            
        newhead = slowPointer.next
        slowPointer.next = None
        fastPointer.next = head
        
        return newhead