"""
Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

import collections 

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: # x, y not in the same set
            if self.rank[x] < self.rank[y]: 
                x, y = y, x
            self.parent[y] = x 
            if self.rank[x] == self.rank[y]: 
                self.rank[x] += 1
               
class Solution:       
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        mail2name = {} # mail: name map, mail is unique, name is not unique
        for acc in accounts:
            name = acc[0]
            for mail in acc[1:]:
                if mail not in mail2name:
                    mail2name[mail] = name
        
        uf = UnionFind()
        for acc in accounts:
            pre = None
            for mail in acc[1:]:
                if mail not in uf.parent:
                    uf.parent[mail] = mail
                    uf.rank[mail] = 0
                if pre:
                    uf.union(pre, mail)
                pre = mail
                
        # uf.parent : mail: pmail       
        pmail2mail = collections.defaultdict(list) # parentmail: mail
        for mail in uf.parent:
            pmail = uf.find(mail) # critical, make sure the pmail is updated    
            pmail2mail[pmail].append(mail)  
        
        ans = []
        for k,v in pmail2mail.items():
            v.sort()
            ans.append(mail2name[k]]+v)
            
        return ans