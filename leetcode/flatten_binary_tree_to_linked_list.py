"""
The desired flattened list is a result of a pre-order traversal specifically root, left, right.
The trick then is to do the recursive in-place modification in reverse order,
specifically post-order in right, left, root.

The actual modification is simple and goes as follows:
    1.) Have an initial prev and set it to None. The value of prev must be tracked
    throughout the entirety of this solution so we set prev as a property of the solution
    2.) Set root.right to prev
    3.) Set left to None
    4.) Update prev to the current root
    
Because we are going in reverse order, this modification works
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        