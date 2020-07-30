"""
[138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        new = collections.defaultdict(lambda: Node(0))
        new[None] = None
        node = head
        while node:
            new[node].val = node.val
            new[node].next = new[node.next]
            new[node].random = new[node.random]
            node = node.next
        return new[head]