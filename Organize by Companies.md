## A2

1. [Two Sum](AllSolutions/Two%20Sum.py)
2. [Longest Palindromic Substring](AllSolutions/Longest%20Palindromic%20Substring.py)
3. [3Sum](AllSolutions/3Sum.py) (**)
4. [Merge Two Sorted Lists](AllSolutions/Merge%20Two%20Sorted%20Lists.py)
5. [Merge k Sorted Lists](AllSolutions/Merge%20k%20Sorted%20Lists.py)
6. [Trapping Rain Water](AllSolutions/Trapping%20Rain%20Water.py) (**)
7. [Group Anagrams](AllSolutions/Group%20Anagrams.py)
8. [Merge Intervals](AllSolutions/Merge%20Intervals.py)
9. [Search a 2D Matrix](AllSolutions/Search%20a%202D%20Matrix.py)
10. [Word Search](AllSolutions/Word%20Search.py)
11. [Interleaving String](AllSolutions/Interleaving%20String.py) (**)
12. [Best Time to Buy and Sell Stock](AllSolutions/Best%20Time%20to%20Buy%20and%20Sell%20Stock.py)
13. [Copy List with Random Pointer](AllSolutions/Copy%20List%20with%20Random%20Pointer.py) (**)
14. [Word Break](AllSolutions/Word%20Break.py)
15. [Word Break II](AllSolutions/Word%20Break%20II.py) (**)
16. [LRU Cache](AllSolutions/LRU%20Cache.py) (**)
17. [Number of Islands](AllSolutions/Number%20of%20Islands.py)
18. [Course Schedule II](AllSolutions/Course%20Schedule%20II.py)
19. [Add and Search Word - Data structure design](AllSolutions/Add%20and%20Search%20Word%20-%20Data%20structure%20design.py) (**)
20. [Basic Calculator II](AllSolutions/Basic%20Calculator%20II.py) (**)
21. [Search a 2D Matrix II](AllSolutions/Search%20a%202D%20Matrix%20II.py)
22. [Flood Fill](AllSolutions/Flood%20Fill.py)
23. [Most Common Word](AllSolutions/Most%20Common%20Word.py)
24. [Reorder Data in Log Files](AllSolutions/Reorder%20Data%20in%20Log%20Files.py)

## P(Graph)

1. [24 Game](AllSolutions/24%20Game.py)(itertools.product(iterator, repeat=k))
2. [Alien Dictionary](AllSolutions/Alien%20Dictionary.py) (edge case, esp duplicated entries)
3. [Array Average](AllSolutions/Array%20Average.py)
4. [Binary Tree Longest Consecutive Sequence](AllSolutions/Binary%20Tree%20Longest%20Consecutive%20Sequence.py)
5. [Binary Tree Zigzag Level Order Traversal](AllSolutions/Binary%20Tree%20Zigzag%20Level%20Order%20Traversal.py)
6. [Can I Win](AllSolutions/Can%20I%20Win.py)(dfs+memo)
7. [Convert Sorted List to Binary Search Tree](AllSolutions/Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree.py) (if linked list, can' assign slow=None, need a pre)
8. [Course Schedule II](AllSolutions/Course%20Schedule%20II.py)
9. [Design Hit Counter](AllSolutions/Design%20Hit%20Counter.py) (ordered dict + counter)
10. [Diameter of Binary Tree](AllSolutions/Diameter%20of%20Binary%20Tree.py) (pay attention to initial and return val, count node then diameter)
11. [Employee Free Time](AllSolutions/Employee%20Free%20Time.py)
12. [Factor Combinations](AllSolutions/Factor%20Combinations.py)
13. [Find Duplicate File in System](AllSolutions/Find%20Duplicate%20File%20in%20System.py)
14. [Find Peak Element](AllSolutions/Find%20Peak%20Element.py) (binary search, compare arr[mid] and arr[mid+1])
15. [Graph Valid Tree](AllSolutions/Graph%20Valid%20Tree.py)(undirectional: no cycle + all connected)
16. [Implement min Heap](AllSolutions/Implement%20min%20Heap.py) (percolation up and percolation down, note parent and child index)
17. [Insert Delete GetRandom O(1)](AllSolutions/Insert%20Delete%20GetRandom%20O(1).py)(cannot use set pop, use dic + list)
18. [Interval List Intersections](AllSolutions/Interval%20List%20Intersections.py)
19. [Is Subsequence](AllSolutions/Is%20Subsequence.py)
20. [Island Perimeter](AllSolutions/Island%20Perimeter.py)
21. [Jump Game III](AllSolutions/Jump%20Game%20III.py)
22. [LFU Cache](AllSolutions/LFU%20Cache.py)(**pretty hard, need to memorize details)
23. [Log System to Graph](AllSolutions/Log%20System%20to%20Graph.py) (the answer has some problems)
24. [Longest Common Prefix](AllSolutions/Longest%20Common%20Prefix.py) (edge cases, for loop exit condition)
25. [Longest Common Subsequence](AllSolutions/Longest%20Common%20Subsequence.py)
26. [Longest Happy Prefix](AllSolutions/Longest%20Happy%20Prefix.py)
27. [Longest Increasing Path in a Matrix](AllSolutions/Longest%20Increasing%20Path%20in%20a%20Matrix.py) (dfs + memo, no default val for all)
28. [Longest Valid Parentheses](AllSolutions/Longest%20Valid%20Parentheses.py)(different from longest palindrom subsequence using dfs where the characters can be deleted, this one is looking for substring, use stack instead)
29. [Markov Chain](AllSolutions/Markov%20Chain.py)
30. [Maximum Length of Repeated Subarray](AllSolutions/Maximum%20Length%20of%20Repeated%20Subarray.py) (return max, not dp[m][n])
31. [Meeting Rooms II](AllSolutions/Meeting%20Rooms%20II.py)
32. [Meeting Rooms](AllSolutions/Meeting%20Rooms.py)
33. [Minimum Window Substring](AllSolutions/Minimum%20Window%20Substring.py) (don't consider order)
34. [MinStack](AllSolutions/MinStack.py)
35. [Next Permutation](AllSolutions/Next%20Permutation.py)
36. [Number of Closed Islands](AllSolutions/Number%20of%20Closed%20Islands.py)
37. [Number of Distinct Islands](AllSolutions/Number%20of%20Distinct%20Islands.py)(**need to record all movements, including 0s)
38. [Number of Islands II](AllSolutions/Number%20of%20Islands%20II.py)
39. [Number of Islands](AllSolutions/Number%20of%20Islands.py)
40. [Paint House II](AllSolutions/Paint%20House%20II.py)
41. [Paint House III](AllSolutions/Paint%20House%20III.py)
42. [Paint House](AllSolutions/Paint%20House.py)
43. [Partition Equal Subset Sum](AllSolutions/Partition%20Equal%20Subset%20Sum.py)(**time exceed limit if using Partition to K Equal Sum Subsets template, use a very different method)
44. [Partition to K Equal Sum Subsets](AllSolutions/Partition%20to%20K%20Equal%20Sum%20Subsets.py)(**time exceed limit, need to sort nums in descending order, pay attention to for loop start position)
45. [Path Sum III](AllSolutions/Path%20Sum%20III.py)(**easy to make mistake recursion)
46. [Priority Queue](AllSolutions/Priority%20Queue.py)
47. [Random Pick with Blacklist](AllSolutions/Random%20Pick%20with%20Blacklist.py)(**optimized solution, not brutal force)
48. [Random Pick with Weight](AllSolutions/Random%20Pick%20with%20Weight.py)
49. [Read N Characters Given Read4 II - Call multiple times](AllSolutions/Read%20N%20Characters%20Given%20Read4%20II%20-%20Call%20multiple%20times.py)
50. [Read N Characters Given Read4](AllSolutions/Read%20N%20Characters%20Given%20Read4.py)
51. [Shortest Path between Two nodes in the tree](AllSolutions/Shortest%20Path%20between%20Two%20nodes%20in%20the%20tree.py)
52. [Shortest Path](AllSolutions/Shortest%20Path%20between%20Two%20nodes%20in%20the%20tree.py)
53. [Shortest Substring](AllSolutions/Shortest%20Substring.py)
54. [Subdomain Visit Count](AllSolutions/Subdomain%20Visit%20Count.py)
55. [Task Scheduler](AllSolutions/Task%20Scheduler.py)
56. [Text Justification](AllSolutions/Text%20Justification.py)
57. [Word Ladder II](AllSolutions/Word%20Ladder%20II.py) (be careful with initial layer definition and layer update)
58. [Word Ladder](AllSolutions/Word%20Ladder.py)
59. [Word Search II](AllSolutions/Word%20Search%20II.py) (**)
60. [Word Search](AllSolutions/Word%20Search.py)
61. [Minimum Window Subsequence](AllSolutions/Minimum%20Window%20Subsequence.py) (compare with 33, consider order, dp)

## M

1. [Add Two Numbers II](AllSolutions/Add%20Two%20Numbers%20II.py)
2. [Add Two Numbers](AllSolutions/Add%20Two%20Numbers.py)
3. [Binary Tree Inorder Traversal](AllSolutions/Binary%20Tree%20Inorder%20Traversal.py)
4. [Clone Graph](AllSolutions/Clone%20Graph.py) (**)
5. [Copy List with Random Pointer](AllSolutions/Copy%20List%20with%20Random%20Pointer.py)
6. [Excel Sheet Column Number](AllSolutions/Excel%20Sheet%20Column%20Number.py)
7. [Find Minimum in Rotated Sorted Array I, II](AllSolutions/Find%20Minimum%20in%20Rotated%20Sorted%20Array%20I%2C%20II.py)
8. [Find the Celebrity](AllSolutions/Find%20the%20Celebrity.py)
9. [Implement Trie (Prefix Tree)](AllSolutions/Implement%20Trie%20(Prefix%20Tree).py) (ask what does startwith mean)
10. [Integer to English Words](AllSolutions/Integer%20to%20English%20Words.py)
11. [Intersection of Two Linked Lists](AllSolutions/Intersection%20of%20Two%20Linked%20Lists.py)
12. [Letter Combinations of a Phone Number](AllSolutions/Letter%20Combinations%20of%20a%20Phone%20Number.py)
13. [Linked List Cycle](AllSolutions/Linked%20List%20Cycle.py)
14. [Longest Increasing Subsequence](AllSolutions/Longest%20Increasing%20Subsequence.py)
15. [Lowest Common Ancestor of a Binary Search Tree](AllSolutions/Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.py)
16. [Lowest Common Ancestor of a Binary Tree](AllSolutions/Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.py)
17. [LRU Cache](AllSolutions/LRU%20Cache.py)
18. [Maximum Subarray](AllSolutions/Maximum%20subarray.py)
19. [Median of Two Sorted Arrays](AllSolutions/Median%20of%20Two%20Sorted%20Arrays.py)
20. [Merge k Sorted Lists](AllSolutions/Merge%20k%20Sorted%20Lists.py)
21. [Merge Sorted Array](AllSolutions/Merge%20Sorted%20Array.py)
22. [Populating Next Right Pointers in Each Node II](AllSolutions/Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II.py)
23. [Populating Next Right Pointers in Each Node](AllSolutions/Populating%20Next%20Right%20Pointers%20in%20Each%20Node.py)
24. [Regular Expression Matching](AllSolutions/Regular%20Expression%20Matching.py)
25. [Remove Duplicates from Sorted Array](AllSolutions/Remove%20Duplicates%20from%20Sorted%20Array.py)
26. [Reverse Linked List](AllSolutions/Reverse%20Linked%20List.py)
27. [Roman to Integer](AllSolutions/Roman%20to%20Integer.py)
28. [Rotate Image](AllSolutions/Rotate%20Image.py)
29. [Search in Rotated Sorted Array](AllSolutions/Search%20in%20Rotated%20Sorted%20Array.py) (II*)
30. [Serialize and Deserialize BST](AllSolutions/Serialize%20and%20Deserialize%20BST.py)
31. [Single Number](AllSolutions/Single%20Number.py)
32. [Sort Colors](AllSolutions/Sort%20Colors.py)
33. [Spiral Matrix](AllSolutions/Spiral%20Matrix.py)
34. [String to Integer (atoi)](AllSolutions/String%20to%20Integer%20(atoi).py)
35. [The Skyline Problem](AllSolutions/The%20Skyline%20Problem.py)
36. [Wildcard Matching](AllSolutions/Wildcard%20Matching.py)
37. [Word Search II](AllSolutions/Word%20Search%20II.py)


F (Tree & Graph) # focus on new first
1. [K Closest Points to Origin](AllSolutions/K%20Closest%20Points%20to%20Origin.py) (heap)
2. [Clone Graph](AllSolutions/Clone%20Graph.py)
3. [Merge Intervals](AllSolutions/Merge%20Intervals.py)
4. [Validate Binary Search Tree](AllSolutions/Validate%20Binary%20Search%20Tree.py)
5. Verifying an Alien Dictionary (easy, new)
6. [Binary Tree Maximum Path Sum](AllSolutions/Binary%20Tree%20Maximum%20Path%20Sum.py)
7. [Binary Tree Vertical Order Traversal](AllSolutions/Binary%20Tree%20Vertical%20Order%20Traversal.py) (**dict + bfs (not dfs))   
8. [Convert Binary Search Tree to Sorted Doubly Linked List](AllSolutions/Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List.py)(**iterative tree traversal)
9. [Continuous Subarray Sum](AllSolutions/Continuous%20Subarray%20Sum.py) (** k==0, mod[0] = [-1])
10. [Subarray Sum Equals K](AllSolutions/Subarray%20Sum%20Equals%20K.py) (**, cursum + dict)
11. [Task Scheduler](AllSolutions/Task%20Scheduler.py)
12. [Valid Palindrome II](AllSolutions/Valid%20Palindrome%20II.py)
13. [Lowest Common Ancestor of Deepest Leaves](AllSolutions/Lowest%20Common%20Ancestor%20of%20Deepest%20Leaves.py)(**)
14. [Divide Two Integers](AllSolutions/Divide%20Two%20Integers.py) (bit operation)
15. [Next Permutation](AllSolutions/Next%20Permutation.py)
16. [Find First and Last Position of Element in Sorted Array](AllSolutions/Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.py) (review binary search 4 template)
17. [Add Binary](AllSolutions/Add%20Binary.py)
18. [Subsets](AllSolutions/Subsets.py) (recursion or dfs)
19. [Kth Largest Element in an Array](AllSolutions/Kth%20Largest%20Element%20in%20an%20Array.py)(**quick sort)
20. Product of Array Except Self (O(N))
21. Integer to English Words
22. [First Bad Version](AllSolutions/First%20Bad%20Version.py) (binary search)
23. Serialize and Deserialize Binary Tree
24. [Intersection of Two Arrays](AllSolutions/Intersection%20of%20Two%20Arrays.py)
25. [Merge Sorted Array](AllSolutions/Merge%20Sorted%20Array.py)
26. Valid Palindrome
27. Copy List with Random Pointer (medium **)
28. Course Schedule
29. Remove Invalid Parentheses (** bfs, pay attention to isvalid check -- use count is enough)
30. Longest Increasing Path in a Matrix (** dfs + memo!!)
31. The Maze (**dfs + seen to avoid repeated dfs)
32. Random Pick with Weight
33. Container with Most Water (medium, new)
34. Merge Two Sorted Lists (easy, new)
35. Longest Valid Parenthesis (**)
36. Search in Rotated Sorted Array (**always narrow down scope between mid, start and end)
37. Trapping rain water I (hard, **), Trapping rain water II (**)
38. Permutations II (medium, **)
39. Reorder List (medium, new)
40. Read N Characters Given Read4
41. Longest Substring with At Most Two Distinct Characters (medium, new)
42. One Edit Distance (medium, corner cases)
43. Binary Tree Right Side View
44. Sliding Window Maximum (hard, O(N, compare with Sliding Window Medium))
45. Meeting Rooms II
46. Inorder Successor in BST (medium, new)
47. Walls and Gates(** dfs or bfs)
48. Range Sum Query 2D - Immutable (medium, new)
49. Nested List Weight Sum (easy, new)
50. Longest Substring with At Most K Distinct Characters (hard, new)
51. Moving Average from Data Stream (easy, new)
52. Intersection of Two Arrays (easy, new)
53. Minesweeper (medium, new)
54. Exclusive Time of Functions (medium, new)
56. [Accounts Merge (medium, ** union find)](AllSolutions/Accounts%20Merge.py)

to-review
57. All Nodes Distance K in Binary Tree (medium, new)
58. Add Two Numbers (medium, new)
59. String to Integer (atoi) (medium, new)
60. Remove Nth Node From End of List (medium, new)
61. Find First and Last Position of Element in Sorted Array (medium, new)
62. Wildcard Matching (hard **)
63. Permutation
64. Rotate List (medium, new)
65. Valid Number (hard**)
66. Sqrt(x)  
67. Search a 2D Matrix
68. Word Search
69. Binary Tree Inorder Traversal   
70. Shortest Distance from All Buildings (hard, bfs)
Recent 6 months
- [Minimum Remove To Make Valid Parentheses](AllSolutions/Minimum%20Remove%20to%20Make%20Valid%20Parentheses.py)(not bfs**, count instead; ()() is also valid)(****)
- [Leftmost Column With At Least A One]() (**)
- Product Array Except Self
- [Add Strings](AllSolutions/Add%20Strings.py)(divmod)
- [Design Add and Search word data structure](AllSolutions/Design%20Add%20and%20Search%20Words%20Data%20Structure.py) (trie, add a helper function to allow for recusrion**)
- [Find All Anagram In a String](AllSolutions/Find%20All%20Anagrams%20in%20a%20String.py)


T
- Minimum Genetic Mutation
- Validate IP address
- Alien Dictionary
- friend cycle
- text justification

- LRU Cache
- [One edit distance](AllSolutions/One%20Edit%20Distance.py) 

- Design log storage system
- flatten nested list iterator
- reaching points
- paint house


- best meeting point
- tree node


- Investments in 2016
- palindromic substrings
- valid parenthesis
- masking personal information

- range sum query-mutable
- max points on a line
- rectangles area
- minimum number of steps to make two strings anagram
- permutation sequence
- integer to Roman
- happy number
- Number of Connected Components in an Undirected Graph (union find)
- Minimum increment to make array unique
- minimum number of taps to open to water a garden
- the skyline problem (*)
- flatten 2D vector

- Multiply strings
- single element in a sorted array

- reorganizing string
- time based key-value store
- binary tree pruning
- k-diff pairs in an array
- max stack
- robot bounded in cycle
- next greater element i

- binary gap
- design skiplist

recent 6 month
- Tweet Count Per Frequency (medium**)
- Insert Delete GetRandom O(1)
- Design HashMap (easy, new)
- Insert Interval (medium, **binary search)
- Find Median from Data Stream (medium, minheap + maxheap)
- Frog Jump (hard, **)
- Range Sum Query 2D - Immutable (medium, **)

# A1
- [Peaking Iterator](AllSolutions/Peeking%20Interator.py) (use cache)
- Moving Average from Data Steam (what if long array?)
- [Median of Two Sorted Arrays (**, O(log(m+n)))](AllSolutions/Median%20of%20Two%20Sorted%20Arrays.py)
- [Longest Substring Without Repeating Characters](AllSolutions/Longest%20Substring%20Without%20Repeating%20Characters.py) (**)
- [Group Anagrams](AllSolutions/Group%20Anagrams.py) (can't sort string directly, key = ''.join(sorted(s)))
- [Reverse Bits](AllSolutions/Reverse%20Bits.py) (bit operation, >>, <<, ^)
- [Course Schedule](AllSolutions/Course%20Schedule.py)(dfs or bfs, detect cycle in graph)
- [Course Schedule II](AllSolutions/Course%20Schedule%20II.py)(dfs or bfs, detect cycle in graph)
- [Product of Array Except Self](AllSolutions/Product%20of%20Array%20Except%20Self.py)(O(1) space and O(n)time)
- [Perfect Squares](AllSolutions/Perfect%20Squares.py)(BFS)
- [Set Matrix Zeros](AllSolutions/Set%20Matrix%20Zeroes.py) (O(m+n) space, or O(1) space)
- [Find Median from Data Stream](AllSolutions/Find%20Median%20from%20Data%20Stream.py) (hard, one minheap + one max heap)
- [Insert Delete GetRandom O(1)](AllSolutions/Insert%20Delete%20GetRandom%20O(1).py)(**, random.choice)
- [Word Break](AllSolutions/Word%20Break.py)(recursion/dfs with memo)
- [Word Break II](AllSolutions/Word%20Break%20II.py)(recursion/dfs with memo)
- [LRU Cache](AllSolutions/LRU%20Cache.py)(**)
- [LFU Cache](AllSolutions/LFU%20Cache.py)(**)
- [Find the next leaf](AllSolutions/Find%20the%20next%20leaf.py)[link](https://leetcode.com/discuss/interview-question/algorithms/124645/return-the-next-leaf-node-in-tree) (in-order tree traversal)
- [3 Sum](AllSolutions/3Sum.py)
- [N Queens](AllSolutions/N-Queens.py) (**dfs + backtracking)
- [Validate Binary Search Tree](AllSolutions/Validate%20Binary%20Search%20Tree.py)
- [Implement k-means Clustering](AllSolutions/Implement%20k-means%20clustering%20algorithm.py)


## S
- [Pancake Sorting](AllSolutions/Pancake%20Sorting.py)
- [Edit Distance](AllSolutions/Edit%20Distance.py)
- [Palindrome Pairs](AllSolutions/Palindrome%20Pairs.py) (**)
- [Available Captures for Rook](AllSolutions/Available%20Captures%20for%20Rook.py)
- [Encode and Decode Strings](AllSolutions/Encode%20and%20Decode%20Strings.py)
- [Integer to English Words](AllSolutions/Integer%20to%20English%20Words.py)
- [Bus Routes](AllSolutions/Bus%20Routes.py)
- [Number of Transactions per Visit](sql)
- [Longest Absolute File Path](AllSolutions/Longest%20Absolute%20File%20Path.py)
- [Text Justification](AllSolutions/Text%20Justification.py)
- [Decode Ways](AllSolutions/Decode%20Ways.py)
- [Game of Life](AllSolutions/Game%20of%20Life.py)
- [Expression Add Operators](AllSolutions/Expression%20Add%20Operators.py)
- [Add Strings](AllSolutions/Add%20Strings.py)
- [Compare Version Numbers](AllSolutions/Compare%20Version%20Numbers.py)
- [Design Search Autocomplete System](AllSolutions/Design%20Search%20Autocomplete%20System.py)
- [Minesweeper](AllSolutions/Minesweeper.py)
- [Multiply Strings](AllSolutions/Multiply%20Strings.py)
- [Reconstruct Itinerary](AllSolutions/Reconstruct%20Itinerary.py)
- [Word Search II](AllSolutions/Word%20Search%20II.py)
- [Letter Combinations of a Phone Number](AllSolutions/Letter%20Combinations%20of%20a%20Phone%20Number.py)
- [Rotating the Box](Rotating%20the%20Box.py)
- [Merge Intervals](AllSolutions/Merge%20Intervals.py)
- [Number of Islands](AllSolutions/Number%20of%20Islands.py)
- [Serialize and Deserialize Binary Tree](AllSolutions/Serialize%20and%20Deserialize%20Binary%20Tree.py)
- [Combination Sum](AllSolutions/Combination%20Sum.py)
- [Word Break](AllSolutions/Word%20Break.py)
- [Two Sum](2Sum.py)
- [Best Time to Buy and Sell Stock II](AllSolutions/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.py)
- [Squirrel Simulation](AllSolutions/Squirrel%20Simulation.py)
- [Falling Squares](AllSolutions/Falling%20Squares.py)
- [Count Nice Pairs in an Array](AllSolutions/Count%20Nice%20Pairs%20in%20an%20Array.py)


## L
- [Shortest Word Distance II](AllSolutions/Shortest%20Word%20Distance%20II.py)
- [Nested List Weight Sum II](AllSolutions/Nested%20List%20Weight%20Sum%20II.py)

- [Minimum One Bit Operations to Make Integers Zero]
- [Max Stack](AllSolutions/Max%20Stack.py)

- [All O`one Data Structure]
- [Paint House](AllSolutions/Paint%20House.py)
- [Closest Binary Search Tree Value II]
- [Find Leaves of Binary Tree](AllSolutions/Find%20Leaves%20of%20Binary%20Tree.py)
- [Design Bounded Blocking Queue]
- [Insert Delete GetRandom O(1)](AllSolutions/Insert%20Delete%20GetRandom%20O(1).py)
- [Max Points on a Line](AllSolutions/Max%20Points%20on%20a%20Line.py) (hard)
- [Can Place Flowers](AllSolutions/Can%20Place%20Flowers.py)
- [Serialize and Deserialize Binary Tree](AllSolutions/Serialize%20and%20Deserialize%20Binary%20Tree.py)
- [Count Different Palindromic Subsequences]
- [Design HashMap]
- [Second Minimum Node In a Binary Tree](AllSolutions/Second%20Minimum%20Node%20In%20a%20Binary%20Tree.py)
- [Bomb Enemy](AllSolutions/Bomb%20Enemy.py)

- [Factor Combinations**](AllSolutions/Factor%20Combinations.py)
- [Partition to K Equal Sum Subsets](AllSolutions/Partition%20to%20K%20Equal%20Sum%20Subsets.py)
- [Binary Tree Upside Down](AllSolutions/Binary%20Tree%20Upside%20Down.py)
- [Lowest Common Ancestor of a Binary Tree III](AllSolutions/Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III.py)(find common ancestor template)
- [Find K Pairs with Smallest Sums](AllSolutions/Find%20K%20Pairs%20with%20Smallest%20Sums.py) (O(k))
- [Maximum Product Subarray](AllSolutions/Maximum%20Product%20Subarray.py) (tricky)
- [Maximum Subarray](AllSolutions/Maximum%20subarray.py) (Three methods)
- [Longest Palindromic Subsequence](AllSolutions/Longest%20Palindromic%20Subsequence.py) (DP, pay attention to dp initialization)
- [Search in Rotated Sorted Array](AllSolutions/Search%20in%20Rotated%20Sorted%20Array.py) (4 binary search template)
- [Binary Tree Level Order Traversal](AllSolutions/Binary%20Tree%20Level%20Order%20Traversal.py) (return val not node)
- [Valid Triangle Number](AllSolutions/Valid%20Triangle%20Number.py) (O(n2))
- [Pow(x, n)](AllSolutions/Pow(x%2C%20n).py) (note that x can be negative)
- [Longest Substring with At Most Two Distinct Characters](AllSolutions/Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py)
- [Longest Substring with At Most K Distinct Characters](AllSolutions/Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py)
- [Rotate List](AllSolutions/Rotate%20List.py) (Typical Linked List problem)
- [Delete Node in a BST](AllSolutions/Delete%20Node%20in%20a%20BST.py) (Delete node: can't do it via node = None **)
- [Subarray Sum Equals K](AllSolutions/Subarray%20Sum%20Equals%20K.py) (use dictionary)