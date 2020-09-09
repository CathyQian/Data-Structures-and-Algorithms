"""
Given n items with size A[i], an integer m denotes the size of a backpack. How full you can fill this backpack?
"""
"""
This is a classical problem to use dynamic programming.
state f[j]: maximum sum item size when backpack size is j and A[0:i+1] elements are allowed to put into 
            the backpack.
function: if j >= A[i]: f[j] = max(pre[j], pre[j - A[i]] + A[i])
          else: f[j] = pre[j]
initialization:f = [0 for _ in range(m)]
return f[m-1]

"""
class Solution:
    def backPack(self, m, A):
        pre = [0 for _ in range(m+1)]
        n = len(A)
        for i in range(n):
            post = pre.copy() # important
            for j in range(1, m+1):
                if j >= A[i]:
                    post[j] = max(pre[j], pre[j-A[i]] + A[i])
            pre = post
        return pre[-1]
