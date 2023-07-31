"""
Smallest Common Region

You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
Example 2:

Input: regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
Output: "Earth"

Constraints:

2 <= regions.length <= 104
2 <= regions[i].length <= 20
1 <= regions[i][j].length, region1.length, region2.length <= 20
region1 != region2
regions[i][j], region1, and region2 consist of English letters.
"""
# similar to lowest common ancestors, but building a tree is quite a lot of trouble --> use hashtable instead

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        #First build a nested dictionary
        #Second find the nearest ancestor of the two regions    
        lookupdic = {}
        for i in range(len(regions)):
            parent, children = regions[i][0], regions[i][1:]
            for child in children:
                if child not in lookupdic:
                    lookupdic[child] = parent

        def getAncestors(region, mapping):
            res = [region]
            while region in mapping:
                res.append(mapping[region])
                region = mapping[region]
            
            return res[::-1]
        
        ancestors1 = getAncestors(region1, lookupdic)
        ancestors2 = getAncestors(region2, lookupdic)

        target = 0
        for i in range(min(len(ancestors1), len(ancestors2))):
            if ancestors1[i] == ancestors2[i]:
                target = i
            else:
                break

        return ancestors1[target]

# a shorter version to find the divergence point
# both time and space complexity O(n) --- n: total number of nodes
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for i in range(1,len(region)):
                parent[region[i]] = region[0]
        chain = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            chain.add(region1)
        while region2 not in chain:
            region2 = parent[region2]
        return region2 
    

# implement a tree and LCA; more complex than previous two methods, but good way to learn how to do LCA without a tree
import collections
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        lookupdic = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for region in regions:
            parent, children = region[0], region[1:]
            for child in children:
                lookupdic[parent].append(child)
                indegree[child] += 1

        for key, value in indegree.items():
            if value == 0: # this key is root
                return self.LCA(key, lookupdic, region1, region2)
                
    def LCA(self, root, graph, a, b):
        if root == a or root == b:
            return root
        count = 0
        result = None
        for child in graph[root]: # this is the key part
            lca = self.LCA(child, graph, a, b)
            if lca:
                count += 1
                result = lca
            if count == 2: # one left; one right
                return root
        return result