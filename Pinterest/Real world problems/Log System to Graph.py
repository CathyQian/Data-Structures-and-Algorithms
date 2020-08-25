"""
A log System with structure like this (output graph like below)
   ex.
|---register_button (10)
|    |---register_email (4)
|    |    |---email_already_exists (1)
|    |    |---register_success (3)
|    |---register_facebook (4)
|    |    |---register_success (4)
|    |---dropoff (2)
|---login_button (10)
|    |---login_email (4)
|    |    |---login_success (4)
|    |---login_facebook (4)
|    |    |---login_success (3)
|    |    |---login_failure (1)
|    |---dropoff (2)

now we have data with 3 properties (real input data)
user_id, timestamp, action 
100, 1000, A
200, 1003, A
300, 1009, B
100, 1026, B
100, 1030, C
200, 1109, B
200, 1503, A

We want to output a graph to visualize it
Graph from input:
|---A(2)
|   |---B(2) 
|   |   |---C(1)
|   |   |---A(1)
|---B(1)

按user_id聚合，然后按字母顺序, 括号里面代表出现的次数 aggregate by user_id:
100: A -> B -> C
200: A -> B -> A
300: B

1. define data structure and classes
2. construct the graph from logfile
3. print out the graph similar to above
"""
class Trie:
    def __init__(self):
        self.root = collections.defaultdict(int)
        self.root['#'] = 0
class Solution:
    def build_log_system(self, logs)：
        user_id, time_stamp, action = zip(*logs)
        user_id = sorted(list(set(user_id)))

        # construct a trie
        root = Trie()
        for uid in user_id:
            t = root
            for log in logs:
                if log[0] == uid:
                    t[log[2]] += 1
                    t = t[log[2]]
            t['#'] = 0 # end of each path
        
        # traversal
        self.dfs(root)

    def dfs(self, node, level_so_far = ''):
        if node == {'#':0}: # end of the path
            return 
        for next_action in node:
            if next_action != '#':
                print('{}|---{}({})'.format(level_so_far, next_action, node[next_action]))
                self.dfs(node[next_action], level_so_far+'|   ')
        