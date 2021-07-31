"""
1861. Rotating the Box
Medium

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.


Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

 

Constraints:

    m == box.length
    n == box[i].length
    1 <= m, n <= 500
    box[i][j] is either '#', '*', or '.'.

"""

# fast slution using two pointers
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if not box or len(box) == 0:
            return []
        m, n = len(box), len(box[0])
        stone, obstacle, empty = '#', '*', '.'
        for row in box:
            move_position = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == obstacle:
                    move_position = j - 1
                elif row[j] == stone:
                    if  j != move_position:
                        row[j], row[move_position] = row[move_position], row[j]
                    move_position -= 1
                    
        # 90 degree rotation     
        rotate = []
        for i in range(n):
            rotate.append([])
            for j in range(m - 1, -1, -1):
                rotate[i].append(box[j][i])        
        
        return rotate
    
# my initial solution --- much slower due to duplicated operation
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # rotate first
        if not box or not box[0]:
            return None
        m, n = len(box), len(box[0])
        new = [['.']*m for _ in range(n)]
        
        for i in range(m//2):
            for j in range(n):
                box[m-1-i][j], box[i][j] = box[i][j], box[m-1-i][j]
        
        for i in range(m):
            for j in range(n):
                new[j][i] = box[i][j]
                
        # relocate
        for i in range(m):
            for j in range(n)[::-1]:
                if new[j][i] == '#':
                    self.dropStone(new, j, i)
        return new
    
    def dropStone(self, matrix, row, col):
        pos = row
        while pos+1 < len(matrix) and matrix[pos+1][col] == '.':
            pos += 1
        if pos != row:
            matrix[row][col] = '.'
            matrix[pos][col] = '#'