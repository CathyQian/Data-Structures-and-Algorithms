"""
Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.



"""
# hashmap, time O(N), space O(N)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ch_cnts = collections.defaultdict(int)
        for ch in s:
            ch_cnts[ch] += 1
        # each letter appears in at most one part --> cnts decrease to 0 for that ch
        res = []
        ch_cnts_copy = copy.deepcopy(ch_cnts)
        left, cur_cnts = 0, 0
        for i, ch in enumerate(s):
            ch_cnts[ch] -= 1  
            if ch_cnts[ch] == 0:
                cur_cnts += ch_cnts_copy[ch] # key
                if cur_cnts == i - left + 1: # used only between left and i
                    res.append(i-left+1)
                    left, cur_cnts = i+1, 0
        return res

# similar but simplier, time O(N), space O(1)
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c]) # intelligent
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans
    
# Both time complexity O(N)