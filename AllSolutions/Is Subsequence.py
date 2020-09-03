"""
Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
 of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a 
 subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T
has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 10^4
    Both strings consists only of lowercase characters.

"""
# only one s
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t or len(t) < len(s):
            return False
        i, j = 0, 0
        while j < len(t):
            if t[j] == s[i]:
                if i == len(s) - 1:
                    return True
                else:
                    i += 1
            j += 1
        return False

# follow up, large influx of s
import collections

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_dict = collections.defaultdict(list)
        for i, a in enumerate(t):
            t_dict[a].append(i)
            
        pre = -1
        for ss in s:
            if ss in t_dict.keys():
                idx = self.binarySearch(pre, t_dict[ss])
                if idx > pre:
                    pre = idx
                else:
                    return False
            else:
                return False
        return True
    
    def binarySearch(self, target, nums):
        # find the first element larger than target in nums
        # if cannot find, return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start] if start < len(nums) else -1