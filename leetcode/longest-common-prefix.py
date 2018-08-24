"""https://leetcode.com/problems/longest-common-prefix/

Time Complexity: O(nm) n is number of words in list and m is number of letters
in the shortest word in the list

Space Complexity: O(m)


Take the first word of the list and loop through its characters.
For each of its characters check if all the other words has that character
in the same index. If all other words have that character then append that
character to the return string.

The exception handling is in place in the case that one of the words is shorter
than the first word which means we've reached the max longest common prefix so 
return the return string we've built so far
    
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ""
        if strs:
            for index, letter in enumerate(strs[0]):
                for word in strs[1:]:
                    try:
                        if letter != word[index]: return ret
                    except IndexError as e: return ret
                ret += letter
        return ret