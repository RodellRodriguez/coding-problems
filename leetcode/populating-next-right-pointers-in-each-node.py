"""	https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

Time Complexity: O(n) where n is number of tree nodes
Space Complexity: O(1)

The trick is to build the children's connections from the parent node and when
you need to connect a child node to an adjacent subtree's child node then just
use the parent node's next to do so.

"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            next_level = root.left
            while root and next_level:
                root.left.next = root.right
                if root.next: 
                	root.right.next = root.next.left
                else: 
                	root.right.next = None
                root = root.next
            root = next_level
