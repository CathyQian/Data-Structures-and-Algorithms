"""
Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length


"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        flowerbed_ = [0] + flowerbed + [0]
        while i < len(flowerbed) + 1:
            if flowerbed_[i] == 0:
                if flowerbed_[i+1] == 0 and flowerbed_[i-1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        
            if n <= 0:
                break
    
        return n <= 0
    
    # time -- O(n), space = O(n)
