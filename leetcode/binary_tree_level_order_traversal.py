""" https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Used a traditional queue method for Breadth First Search (BFS). I use the deque
class from the python collections library for optimized speed for
popping from the 0th index of the queue.

"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            next_level = deque([])
            level = []
            while queue:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            res.append(level)
        return res