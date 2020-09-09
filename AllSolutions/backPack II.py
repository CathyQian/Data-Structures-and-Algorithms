# backpack II
"""
Given n items with size A[i] and value V[i], and a backpack with size m. 
What's the maximum value can you put into the backpack?
"""
# similar to backPackI but replace A with V when calculating f
class Solution:
    def backPackII(self, m, A, V):
        pre = [0 for _ in range(m+1)]
        for i in range(len(A)):
            post = pre.copy() # shallow copy
            for j in range(1, m+1):
                if j >= A[i]:
                    post[j] = max(pre[j], pre[j-A[i]] + V[i])
            pre = post
        return pre[-1]
