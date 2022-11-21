"""
Priority Queue

输入是⼀堆pin和一个col数，将这些pin放⼊入col个list中返回，填充页面，
规则是每次填一个pin的时候找当前像素数最少的那⼀列填
"""
# use heap, each element is (height, col_name, list of pins in that column), order by height, if indistinguishable,
# then order by col_name

import heapq
class Pin:
    def __init__(self, height=None, name=None, score=None):
        self.height = height
        self.name = name
        self.score = score
        
class Solution:     
    def arrange_pins(self, pins, n_col):
        """
        pins: list of Pins
        """
        pins.sort(key=lambda x: x[2], reverse=True)
        contents = []   
        for i in range(n_col):         
            heapq.heappush(contents, (0, 'Col_{}'.format(i), [])) # initialize each column, order depends on ranking rule    
        for pin in pins:         
            col_height, col_name, pin_lst = heapq.heappop(contents) # pop out shortest column        
            heapq.heappush(contents, (height+pin.height, name_col, lst+[pin.name]))    
        return contents
    
Pinterest主⻚页上有N个column，给⼀一个set of pins，pins有score和 length，每次把score最⾼高的pin贴到最短的
column上，return List<List<pins>> 表示每个column⾥里里的pins。⽤用priority queue做，写完之 后follow up：
⽤用户的⼿手机屏幕只有M⻓长，如果屏幕的顶点距离主⻚页顶点距离 为K，求出能显示出的pins。思路路是⽤用数组存⼀一个
column中每个pins到顶点 的距离，然后找到最上⾯面的和最下⾯面的，再求中间的。⼩小优
化是⽤用binary search找start point 和 end point。写了了⼀一半，时间不不够了了，问了了点问题就 结束了了

# follow-up
