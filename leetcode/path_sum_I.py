""" https://leetcode.com/problems/path-sum/

    1.) If root is None then return False
    2.) Subtract (root value from sum and update sum to that new value
    3.) If root is the leaf then:
            if sum == 0: 
                return True
            return False
    4.) Recursively call the function for root.left and then root.right
    5.) Or the result of step 4 and return the result

Time Complexity: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        sum -= root.val
        if self.isLeaf(root):
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
    def isLeaf(self, root):
        return root.left is None and root.right is None
        