"""
Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate
to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []

 

Constraints:

    0 <= num.length <= 10
    num only contain digits.


"""

# https://www.youtube.com/watch?v=v05R1OIIg08
# dfs(expr, pos, prev, curr)
# expr: current scanned string 
# pos: starting index of the next number
# prev: the last element in expr
# curr: value of expr 

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        self.dfs(num, target, 0, '', 0, 0)
        return self.ans
    
    def dfs(self, num, target, start, exp, prev, curr):
        if start == len(num) and curr == target:
            self.ans.append(exp)
            return
        
        for i in range(start + 1, len(num)+1):
            t = num[start:i]
            
            # edge case 1
            if t[0] == '0' and len(t) > 1:
                break
            
            # edge case 2 --- this is the first element
            elif start == 0:
                self.dfs(num, target, i, t, int(t), int(t))
            
            else:
                self.dfs(num, target, i, exp + '+' + t, int(t), curr + int(t))
                self.dfs(num, target, i, exp + '-' + t, -int(t), curr - int(t))
                self.dfs(num, target, i, exp + '*' + t, prev * int(t), curr - prev + prev * int(t))
                
        
