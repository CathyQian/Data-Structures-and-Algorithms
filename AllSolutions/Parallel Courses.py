"""
Parallel Courses

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], 
representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

Example 1:

Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

Example 2:

Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 
Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.


"""
# BFS for cycle detection and finding shortest path
# time complexity: O(n)
from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        in_degree = {i: 0 for i in range(1, n+1)}
        for r in relations:
            pre, nxt = r[0], r[1]
            adj_list[pre].append(nxt)
            in_degree[nxt] += 1
        numsemesters, orderedCS = 0, []
        q = deque([course for course, cnt in in_degree.items() if cnt == 0])
        q.append('#')
        while q != deque(['#']): # note needs to compare with deque, not list
            cur = q.popleft()
            while cur != '#':
                orderedCS.append(cur)
                if cur in adj_list:    
                    for nxt in adj_list[cur]:
                        in_degree[nxt] -= 1
                        if in_degree[nxt] == 0:
                            q.append(nxt)
                cur = q.popleft()
            q.append('#')
            numsemesters += 1
            if len(orderedCS) == n:
                return numsemesters
        return -1
