""" https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Perform a DFS and create a an array for each level and find the max of each level and append
to the array that will contain the max of each level

"""

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = [root.val]
        queue = [root]
        while queue:
            nextQueueNodes = []
            nextQueueValues = []
            for node in queue:
                if node.left: 
                    nextQueueNodes.append(node.left)
                    nextQueueValues.append(node.left.val)
                if node.right: 
                    nextQueueNodes.append(node.right)
                    nextQueueValues.append(node.right.val)
            if nextQueueValues: 
                res.append(max(nextQueueValues))
            queue = nextQueueNodes
        return res