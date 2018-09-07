"""https://leetcode.com/problems/jump-game/description/

3 solutions. First one is mine and timed out, Time is O(n^2).
The next two solutions are O(n) one solution going backwards in the list
and the other going forwards respectively. 

"""

"""
Solution 1:
Time Complexity O(n^2)

Recursive backtracking solution where I brute force all the possible jumps
from current position moving forward in the list. We start with the maximum
possible jump from position n and see if we can reach the end. If not then we
backtrack and reduce the maximum jump value by 1 and try again
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        max_jump = nums[0]
        while max_jump > 0:
            if max_jump < len(nums):
                reached_end = self.canJump(nums[max_jump:])
                if reached_end:
                    return True
            max_jump -= 1
        return False

"""
Solution 2:
Backwards in O(n) time. Greedy solution.

Start from the end and set the last index as the index that the previous values in 
the list need to surpass. This last index will be called "goal".
Now we go backwards in the list and see if the i'th index + the value at that index
i.e. the maximum jump can be at least equal to goal. If so then we know that this jump
is now possible from that i'th index so now we can move the "goal" variable from
the last index in the list to the i'th index.

Therefore on the next iteration if the same thing happens then we keep moving the goal
backwards until goal finally equals 0. If the for loop is finished and goal does not
equal 0 then we know that it is not possible for the goal to be reached. If goal is 0
then it was a success.
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        # This returns True if goal is 0, False if otherwise
        return not goal

"""
Solution 3: 
Forwards in O(n) time. Greedy solution.

In the previous solution we wanted the i'th index and the value at that index
to be at least equal to goal. This time it is the opposite since we are starting
from the beginning. We want i + nums[i] <= m (in this solution we call "goal" "m"
instead).

The m variable tells us the max index that can be reached from any of the previous values
in the list. So if you ever reach a part in the list where i + nums[i] is greater than
m then that means NONE of the previous values provides a jump capable of surpassing
the m'th index so end the function and return False immediately.

If you are able to go through the entire for loop without a problem then return True

In my opinion, Solution 2 is probably more intuitive than Solution 3. 
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Tells the max index we can reach so far
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True