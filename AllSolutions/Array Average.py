给⼀一个N⻓长度的unsorted array，array中的每个数都是8bit的正数 integer，以及M个query，
每个query⾥里里有个start index和end index， 要求 出原array中每个start point到end point
的平均数。先说了了⼀一下brute force的 解法，时间O(N*M)，⼩小哥问能不不能优化，给出了了⽤
用累加array的解法，时间 O(N+M)，⼩小哥表示ok。follow up，如果找中数怎么找。这⾥里里有点
卡住，⼩小 哥提示每个数都是8bit的这个条件还没⽤用，想出了了bucket sort的解法，说完 时间
不不够了了，没有写代码