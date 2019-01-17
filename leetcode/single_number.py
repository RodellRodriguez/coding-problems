""" https://leetcode.com/problems/single-number/

"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Assume array has a size of at least 3
        Every number is appears twice except one number. FInd that one number.
        
        
        Hash table to get the counts of each number. Use the number as key and count as value.
        Return the key where the count  = 1
            -> Space: O(n)
            -> Time: O(n)
            
        Improved solution with Space: O(1)
        
        Any number XOR'd with itself = 0. Any number XOR'd with 0 remains the same.
        a XOR a = 0
        0 XOR a = a
        a XOR b = c
        c XOR b = a
        
        XOR is associative and commutative therefore we can XOR the array in any order we want.
        
        4, 1, 2, 1, 2
        """
        
        single_num = nums[0]
        for index, num in enumerate(nums[1:]):
            single_num ^= num
        return single_num