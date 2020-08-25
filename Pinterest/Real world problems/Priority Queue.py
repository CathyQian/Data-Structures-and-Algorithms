"""
Priority Queue

输⼊入是⼀堆pin和一个col数，将这些pin放⼊入col个list中返回，填充 ⻚页⾯面，
规则是每次填⼀一个pin的时候找当前像素数最少的那⼀一列列填
"""
import heapq
class Solution:     
    def arrange_pins(self, pins, n_col):    
        position = []   
        for i in range(n_col):         
            heapq.heappush(position, (0, 'Col_{}'.format(i), [])) # initialize each column, order depends on ranking rule    
            for pin, name in pins:         
                height, name_col, lst = heapq.heappop(position)         
                heapq.heappush(position, (height+pin, name_col, lst+[name]))    
        return position # what to output??
Pinterest主⻚页上有N个column，给⼀一个set of pins，pins有score和 length，每次把score最⾼高的pin贴到最短的
column上，return List<List<pins>> 表示每个column⾥里里的pins。⽤用priority queue做，写完之 后follow up：
⽤用户的⼿手机屏幕只有M⻓长，如果屏幕的顶点距离主⻚页顶点距离 为K，求出能显示出的pins。思路路是⽤用数组存⼀一个
column中每个pins到顶点 的距离，然后找到最上⾯面的和最下⾯面的，再求中间的。⼩小优
化是⽤用binary search找start point 和 end point。写了了⼀一半，时间不不够了了，问了了点问题就 结束了了