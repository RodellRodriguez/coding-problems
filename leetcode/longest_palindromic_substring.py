""" https://leetcode.com/problems/longest-palindromic-substring/description/

2 solutions. First solution is the one I came up with. That solution timed out because
it was too slow. Second solution is one of the top answers from leetcode. It's an
impressive algorithm.

Solution 1:
    1. Set max_palindrome = ""
    2. Calculate all substrings and for each substring:
        a. If substring is a palindrome and its length is greater than max_palindrome
        then max_palindrome updates to equal substring
    3. Return max_palindrome

The above solution takes too long because every single substring is calculated and
for each substring we do a palindrome check. Calculating a substring is O(n^2) and
a palindrome check is O(n) so time complexity of this solution is O(n^3)


Solution 2:
    1. Set max_palindrome = ""
    2. For each i'th index in s find the largest palindrome possible where you treat
    the i'th index as the middle of the potential palindrome (odd case):
    3. If the length of the result of step 2 is larger than max_palindrome then set
    max_palindrome to the string from step 2
    4. Repeat step 2 and 3 but for step 2 you handle the case for if input s has an
    even number of letters

The above solution is better because for every index (linear) you do the middle
expansion to check for palindrome (linear) therefore the time complexity for the 
above solution is O(n^2)
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palindrome = ""
        for substring in self.calculate_substring(s):
            print(substring)
            if self.is_palindrome(substring) and len(substring) > len(max_palindrome):
                max_palindrome = substring
        return max_palindrome
    
    def calculate_substring(self, s):
        for i, letter in enumerate(s):
            j = i
            while j < len(s):
                j += 1
                yield s[i:j]
        
    def is_palindrome(self, substring):
        return substring == substring[::-1]



class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_palindrome = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(max_palindrome):
                max_palindrome = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(max_palindrome):
                max_palindrome = tmp
        return max_palindrome
    
    # Middle expansion. The variables l and r act as if they start
    # in the middle of the palindrome and expand left and right
    # respectively to and check equality in order to detect if palindrome
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
