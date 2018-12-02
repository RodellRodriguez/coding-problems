""" https://leetcode.com/problems/path-sum-ii/

    1.) Find Leaf
    2.) Check if summed path == target
    3.) If step 2 is true then append that path to a list
    4.) Repeat steps 2 and 3 for all leaves
    5.) Return list
    
    
At each node during the recursion we have to "remember" the path that we are on
So this we need to have an extra parameter in the method that remembers current path.
We also need another parameter that will contain the list of all valid root-leaf-paths

valid root-leaf path means that path == target sum

Lastly, a COPY of the current path parameter needs to be passed into the recursive calls
otherwise the recursive calls will all reference to the SAME current path parameter all the
way from the first recursive call and that is NOT what we want. It will result in bugs


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        root_to_leaf_paths = []
        current_path = []
        self.findPaths(root, sum, current_path, root_to_leaf_paths)
        return root_to_leaf_paths
        
    def findPaths(self, root, sum, current_path, root_to_leaf_paths):
        if root is None:
            return
        sum -= root.val
        if self.isLeaf(root):
            if sum == 0:
                root_to_leaf_paths.append(current_path + [root.val])
            return
        
        self.findPaths(root.left, sum, current_path + [root.val], root_to_leaf_paths)
        self.findPaths(root.right, sum, current_path + [root.val], root_to_leaf_paths)

    def isLeaf(self, root):
        return root.left is None and root.right is None
        