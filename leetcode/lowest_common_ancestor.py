"""
Idea is to find where p and q from the perspective of the LCA
If root has a left and a right that means p and q are in completely different sub trees
Therefore their only LCA is the current root that has a left and right value
If root only has a left then just return the left and not the root because we only found p or q
But not both. Same with if root only has a right. Eventually when the left and right values propagate
Upwards the call stack we'll end up with a root that has both a left and a right
This algorithm works assuming we have a valid p and q

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        if left: return left
        if right: return right