"""
Implement k-means clustering algorithm


"""
# can use numpy
import numpy as np
class Solution:
    def kMeans(self, X, K):
        Cx = np.random.random_sample(K)*(np.max(X)- np.min(X)) + np.min(X)
        Cy = np.random.random_sample(K)*(np.max(X)- np.min(X)) + np.min(X)
        C = np.array(list(zip(Cx, Cy)), dtype=np.float32)

        for i in range(100):
            m = len(X)
            idx = np.zeros(m)
            for i in range(m):
                dist = np.linalg.norm(X[i] - C, axis = 1)
                idx[i] = np.argmin(dist)

            # update the position of the K centroids
            for i in range(K):
                points = [X[j] for j in range(m) if idx[j] == i]
                C[i] = np.mean(points, axis = 0)
        return C

arrays = [[12, 39], [20, 36], [28, 30], [18, 52], [29, 54], [33, 46], [24, 55],
[45, 59], [45, 63], [52, 70], [51, 66], [52, 63], [55, 58], [53, 23], [55, 14],
[61, 8], [64, 19], [69, 7], [72, 24]]

test = Solution()
test.kMeans(arrays,3)

# don't use numpy
import random, math
class Solution:
    def kMeans(self, X: list[list], K:int) -> list:
        min_x, max_x = min([e[0] for e in X]), max([e[0] for e in X])
        min_y, max_y = min([e[1] for e in X]), max([e[1] for e in X])
        Cx = [random.randrange(min_x, max_x) for _ in range(K)]
        Cy = [random.randrange(min_y, max_y) for _ in range(K)]
        C = list(zip(Cx, Cy)) # need list here
        
        for i in range(100):
            m = len(X)
            idx = [0 for _ in range(m)]
            for i in range(m):
                dist = [self.dist(X[i], C[j]) for j in range(K)]
                idx[i] = dist.index(min(dist))
            # update the position of the K centroids
            for i in range(K):
                points = [X[j] for j in range(m) if idx[j] == i]
                C[i] = [sum([x[0] for x in points])/K, sum([x[1] for x in points])/K]
        return C
    
    def dist(self, x, y):
        return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)