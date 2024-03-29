"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all types, not just integer?

"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

"""
Iterator: 
The first property of an Iterator that we'll looked at is that it only needs to know how to get the next item. It doesn't need to store the entire data 
in memory if we don't need the entire data structure. For massive data structures, this is invaluable!
Another really interesting property of Iterators is that they can represent sequences without even using a data structure!

"""


# use cache to store next element
class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self.cache = None

    def peek(self):
        if not self.cache: 
            self.cache = self._iterator.next()
        return self.cache

    def next(self):
        if self.cache: 
            val, self.cache = self.cache, None
            return val
        else: 
            return self._iterator.next()
        
    def hasNext(self):
        return self._iterator.hasNext() or self.cache != None
    
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].