"""
Random Pick with Blacklist

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer
from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

    1 <= N <= 1000000000
    0 <= B.length < min(100000, N)
    [0, N) does NOT include N. See interval notation.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]

Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]

Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]

Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
"""
这道题的最直接的思路是新建一个list,里面填满从0到n-1但是不在B里面的整数，然后randrange(len(list)), return list(idx)
这样会time exceed limit,因为题目不许重新建一个list(too much time and space consumption)

下面的思路非常巧妙：M = N - len(B)
随机取一个从0到M-1的整数，如果这个数不在B里面，可以直接返回
如果这个数在B里面，不能直接返回，需要做些mapping
那么怎么做mapping呢, mapping到一个大于等于M且不在B里面的数

扫描B里面的元素，如果这个数>=M, 这个数肯定不能通过randrange(M)随机取到，不用处理
如果这个数<M, 这个数会通过randrange(M)取到，需要mapping到一个大于等于M且不在B里面的数
注意为什么一定要大于等于M呢，因为小于M的数会被randrange(M)随机取到，不需要mapping

time & space complexity: O(len(B))
"""
class Solution:
    def __init__(self, N: int, B: List[int]):
        blackset = set(B)
        self.threshold = N - len(B)
        self.dic = {}
        j = self.threshold
        for b in blackset:
            if b < self.threshold:
                while j in blackset:
                    j += 1
                self.dic[b] = j
                j += 1

    def pick(self) -> int:
        i = randrange(self.threshold)
        return self.dic.get(i,i)

# brutal force, time exceed limit
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.n = N
        self.blacklist = set(blacklist)
    
    def pick(self) -> int:
        self.candidate = []
        for i in range(self.n):
            if i not in self.blacklist:
                self.candidate.append(i)
        idx = random.randrange(0, len(self.candidate))
        return self.candidate[idx]
