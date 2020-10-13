"""
Implement min Heap

min Heap in Python is a complete binary tree (missing nodes only in the last level)
"""
"""
How is Min Heap represented ?
A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array. 
The root element will be at Arr[0]. For any ith node, i.e., Arr[i]:

    Arr[(i -1) / 2] returns its parent node.
    Arr[(2 * i) + 1] returns its left child node.
    Arr[(2 * i) + 2] returns its right child node.

    parent i --- 0, left child --- 1, right child --- 2
    child ---- 1 or 2, parent --- 0

    getMin(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).
    extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Log n) as this operation needs to maintain the heap property (by calling heapify()) after removing root.
    insert(): Inserting a new key takes O(Log n) time. We add a new key at the end of the tree. If new key is larger than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

child node value <= parent node value
"""

# Python3 implementation of Min Heap 

class MinHeap: 

    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0 # # of elements in heap, decide on the end of the heap (notice the extra numbers are not removed)
        self.Heap = [0]*(self.maxsize) # index starts from 0

    def heapifyHelper(self, pos):
        # percolation down (from top to bottom), O(logn)
        if 2*pos + 1 < self.size: # if it is not a leave (has at least one child)
            smallest = pos
            l_pos, r_pos = 2 * pos + 1, 2 * pos + 2
            if l_pos < self.size and self.Heap[l_pos] < self.Heap[smallest] :
                smallest = l_pos
            if r_pos < self.size and self.Heap[r_pos] < self.Heap[smallest]:
                smallest = r_pos
            if smallest != pos:
                self.Heap[smallest], self.Heap[pos] = self.Heap[smallest], self.Heap[pos]
                    self.heapifyHeaper(smallest) 

    def heapify(self):
        # transform an unsorted list to a minheap, O(n) --- why is it O(n)? worst case scenario
        for pos in range((self.size - 1) // 2, -1, -1): # don't consider leaves
            self.heapifyHelper(pos) 
            
    # Function to insert a node into the heap 
    def push(self, element):
        # percolation up (bottom to up), O(logn)
        if self.size >= self.maxsize: 
            return
        self.Heap[self.size] = element # add as leave
        
        curr = self.size 
        parent = (curr - 1) // 2
        while self.Heap[curr] < self.Heap[(parent)]: # swap with parent
            self.Heap[curr], self.Heap[parent] = self.Heap[parent], self.Heap[curr] 
            curr = parent
            parent = (curr-1)//2
        
        self.size += 1

    def pop(self): # O(logn)
        popped = self.Heap[0] # O(1)
        self.Heap[0] = self.Heap[self.size-1] 
        self.size -= 1
        self.heapifyHelper(0)
        return popped  

    
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(self.size//2): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 2])) # may have no right child

# Driver Code 
if __name__ == "__main__": 
    print('The minHeap is ') 
    minHeap = MinHeap(15) 
    minHeap.push(5) 
    minHeap.push(3) 
    minHeap.push(17) 
    minHeap.push(10) 
    minHeap.push(84) 
    minHeap.push(19) 
    minHeap.push(6) 
    minHeap.push(22) 
    minHeap.push(9) 
    minHeap.minHeap() 

    minHeap.Print() 
    print("The Min val is " + str(minHeap.pop())) 
    minHeap.Print()
