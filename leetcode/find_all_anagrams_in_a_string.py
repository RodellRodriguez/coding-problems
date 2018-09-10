""" https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

2 solutions. Solution 1 is my solution but it timed out. Time complexity is O(n^2)
and it's too slow.

Solution 2 is similar to solution 1. The biggest difference is that Counter
is not being created at every iteration. Each time you create Counter, thats O(n)
thus reducing the time complexity of the solution to O(n)

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


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1)
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res