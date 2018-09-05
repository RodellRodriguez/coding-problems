""" https://leetcode.com/problems/3sum/description/
Time Complexity: O(nlogn + n^2) -> O(n^2)
Space Complexity: O(n)

1. Create empty res list
2. Sort the list in ascending order
3. Iterate from 0'th index up to 2'nd to last index (excluding):
    a. Check if previous i'th result is a duplicate and if so then skip this loop
    b. Create a window where you set the start of the window of  i +1
    and the end of the window to the last element of the list
    c. Now find the sum of the i'th element with the left and right end of the window
    and see if it equals 0.
    d. If the sum is less than 0 then increment the left end, if the sum is
    greater than 0 then decrement the right end
    e. If the sum equals 0 then append this match to the final list
    f. Then increment/decrement the left and right end of the window respectively until no duplicate 
    numbers are found
4. Return res
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # Increment if duplicate i'th number is encountered
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                if s > 0:
                    r -= 1
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Increment if duplicate l'th number is encountered
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Decrement if duplicate r'th number is encountered
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res