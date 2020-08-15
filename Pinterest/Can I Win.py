"""
Can I Win
"""
"""
https://leetcode.com/problems/can-i-win/discuss/95319/Python-solution-with-detailed-explanation/169008

state: allowed numbers to put in the list
use recursion + memorization to reduce memory


    We create an array allowed which has all the integers from 1 to maxChoosableInteger.
    We test if the input is valid or not i.e. sum(allowed) >= desiredTotal.
    How do we define the state of the game? This answer determines how we will do memoization as well. Clearly list of current allowed numbers are needed to define the state. It might also look that so_far is also required to define the state. However, given all allowed values and the current set of allowed values, so_far is really the difference of the sum of the two. Therefore only allowed values uniquely determine the state.
    How many allowed values sets are possible? The length of the allowed value set can range 1 to maxChoosableInteger(N). So the answer is (N,1) + (N,2) + ..(N,N) where (N,K) means choose K from N. This is equal to 2^N.
    Now at my turn, if the max(allowed) + so_far >= target, then I will win. Otherwise, I choose from the allowed values one by one and recursively call for the other player. If with any choice the opponent fails for sure, then also I can win for sure from this state.
    What is the time complexity? For a brute force solution, the game tree has 10 choices at first level, each of these choices has 9 choices at second level, and so on. So the complexity is N!. But with memoization, we only compute 2^N sub-problems, and in each problem we do O(N) work. So total time complexity is O(N2^N).

"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        self.memo = {'[]': False}
        return self.helper([i for i in range(1, maxChoosableInteger+1)], desiredTotal)
    
    def helper(self, nums, total):
        state = str(nums)
        if state not in self.memo:
            #if total in set(nums) or total == 0: #  wrong
            if nums[-1] >= total: # reach or exceed desiredTotal wins
                self.memo[state] = True
            elif sum(nums) < total: # O(n) time
                self.memo[state] = False
            else:
                self.memo[state] = False
                for i in range(len(nums)): # O(2^n) time since there is 2^n states in total
                    if not self.helper(nums[:i] + nums[i+1:], total - nums[i]): # take elements without replacement
                        self.memo[state] = True
                        break # make sure to jump out of the for loop here
        return self.memo[state]