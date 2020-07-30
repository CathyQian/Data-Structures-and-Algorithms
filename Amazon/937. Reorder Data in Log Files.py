"""
[937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
"""

# fastest solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets, digs = [], []
        dic = {}
        for s in logs:
            slist = s.split()
            if slist[1][0].isdigit():
                digs.append(s)
            else:
                reversed_s = ' '.join(slist[1:] + [slist[0]])
                lets.append(reversed_s)
                dic[reversed_s] = s
        lets.sort()
        new_lets = []
        for l in lets:
            new_lets.append(dic[l])
        return new_lets + digs
            
# slightly slower, but more concise code
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets, digs = [], []
        for s in logs:
            slist = s.split()
            if slist[1][0].isdigit():
                digs.append(s)
            else:
                lets.append(s)
                
        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return lets + digs