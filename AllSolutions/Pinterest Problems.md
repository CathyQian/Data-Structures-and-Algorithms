
1hr tech screen
Karat电面，1个小时全程视频+需要把代码debug on coder pad
10 ~20 min ML/project + 三道题，做出2.5道就有onsite 机会，每道题都要先和他们讲思路才能写 24小时内有redo机会
coding只需要complete，不需要optimize


Recent problems from careercup
- write a binary calculator for summing two strings
- given a matrix find the subset sum while performing spiral traversing
- given an input stirng and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. You need to output the minimum number of words. For example, input 'aaaisaname', dic: ("a', 'aaa', 'is', 'name')
output: "aaa is a name"
wrong output: "a a a is a name"

number of island的有2个followup的题
https://leetcode.com/problems/number-of-islands/
https://leetcode.com/problems/number-of-islands-ii/ ?? hard
https://leetcode.com/problems/number-of-distinct-islands/ ?? hard

text justification: https://leetcode.com/problems/text-justification/  (key: last line + space distribution in previous lines)

longest common subsequence: https://leetcode.com/problems/longest-common-subsequence/

meeting room I and II: https://leetcode.com/problems/meeting-rooms-ii/

https://leetcode.com/problems/design-hit-counter/

https://leetcode.com/problems/random-pick-with-blacklist/

word ladder I II: https://leetcode.com/problems/word-ladder/

find celebrity: https://leetcode.com/problems/find-the-celebrity/

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
pin十分喜欢出bfs/dfs了

World Search I and II 只能往右下
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
https://leetcode.com/problems/alien-dictionary/

https://leetcode.com/problems/employee-free-time/
We are given a list schedule of employees, which represents the working time for each employee.Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.Return the list of finit间写出使用priority queue 解法follow up如果time 限定一个小的范围 如何优化 

https://leetcode.com/problems/course-schedule-ii/ (topological sort)

请问找课友是哪题？找intersection？ 输入是每个人上的课， 然后输出是所有课的两两combination，每个combination对应这两门课都上了的人名，如果有一种combination是空的，那也要输出空的list

第一题是给一个list，一个entry是 一个学生id对应一个课程，要求输出每两个学生之间的共同课程。就用hashtable过一遍，比较简单。
第二题是给一个list，一个entry是 一个前置课程和当前课程，包含了所有的课程，要求输出中间的课程。这个用doublu linked list 串起来，然后拿到head后用slow fast pointer找到list的中间点就好了，也是比较简单。但是我当时比较慌一下时间就结束了。。。


2. longest common visit history, 和 longest common substring类似，https://www.geeksforgeeks.org/longest-common-substring-dp-29/，只不过把char变成了string而已

https://leetcode.com/problems/find-peak-element/

https://leetcode.com/problems/paint-house/ 
paint house II

https://leetcode.com/problems/longest-valid-parentheses/


https://leetcode.com/problems/subdomain-visit-count/

CanWin. 给一个数组比如 [2,3,0,3,5]和一个index比如4，从这个index每次可以向左或者向右跳ary[index]的距离， 如果能跳到值为0的index则返回true: https://www.1point3acres.com/bbs/thread-287074-1-1.html


rooms={"A": {"size":2},"B":{"size":3}}, meetings={"m1":{"size":2, "start": 1200, "end" :1300},"m2":{"size":3,"start":1300,"end":1400}}。我用的python,大概就是dict of dict
类似刷题网的meeting room？先按开始时间排序，然后用heap存结束时间，keep track of number for each ongoing meeting, always assign the new meeting to the meeting room with least capacity.

做一个 word wrap, 输入 wordList 和一个数字 number，把单词按顺序用 "-" 连接起来，长度不能超过 number. 输出是一个 list. 


和一道domain提
一道用Python实现几个表格的inner join

用trie存一些words，然后实现一个不同word的查找，在实现一个partial word的查找，比如之前trie里面存了一个ABCD，然后如果输入BCD，或者BC，就可以return true。中国小哥挺放水的，一直在跟我中文聊天。。
Trie, prefix and suffix 查找还是相对比较容易的，但是中间查找感觉很麻烦啊。要全trie dfs 吗


给定一个blacklist phrases，比如[machine guns, world war 1, world, war 2], 然后给定一个pin的文字描述，判断其是否包含blacklist中的phrase。比如“I have machine guns”就是包含，“Let's say no to world war”就是不包含（因为war后面没有1/2）。题意很简单，暴搜就是O(mn)，m

coding就一道题，经典利口耳领领，但分成一步一步来问的。
https://leetcode.com/problems/number-of-islands/
第一个部分是给定一个点，把valid的下一个move的坐标放到一个list里面返回。就是看上下左右四个放下里面哪一个是valid的。
第二部分就是原题代码，但问法不太一样。大概是在map上有个start point，问从start点能不能cover所有的land。
第三部分稍微难一点，也就剩下十分钟不到，我也就说了个思路，面试小哥好像也没有指望我能做出来。就是在map上有一

说先pairwise dfs，找到所有pair之间的可能path，形成一个graph，然后再在新的graph上做dfs，同时记录不能有在原grid上overlap的点。复杂度会比较高，小哥也没啥异议。

多练练trie, 和图的题


1. 一個2-dim list of list，給座標，回傳下一步可走的選項。只能走上下左右，no diagonal moves
2. 給定一個座標，問if any other position can reach this position，DFS掃過一次，回傳ture/false
3. 給起點跟終點，能搜集到所有寶物的path當中最短的，output任一條。如果沒有任何一條path能搜集到所有寶物，則回傳[]。
Given a n by n grid which has # or * as elements. Please write a function to tell whether all the #s in the grid look like 0 or 1?This question can be condisered as a simplified version of handwritten digits recognition.if there exists a star which cannot reach the border, then it should be 0. Otheriwse 1.
给你一个schema，和一个json，让你判断这个json是不是match这个schema



behavior graph （面经题，考点trie）
3. 一个日志（格式: time | num），要求实时算出最近一小时内的和
例如：
time   num
10:00  10
10:20  20
10:30  30
11:00  60 (now) sum = 20 + 30 + 60 = 11
给定一个无序数组 找出最大子集 集合里的数相互之间的差不超过k
扩展问题 要求最优解 时间复杂度O(N)



密码解锁，给一个API用来判断是不是valid的密码，然后给一个array, [0-9,a-z,A-Z]，然后随意组合再判断。
Input看起来像这样： public List<Long> getAllValidPW(String[] nums, int length) 我用backtracking来做的，加了一个set去重，然后每次call API判断一下是不是valid的密码，如果是就加到list里。


Given a list of words, e.g, ["bandage", "banana", "anchor", "anchovy", "bass"], find the longest common prefix. 并不是这个prefix所有的word都要有，只要有2个word有的common prefix
最后解答是类似于n pointers 从0开始读 直到再也没有common prefix 为止。trie 算 common prefix 可以在每个node记录一个cnt看多少个词经过了这个node，然后cnt > 2的就是common prefix吧。。这题没必要trie吧，因为不是比prefix，而是完全match。hashmap做个space splited term到它位置的index，对于每个blacklist的词也split一下，verify它们index是连续的


给定字母矩阵，任意起点，找出最长路径并输出。路径定义为其字母相邻，且A与Z不相邻。

Json parser或者prettyprint a JSON file
给一个全是字母的矩阵，找最长路径，规则是允许移动到字母表相邻的字母上，比如c可以移动到b 假设矩阵有M行N列的话，我认为时间复杂度是O(M*N*4^s)(s是最长字符串的长度), 空间复杂度是O(MN)(我使用了visited数组)，


3. ad click conversion rate，

让找出每个ad的点击转化率，即点击了ad的user有多少最后购买了商品，比如ad1被ip1，ip2的用户点击过，ip1,ip2分别对应user id1, id2, 最终id1,id2都purchase了，所有ad1的conversion rate是1


Problems from Leetcode (1 year)	plus
- Text Justification
- Design Hit Counter
- Task Scheduler
- Interval List Intersections
- Partition to K Equal Sum Subsets


ML:
1. regularzation是啥；
loss function的定义是啥;
L1/L2正则区别是啥，哪个更适合sparse matrix；
当模型越来越复杂的时候的Bias-Variance Tradeoff;
SGD是啥;
auc是用在classification task上还是Regression ta
gradient vanishing, loss func,dropout，regularization，embedding
