"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of 
largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights +[0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 # not width = i - stack[-1] as the last element has already popped out
                max_area = max(max_area, height*width)
            stack.append(i)
        return max_area


"""
maintain an ascending stack to keep the index/height,
whenever a new element is smaller than the top element of the stack, it's time to 
calculate max area of the past blocks which equals to height * width. Given that 
the stack is ascending, so the width is the difference between idx highest element
 and the current idx, the height is the current element. 
When finish, the new element is put into the stack to maintain the ascending order.

To make sure the first and last element will be counted, add 0 to both ends of the list.
"""
