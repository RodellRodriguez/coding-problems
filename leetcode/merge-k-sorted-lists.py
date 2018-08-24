"""https://leetcode.com/problems/merge-k-sorted-lists/

Idea is to push every single element from all the lists into a min heap
data structure then convert the heap into a single list. The problem
is trivial if you use a heap.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        heapq.heapify(heap)
        for head in lists:
            while head:
                heapq.heappush(heap,head.val)
                head = head.next
        ret = []
        while heap:
            ret.append(heapq.heappop(heap))
        return ret
        
        