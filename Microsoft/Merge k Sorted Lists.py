"""
Merge k Sorted Lists

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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 


import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        nodes = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(nodes)
        
        Dummy = ListNode(-1)
        cur = Dummy
        while nodes:
            val, idx, node = heapq.heappop(nodes)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(nodes, (node.next.val, idx, node.next))
        return Dummy.next
    

# This problem is hard because  1) use minheap, make sure elements in the heap are (node.val, idx, node) to allow comparison 
# 2) time & space complexity analysis
#
"""
Time complexity : O(Nlog⁡k) where k is the number of linked lists.
    heapify is one time operation (outside while loop) that takes O(k) time, much less than O(nlogk)
    The comparison cost will be reduced to O(log⁡k) for every pop and insertion to priority queue.
    Adding a node to the linked list is O(1)
    There are N nodes in the final linked list.

Space complexity :

    O(n) Creating a new linked list costs O(n) space.
    O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented 
    with heaps) costs O(k) space (it's far less than N in most situations). 
     
"""