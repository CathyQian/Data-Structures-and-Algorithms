"""
LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

 

Follow up:
Could you do both operations in O(1) time complexity?

 

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

 

"""
# LFUCache: quite hard
from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.space = capacity
        self.key2node = {} # key:node
        self.count2node = defaultdict(OrderedDict) #{count: {key: node}}
        self.minCount = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        # clean memory
        if not self.count2node[node.count]: # if empty, clean memory
            del self.count2node[node.count]
        
        node.count += 1
        self.count2node[node.count][key] = node
        
        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1
            
            
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.space == 0 and not self.key2node:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key) # NOTICE, put makes count+1 too
            return
        
        if self.space == 0:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False) # the most important line of code
            del self.key2node[k] 
            self.space += 1
        
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        self.space -= 1
        return

# LRUCache: https://leetcode.com/problems/lru-cache/

import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.keys = collections.deque()
        self.ele = {}
        self.maxlength = capacity
        
    def get(self, key: int) -> int:
        if key in self.ele:
            self.put(key, self.ele[key])
            return self.ele[key]
        return -1
    
    def put(self, key: int, value: int) -> None:

        if key in self.ele:
            self.ele[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        else:
            
            if len(self.keys) == self.maxlength:
                out = self.keys.popleft()
                del self.ele[out]
            self.keys.append(key)
            self.ele[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)