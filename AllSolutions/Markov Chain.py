"""
然后就是设计⼀一个组成语句句的API(⻢马尔科夫链) 例例⼦子: "one two three four" "two three four" "two five
four" 那以"two" 开头的概率是2/3 "one" 开头的概率是1/3 那我们先选开头的这个词， 如果选到了了two， 那在two这个
阶段上再往后看，three跟着two的概率是2/3 five跟着two的概率是1/3 如果选到了了three，..
按照这样的模式直到结束。
"""

# separate the first word and other word; if words can't be found in the existing dictionary, break

import random 
import collections

class Solution:
    def sentenceMarkovGenerator(self, sentence_lst, N):     
        # begin word and next word are treated differently
        begin = collections.defaultdict(int)     
        nextword = collections.defaultdict(dict)   
        prev = ''     
        for sentence in sentence_lst:         
            words = sentence.split(' ') 
            for i in range(len(words)):             
                if i == 0:                                  
                    begin[words[i]] += 1                 
                    prev = words[i]             
                else:                 
                    if prev in nextword:                                             
                        nextword[prev][words[i]] += 1 
                    else:                     
                        nextword[prev] = {}                     
                        nextword[prev][words[i]] = 1                 
                    prev = words[i] 
        result = []     
        for i in range(N):         
            if i == 0: # first word      
                result += [self.randomWord(begin)]         
            elif result[-1] in nextword: # following words             
                result += [self.randomWord(nextword[result[-1]])]         
            else:  # begin word doesn't exit in nextword, can't predict next. This happens if the given sentences has too many one word sentence         
                break     
        return result

    def randomWord(self, wordict):     
        total = 0     
        for key, value in wordict.items():         
            total += value 
        randindex = random.randint(1, total) # [0, total] or [1, total]
        for key, value in wordict.items():  # output is random       
            randindex -= value         
            if randindex <= 0:             
                return key 