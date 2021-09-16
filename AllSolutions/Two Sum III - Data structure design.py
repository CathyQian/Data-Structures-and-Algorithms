"""
Two Sum III - Data structure design
Easy

Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

    TwoSum() Initializes the TwoSum object, with an empty array initially.
    void add(int number) Adds number to the data structure.
    boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false

 

Constraints:

    -105 <= number <= 105
    -231 <= value <= 231 - 1
    At most 104 calls will be made to add and find.



"""

# which one is better depends on which function is used more frequent --- add or find
class TwoSum:

    def __init__(self):
        self.ctr = {}

    def add(self, number): #O(1)
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value): # O(n2)
        ctr = self.ctr
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False


# slower solution
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.sums = set()
        

    def add(self, number: int) -> None: # O(len(self.elements))  --- too big
        """
        Add the number to an internal data structure..
        """
        if len(self.elements) == 0:
            self.elements.append(number)
        else:
            for ele in self.elements:
                self.sums.add(ele + number)
            self.elements.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value in self.sums:
            return True
        else:
            return False
        

