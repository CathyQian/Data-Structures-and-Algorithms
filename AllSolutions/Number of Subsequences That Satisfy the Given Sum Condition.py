"""
Number of Subsequences That Satisfy the Given Sum Condition


You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106


"""

# easy to make mistake: treat subsequence as continous subsequence
# solution for continuous subsequence, O(n^2)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_num = [[0]*n for _ in range(n)]
        max_num = [[0]*n for _ in range(n)]
        cnt = 0

        for i in range(n):
            for j in range(i, n):
                if j == i:
                    min_num[i][j] = nums[i]
                    max_num[i][j] = nums[i]
                elif j >= 1:
                    min_num[i][j] = min(min_num[i][j-1], nums[j])
                    max_num[i][j] = max(max_num[i][j-1], nums[j])
                if min_num[i][j] + max_num[i][j] <= target:
                    cnt += 1
        return cnt % (10**9 + 7)


# time complexity: O(nlogn), spcace complexity: O(1)
  class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for i, num in enumerate(nums):
            if num > target//2:
                break
            j = bisect.bisect_right(nums, target-num)
            cnt += 2**(j-i-1)
        return cnt%(10**9 + 7)