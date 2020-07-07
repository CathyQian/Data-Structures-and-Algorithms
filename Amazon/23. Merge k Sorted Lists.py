"""
[Leetcode](https://leetcode.com/problems/merge-k-sorted-lists/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
   
from heapq import heapify, heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodelist = [(node.val, i, node) for i, node in enumerate(lists) if node] # if 
        heapify(nodelist)
        head = ListNode(-1)
        node = head
        while nodelist:
            (_, idx, new) = heappop(nodelist)
            node.next = new
            node = node.next
            if new.next:
                heappush(nodelist, (new.next.val, idx, new.next))
        return head.next
                

 # binary heap, adding/insertion O(logN), delete: O(logn)
 # time complexity: O(Nlogk) # N is the number of lists, k is the max length of these lists
 # Space complexity: O(M) # M is the total number of list nodes            