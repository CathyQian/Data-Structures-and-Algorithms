"""
Pour Water

You are given an elevation map represents as an integer array heights where heights[i] representing the height of the terrain at index i. The width at each index is 1. You are also given two integers volume and k. volume units of water will fall at index k.

Water first drops at the index k and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise to its current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, level means the height of the terrain plus any water in that column.

We can assume there is infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than one grid block, and each unit of water has to be in exactly one block.

Input: heights = [2,1,1,2,1,2,2], volume = 4, k = 3
Output: [2,2,2,3,2,2,2]
Explanation:
The first drop of water lands at index k = 3. When moving left or right, the water can only move to the same level or a lower level. (By level, we mean the total height of the terrain plus any water in that column.)
Since moving left will eventually make it fall, it moves left. (A droplet "made to fall" means go to a lower height than it was at previously.) Since moving left will not make it fall, it stays in place.

The next droplet falls at index k = 3. Since the new droplet moving left will eventually make it fall, it moves left. Notice that the droplet still preferred to move left, even though it could move right (and moving right makes it fall quicker.)

Example 2:

Input: heights = [1,2,3,4], volume = 2, k = 2
Output: [2,3,3,4]
Explanation: The last droplet settles at index 1, since moving further left would not cause it to eventually fall to a lower height.
Example 3:

Input: heights = [3,1,3], volume = 5, k = 1
Output: [4,4,4]
 

Constraints:

1 <= heights.length <= 100
0 <= heights[i] <= 99
0 <= volume <= 2000
0 <= k < heights.length

"""
# O(NK) time complexity
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):

            # first explore left
            # if decreasing, keep moving left; if equal, record position, keep going left; if bigger, break
            minheight, minidx = heights[k], k
            cur = k 
            while cur - 1 >= 0 and heights[cur-1] <= heights[cur]:
                if heights[cur-1] < minheight:
                    minheight = heights[cur-1]
                    minidx = cur - 1
                cur -= 1
            if minidx != k: # found a place on the left
                heights[minidx] += 1
                continue
        
            # then explore right
            minheight, minidx = heights[k], k
            cur = k 
            while cur + 1 < len(heights) and heights[cur+1] <= heights[cur]:
                if heights[cur+1] < minheight:
                    minheight = heights[cur+1]
                    minidx = cur + 1
                cur += 1
            # if minidx != k: # found a place on the right
            #     heights[minidx] += 1
            #     continue

            # # if not left/right, stay here
            # else:
            #     heights[k] += 1
            heights[minidx] += 1
    
        return heights
            

# a simplier version, O (nk), u
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume): 
            kk = k
            for i in reversed(range(k)): 
                if heights[i] < heights[i+1]: # update kk only when there's a drop in height
                    kk = i
                elif heights[i] > heights[i+1]: 
                    break
            if kk < k: 
                heights[kk] += 1
                continue
            for i in range(k+1, len(heights)): 
                if heights[i-1] > heights[i]: 
                    kk = i
                elif heights[i-1] < heights[i]: 
                    break 
            heights[kk] += 1
        return heights
    

# a faster solution O(N+K)
class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        left, right = [], [] # 2 stacks 
        lo = hi = k
        for _ in range(volume): 
            
            while lo and heights[lo-1] <= heights[lo]: # can't move out of the for loop
                if heights[lo-1] < heights[lo]: 
                    left.append(lo-1)
                lo -= 1

            while hi+1 < len(heights) and heights[hi] >= heights[hi+1]: # can't move out of the for loop
                if heights[hi] > heights[hi+1]: 
                    right.append(hi+1)
                hi += 1
                
            if left:  # tricky
                i = left[-1]
                heights[i] += 1
                if heights[i] == heights[i+1]: 
                    left.pop()
                if lo <= i-1: 
                    left.append(i-1)

            elif right: # tricky
                i = right[-1]
                heights[i] += 1
                if heights[i-1] == heights[i]: 
                    right.pop()
                if i+1 <= hi: 
                    right.append(i+1)

            else: 
                heights[k] += 1
                if k and heights[k-1] < heights[k]: 
                    left.append(k-1)
                if k+1 < len(heights) and heights[k] > heights[k+1]: 
                    right.append(k+1)

        return heights