""" https://leetcode.com/problems/plus-one/description/

2 solutions. First is recursive. Second is iterative. Iterative is usually faster
than recursive
"""


"""
Solution 1:

Recursive.

The idea is that we start at the end of the list and recursively check at each
index what the value of the digit is. If the value is 9 then we know when we add
plus 1 to it that value needs to turn into a 0 and then that carry over value will affect
the previous (the larger place value) digit so that is the only situation where
we need to recursively call the function again to check the previous digit.

The base case is when the index goes below the value 0 since that means every digit
was 9 therefore we need to insert a 1 at the 0'th index i.e. [9,9,9] -> [1,0,0,0]
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.helper(digits, len(digits)-1) 
        return digits
    
    def helper(self, digits, index):
        if index < 0:
            digits.insert(0, 1)
        elif digits[index] == 9:
            digits[index] = 0
            self.helper(digits, index - 1)
        else:
            digits[index] += 1


"""
Solution 2

Iterative.

Iterative backwards starting at the final index. Keep setting each value at the index
to the value 0 as long as we are within the bounds of the list and that the current
value is 9. When the the while loop breaks we know it broke due to one of the 2
while conditions so we check for both conditions and proceed accordingly.

If the while loop condition broke due to the index being below 0 then we know that
all of the values in the list got turned into 0's so we just prepend a 0 to the list

Otherwise, the while loop exited due to the value not being a 9 so all we do is increase
the value at that current index by 1
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        while index >= 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1
        if index < 0:
            digits.insert(0, 1)
        else:
            digits[index] += 1
        return digits
        