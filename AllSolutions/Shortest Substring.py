"""
给一个字符串， 给一个字典，字典里是不重复的单个字母。问这个字符串中最短的substring，条件是包含
所有字典中的字母。 应该是leetcode的原题了了。 做法是two pointer + hashmap
"""

from collections import defaultdict 
def find_min_window(S, T):     
    left, right = 0, 0     
    c = defaultdict(int)    
    for ch in T: # scan the dictionary, hashmap allows for O(1) search     
        c[ch] += 1     
    min_str = ''         
    while right <= len(S):  # search the string        
        if all(map(lambda x: True if x <= 0 else False, c.values())): # all elements in dic have been visited           
            if not min_str or right-left <= len(min_str): # if the first str or shorter than existing str
                min_str = S[left:right]             
            if S[left] in c:           # if found string is longer than existing str, left += 1, then keep searching      
                c[S[left]] += 1             
            left += 1         
        else:             
            if right == len(S): 
                break             
            if S[right] in c:                 
                c[S[right]] -= 1             
            right += 1     
    return min_str
