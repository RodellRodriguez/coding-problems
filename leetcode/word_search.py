""" https://leetcode.com/problems/word-search/description/

2 solutions. Both solutions are similar but 2'nd solution is a minor improvement on
Solution 1.
"""


"""
Solution 1:

For each cell in the matrix, perform a depth first search (dfs) and recursively
see if each encountered cell from the dfs matches the first letter of the word
variable until the word variable is empty. Each recursive call means a match was found 
so then the first letter of the word variable is stripped away so the recursive call 
looks for the next letter in the word variable. 
The dfs algorithm searches both horizontally and vertically.

	1. Check the base case i.e. length of word is 0. If so we are done. 
	2. Check if current row and col coordinates of the current call stack are both
	within the bounds of the matrix and that the current cell matches word[0]. If
	either condition is false then return immediately
	3. We have to mark the current cell as visited so we overwrite the current cell with a 
blank character. We have to restore this cell to its original state before this 
call stack is returned so store original letter in this cell in memory before overwriting
	4. Start the recursive call and perform the call both horizontally and vertically by
	changing the row/col parameters and store the boolean result of these calls. 
	Additionally we strip away the first character of the word variable for each recursive call.
	We are prioritizing when a True boolean is returned. As soon as we get at least one
	True value then we stop the recursion. Store this boolean as result variable
	5. Restore the current cell to its original letter so the board remains unaffected
	6. Return result variable

Worst case scenario this time complexity is O(n^3)
"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    return True
        return False
    
    def dfs(self, board, row, col, word):
        if len(word) == 0:
            return True
        
        if (self.is_out_of_bounds(board, row, col) 
            or board[row][col] != word[0]):
            return False

        temp = board[row][col]
        self.mark_as_visited(board, row, col)
        result = (self.dfs(board, row+1, col, word[1:])
                 or self.dfs(board, row-1, col, word[1:])
                 or self.dfs(board, row, col+1, word[1:])
                 or self.dfs(board, row, col-1, word[1:]))
        self.undo_mark(board, row, col, temp)
        return result
    
    def is_out_of_bounds(self, board, row, col):
        if (row < 0 or row >= len(board) 
            or col < 0 or col >= len(board[0])):
            return True
        return False
        
    def mark_as_visited(self, board, row, col):
        board[row][col] = ""
                        
    def undo_mark(self, board, row, col, letter):
        board[row][col] = letter


"""
Solution 2:

Similar solution to Solution 1 except instead of stripping the word variable
by its first character, we include a new parameter in the dfs function and call this
parameter "index". This index variable will track how many of the chars in the word
variable we have matched so far. The index variable will start at 0 and each successful
match we increase the index variable by 1. Thus changing the base case and reducing the
space complexity and linear time complexity of the act of stripping off the first
character of the word variable like in Solution 1.

Everything else remains the same.

"""
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word, 0):
                    return True
        return False
    
    def dfs(self, board, row, col, word, index):
        if index == len(word):
            return True
        
        if (self.is_out_of_bounds(board, row, col) 
            or board[row][col] != word[index]):
            return False
        
        temp = board[row][col]
        self.mark_as_visited(board, row, col)
        result = (self.dfs(board, row+1, col, word, index+1)
                 or self.dfs(board, row-1, col, word, index+1)
                 or self.dfs(board, row, col+1, word, index+1)
                 or self.dfs(board, row, col-1, word, index+1))
        self.undo_mark(board, row, col, temp)
        return result
    
    def is_out_of_bounds(self, board, row, col):
        if (row < 0 or row >= len(board) 
            or col < 0 or col >= len(board[0])):
            return True
        return False
        
    def mark_as_visited(self, board, row, col):
        board[row][col] = ""
                        
    def undo_mark(self, board, row, col, letter):
        board[row][col] = letter
