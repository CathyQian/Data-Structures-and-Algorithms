"""
[937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier 
used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

 

Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.


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
