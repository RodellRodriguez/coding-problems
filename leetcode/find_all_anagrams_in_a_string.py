""" https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

2 solutions. Solution 1 is my solution but it timed out. Time complexity is O(n^2)
and it's too slow.

"""


from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if not s or not p:
            return res
        l, r = 0, len(p)
        p_count = Counter(p)
        while r <= len(s):
            if p_count == Counter(s[l:r]):
                res.append(l)
            l += 1
            r += 1
        return res