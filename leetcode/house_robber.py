""" https://leetcode.com/problems/house-robber/description/

2 solutions. Both using Dynamic Programming in O(n) time.

"""

""" 
Solution 1.

DP solution. O(n) Time Complexity. O(n) Space complexity

Key observation is to recognize the recursive formula:
    f(0) = nums[0]
    f(1) = max(num[0], num[1])
    ...
    ...
    f(k) = max( f(k-2) + nums[k], f(k-1) )

A key observation is the formula for f(1). This formula works because if f(1) < f(0) then
we wouldn't want to use f(1). There aren't any consquences for this because say we want to use f(2) 
and f(1) < f(0) then we can use f(0) + f(2) since they aren't adjacent. Even if we want to use f(2) we can't
use f(1) since they are adjacent. 

For the f(k) formula we recognize that for the current num in the nums array, the max sum for that index is either:
    1.) The current number (nums[k]) plus the max of the previous non-adjacent index (f(k-2))
    2.) The max sum of the previous index (f(k-1))

In the below solution, the array dp will represent the values of the f(k) function where k is for each index of the nums array

"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
          dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]


"""
Solution 2.

Improved DP solution on the space complexity. O(n) Time Complexity and O(1) Space Complexity

In the previous DP solution, we realize that the recursive formula is:
    f(k) = max(f(k-2) + nums[k], f(k-1))
    
While we can't improve on the linear time, we recognize that as our dp array grows, we are really
interested in only the last 2 values of the dp array as the dp array grows i.e f(k-2) and f(k-1) 
Therefore this means we only need 3 running values: one that holds f(k-2), one that holds f(k-1), and f(k)

This eliminates the need for an entire dp array and only allocate memory for f(k-2), f(k-1) and f(k)

Thus this solution improves to O(1) Space Complexity
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = curr = 0
        for num in nums:
            temp = prev # This represents the nums[k-2]th value
            prev = curr # This represents the nums[k-1]th value
            #Here we just plug into the formula: f(k) = max(f(k-2) + nums[k], f(k-1))
            curr = max(temp + num, prev) 
        return curr