"""
Max Stack

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:

    MaxStack() Initializes the stack object.
    void push(int x) Pushes element x onto the stack.
    int pop() Removes the element on top of the stack and returns it.
    int top() Gets the element on the top of the stack without removing it.
    int peekMax() Retrieves the maximum element in the stack without removing it.
    int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

 

Example 1:

Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]

Explanation
MaxStack stk = new MaxStack();
stk.push(5);   // [5] the top of the stack and the maximum number is 5.
stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, 5] the stack did not change.
stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [5, 1] the stack did not change.
stk.peekMax(); // return 5, [5, 1] the stack did not change.
stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
stk.top();     // return 5, [5] the stack did not change.

 

Constraints:

    -107 <= x <= 107
    At most 104 calls will be made to push, pop, top, peekMax, and popMax.
    There will be at least one element in the stack when pop, top, peekMax, or popMax is called.

"""

import heapq

class MaxStack:

    def __init__(self):
        self.soft_deleted = set()
        self.max_heap = []
        self.stack = []
        self.next_id = 0
        
    def push(self, x: int) -> None:
        heapq.heappush(self.max_heap, (-x, self.next_id))
        self.stack.append((x, self.next_id))
        self.next_id -= 1

    def _clean_up(self):
        # clean up from the end, if some residual elements, OK, since only need to retrieve terminal elements
        #print('stack', self.stack)
        #print('max heap', self.max_heap)
        #print('soft deleted', self.soft_deleted)
        while self.stack and self.stack[-1][1] in self.soft_deleted:
            self.soft_deleted.remove(self.stack.pop()[1])
        while self.max_heap and self.max_heap[0][1] in self.soft_deleted:
            self.soft_deleted.remove(heapq.heappop(self.max_heap)[1])
    
    def pop(self) -> int: # need to remove element
        res_val, res_index = self.stack.pop()
        self.soft_deleted.add(res_index)
        self._clean_up()
        return res_val
        
    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.max_heap[0][0]
        
    def popMax(self) -> int: # need to remove element
        value, time = heapq.heappop(self.max_heap)
        self.soft_deleted.add(time)
        self._clean_up()
        
        return value * -1


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# slower but more straightforward

import heapq

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, -x) # O(logn)

    def pop(self) -> int:
        ele = self.stack.pop(-1)
        
        # remove ele from self.heap
        idx = self.heap.index(-ele) # O(n)
        self.heap[idx] = self.heap[-1]
        self.heap.pop()
        heapq.heapify(self.heap) # O(n)
        
        return ele
        
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return - self.heap[0]

    def popMax(self) -> int:
        ele = heapq.heappop(self.heap) # O(logn)
        idx = self.stack[::-1].index(-ele) # O(n)
        idx = len(self.stack) - idx - 1
        self.stack = self.stack[:idx] + self.stack[idx+1:]
        print(self.stack)
        return -ele


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
