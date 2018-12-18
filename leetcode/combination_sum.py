""" https://leetcode.com/problems/combination-sum/

Solution is taken from leetcode. I had the same high level idea but struggled with
the implementation. In particular the final two lines of the helper function was the
part that tripped me up the most.

The idea is a depth first search approach by replicating the number via recursion until the target
is reached or goes over the target. If the target is reached then that path can be
appended to the solution set, otherwise return from the call stack.

You have to cycle through all of the numbers in the array and repeat this process to account
for all possible combinations. Therefore you need a for loop as the controller to go through
each index but at each iteration requires a recursive call in order to give a new scope

In addition, the list of cadidates should be sorted so that we know that if we ever
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        if candidates:
            self.dfs(candidates, target, 0, [], res)
        return res
    
    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path + [candidates[i]], res)
            