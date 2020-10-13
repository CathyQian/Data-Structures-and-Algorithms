"""
Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""
"""
下面两种解法的思路是一样的，都是遍历所有combination,看有没有和等于总和的一半
"""
# find all possible combinations, time complexity O(n2)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums)//2
        curr = set([target])
        for idx, num in enumerate(nums):
            new = set() # start new
            for val in curr:
                if val > num:
                    new.add(val-num)
                if val == num:
                    return True
            curr.update(new)
        return False

 # dp solution   
 """
 https://www.cnblogs.com/grandyang/p/5951422.html
 定义一个一维的 dp 数组，其中 dp[i] 表示原数组是否可以取出若干个数字，其和为i。那么最后只需要返回 dp[target] 就行了。
 初始化 dp[0] 为 true，由于题目中限制了所有数字为正数，就不用担心会出现和为0或者负数的情况。关键问题就是要找出状态转移
 方程了，需要遍历原数组中的数字，对于遍历到的每个数字 nums[i]，需要更新 dp 数组，既然最终目标是想知道 dp[target] 的 
 boolean 值，就要想办法用数组中的数字去凑出 target，因为都是正数，所以只会越加越大，加上 nums[i] 就有可能会组成区间
  [nums[i], target] 中的某个值，那么对于这个区间中的任意一个数字j，如果 dp[j - nums[i]] 为 true 
   j-nums[i] 这个数字了，再加上 nums[i]，就可以组成数字j了，那么 dp[j] 就一定为 true。如果之前 dp[j] 已经为 true 了，
   当然还要保持 true，所以还要 ‘或’ 上自身，于是状态转移方程如下：

dp[j] = dp[j] || dp[j - nums[i]]         (nums[i] <= j <= target)

有了状态转移方程，就可以写出代码了，这里需要特别注意的是，第二个 for 循环一定要从 target 遍历到 nums[i]，而不能反过来，
想想为什么呢？因为如果从 nums[i] 遍历到 target 的话，假如 nums[i]=1 的话，那么 [1, target] 中所有的 dp 值都是 true，
因为 dp[0] 是 true，dp[1] 会或上 dp[0]，为 true，dp[2] 会或上 dp[1]，为 true，依此类推，完全使的 dp 数组失效了
 """    
class Solution:        
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target, n = total // 2, len(nums)
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]   
                if dp[target]:
                    return True
        return dp[target]

# dfs solution, find all combinations, time complexity O(n!)  --- time exceed limit
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        self.visited = [False] * len(nums) # record which numbers has been used so far
        target = sum(nums) // 2
        return self.dfs(0, 0, nums, target)

    def dfs(self, start, curr, nums, target):
        if curr > target: 
            return False

        if curr == target:   
            return True

        for i in range(start, len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                if self.dfs(i+1, curr + nums[i], nums, target):
                    return True
                self.visited[i] = False
        return False
