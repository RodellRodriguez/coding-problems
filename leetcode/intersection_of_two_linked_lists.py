"""
Time Complexity: O(n)

The idea is to preserve the value of the two heads and increment them using temp variables until
either of the temp nodes reach the end. Once that happens, set that temp node to the head of the 
other linked list.
The idea is if you switch head, the possible difference between lengths of the two linked lists
would be countered. On the second traversal, they either hit or miss. 
If they meet, temp_a or temp_b would be the node we are looking for, 
if they didn't meet, they will hit the end at the same iteration, temp_a == temp_b == None, 
so return either one of them is the same, None
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        temp_a, temp_b = headA, headB
        while temp_a is not temp_b:
            temp_a = headB if temp_a is None else temp_a.next
            temp_b = headA if temp_b is None else temp_b.next
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return temp_a