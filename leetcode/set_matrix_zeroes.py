""" https://leetcode.com/problems/set-matrix-zeroes/description/ 

O(m*n) Time Complexity and O(m + n) Space Complexity where m = # of rows and n = # of columns.

The idea is to use the first row and first column of the matrix as markers for where we need to
apply 0's throughout the matrix. We also need to save check if there are any 0's in the first row and store as boolean.
We will see later why we need to do that.

After the marking process, we start at the second row (not the first row) and iterate through each row setting the 0's.
Note that when it comes to iterating through the columns we actually need to iterate backwards because
if the first column of the row that we are on gets turned into 0 due to a 0 in it's column but on an previous row,
that newly formed 0 will cause our entire row to automatically be 0 which is definitely what we don't want.
Therefore we must iterate through the columns backwards.

Now the only problem with this solution is the scenario where the first row
does not contain any 0's at all but the subsequent rows do contain 0's yet we still fill in the first 
row with 0's. In that scenario, then the first row will all turn into 0 which is what we don't want. 
To avoid that problem, that is why we had to check if there are any 0's in the first row and store as a boolean 
and also why we start on the second row for the marking process.
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        #all() evaluates to true if the entire list is true. If even one number in the list is a 0
        #Then all() evaluates to false so we negate that to get a true, which is what we want.
        first_row_has_zero = not all(matrix[0])
        
        #mark 0's
        for row in range(1, rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        #Set 0's
        for row in range(1, rows):
            for col in range(cols-1, -1, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
    
        if first_row_has_zero:
            matrix[0] = [0] * cols