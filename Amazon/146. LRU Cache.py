"""
[146. LRU Cache](https://leetcode.com/problems/lru-cache/)
"""

# O(n) solution
class LRUCache:

    def __init__(self, capacity: int):
        self.keys = deque()
        self.ele = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.ele:
            self.put(key, self.ele[key])
            return self.ele[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.ele:
            if len(self.keys) == self.capacity:
                out = self.keys.pop()
                del self.ele[out]   
            self.keys.appendleft(key)
            self.ele[key] = value
        else:
            self.ele[key] = value
            self.keys.remove(key) # O(n)
            self.keys.appendleft(key)
 
 # O(1) solution
 #Method 1: double-linked list + dictionary
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.post = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.post = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        prev, post = node.prev, node.post
        prev.post = post
        post.prev = prev
        del self.cache[node.key]
        return
        
    def _add(self, node):
        post = self.head.post
        self.head.post = node
        node.post = post
        post.prev = node
        node.prev = self.head
        self.cache[node.key] = node
        return 
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val
            self.put(key, value)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            
        if len(self.cache) == self.capacity:
            node = self.tail.prev
            self._remove(node)
        
        insert = Node(key,value)
        self._add(insert)
        return



# using OrderedDict, (move_to_end, popitem), don't use it in the interview
from collections import OrderedDict        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value