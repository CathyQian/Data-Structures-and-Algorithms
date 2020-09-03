"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    Methods pop, top and getMin operations will always be called on non-empty stacks.

"""


# use double stack
# alternatively, use one stack and self.min (too convoluted)

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            nextmin = min(x, self.minstack[-1])
            self.minstack.append(nextmin)
                
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self): # doesn't pop, only retrieve
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()