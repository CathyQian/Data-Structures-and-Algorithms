"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, '', 4, res)
        return res
    
    def dfs(self, s, start, path, parts, res):
        if start == len(s) and parts == 0:
            res.append(path[:-1]) 
    
        elif parts <= len(s) - start and 3*parts >= len(s) - start:
            for i in range(1,4):
                if int(s[start:start + i]) <= 255 and (i > 1 and int(s[start]) != 0 or i == 1):
                    self.dfs(s, start + i, path + s[start:start + i] + '.', parts - 1, res)

          
