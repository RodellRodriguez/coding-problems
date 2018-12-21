"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

First solution is mine and second is one of the fastest solutions in leetcode

Build a hash table that keeps count of all of the possible numbers that can appear
in the array, then mutate the count as you iterate through the nums array.
Return all keys who's count value did not change


Leetcode solution was to turn the nums array into a set
and subtract that from the set that contains all possible
nums. The left over nums are the answer.

"""

from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter([i for i in range(1,len(nums)+1)])
        for num in nums:
            counter[num] += 1
        
        # The counter initialies all possible nums with a count of 1
        res = [num for num, count in counter.items() if count == 1]
        return res



class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list(set(range(1, len(nums)+1)) - set(nums))
        return res