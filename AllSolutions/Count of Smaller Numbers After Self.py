#method 1 
class Solution:
    def merge_sort(self, enums):
        half = len(enums) // 2

        if half:
            left = self.merge_sort(enums[:half])         
            right = self.merge_sort(enums[half:])
            for i in range (len(enums))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    self.smaller[left[-1][0]] += len(right)
                    enums[i] = left.pop()
                else:
                    enums[i] = right.pop()
        return enums
    
    def countSmaller(self, nums):
        self.smaller = [0] * len(nums) 
        enums = list(enumerate(nums))
        self.merge_sort(enums)
        return self.smaller


#method 2  --- time exceed limit in leetcode (O(NlogN))
class Solution:
    def bs_insert(self, num, sorted_list):
            left, right = 0, len(sorted_list) -1
            while left <= right:
                mid = left + (right-left)//2
                if sorted_list[mid] >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            return left, sorted_list[:left]+[num]+sorted_list[left:]
                    
    def countSmaller(self, nums):        
        Sorted_List = []
        counts = []
        for i in nums[::-1]:
            count, Sorted_List= self.bs_insert(i, Sorted_List)
            counts.append(count)
        return counts[::-1]
        
# method 3: O(NlogN)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return []
        res = [0]
        stack = [nums[-1]]
        for i in range(len(nums) - 1)[::-1]:
            loc = bisect.bisect_left(stack, nums[i])
            res.append(loc)
            stack = stack[:loc] + [nums[i]] + stack[loc:]
        return res[::-1]