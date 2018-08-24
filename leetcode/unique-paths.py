""" https://leetcode.com/problems/unique-paths/

Time Complexity: O(nm) where n is number of rows and m is number of columns 
Space Complexity: O(nm)

The number of ways to go from (0,0) to (n,m) is the number of ways from (1,0) to (n,m)
plus the number of ways from (0,1) to (n,m). If you continue this pattern, this is a recursive
relationship and there lies an opportunity for memoization to cache number of ways for any
position of the grid that has already been calculated.
"""


class Solution():
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = [[None] * m for _ in range(n)]
        return self._helper(0, 0, n, m, cache)
    
    def _helper(self, x, y, n, m, dp):
        if self.reached_bottom_right(x, y, n, m): return 1
        if self.is_out_of_bounds(x, y, n, m): return 0
        if not dp[x][y]:
            down_count = self.uniquePathsHelper(x+1, y, n, m, dp)
            right_count = self.uniquePathsHelper(x, y+1, n, m, dp)
            dp[x][y] = down_count + right_count
        num_of_paths = dp[x][y]
        return num_of_paths
        
    def reached_bottom_right(self, x, y, n, m):
        return (x == n-1 and y == m-1)
    
    def is_out_of_bounds(self, x, y, n, m):
        return (x > n-1 or y > m-1)