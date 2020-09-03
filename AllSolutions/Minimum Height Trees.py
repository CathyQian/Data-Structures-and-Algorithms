"""
For a undirected graph with tree characteristics, we can choose any node as the
root. The result graph is then a rooted tree. Among all possible rooted trees,
those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given
the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are
undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph
in which any two vertices are connected by exactly one path. In other words, any
connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path
between the root and a leaf.
"""

"""
一个类似剥洋葱的方法，就是一层一层的褪去叶节点，最后剩下的一个或两个节点就是我们要求的最小
高度树的根节点，
我们需要建立一个图g，是一个二维数组，其中g[i]是一个一维数组，保存了i节点可以到达的所有节点。
开始将所有只有一个连接边的节点(叶节点)都存入到一个队列queue中，然后我们遍历每一个叶节点，
通过图来找到和其相连的节点，并且在其相连节点的集合中将该叶节点删去，如果删完后此节点也也变成
一个叶节点了，加入队列中，再下一轮删除。
那么我们删到什么时候呢，当节点数小于等于2时候停止，此时剩下的一个或两个节点就是我们要求的最小高度树的根节点.

注意：如果剩下三个或者三个以上节点，可以继续剥洋葱；如果剩下两个节点，两个都是我们求的最小高度树
的根节点， 因为无论哪个做根节点都一样； 如果剩下一个， 那就是我们求的根节点
所以之可能返回一个或者两个节点
"""


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # base condition
        if n == 1:
            return [0] 
        
        # when n >= 2
        # build the ajacency table
        adj = [set() for _ in range(n)]
        for (i, j) in edges:
            adj[i].add(j)
            adj[j].add(i)
            
        # get the first layer of leaves 
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        # start to peel of leaves until the last one or two elements
        while n > 2:
            n -= len(leaves)
            # get new leaves
            newleaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newleaves.append(j)
            leaves = newleaves
        return leaves