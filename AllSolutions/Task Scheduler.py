"""
Task Scheduler

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter 
represents a different task. Tasks could be done without the original order of the array. Each task is done in one
 unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same 
letter in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

 

Constraints:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].

"""

# solution: https://www.cnblogs.com/grandyang/p/7098764.html
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = sorted(list(collections.Counter(tasks).items()),key=lambda x: x[1], reverse=True)
        
        max_counts = task_counts[0][1]
        i = 1
        while i < len(task_counts): # can't use for loop here
            if task_counts[i][1] < max_counts:
                break
            i += 1
        return max((n+1)*(max_counts-1) + i, len(tasks))
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = collections.defaultdict(int)
        maxcount = 0
        for task in tasks:
            task_count[task] += 1
            maxcount = max(maxcount, task_count[task])
        m = 0
        for task, count in task_count.items():
            if count == maxcount:
                m += 1
        return max(len(tasks), max(m, n+1)*(maxcount-1) + m)
            