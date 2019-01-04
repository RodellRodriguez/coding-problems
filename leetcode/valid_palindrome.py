""" https://leetcode.com/problems/valid-palindrome/

Create a new string of lower case version of original string
Create an empty string and add to it only the alphanumeric characters of the lower case string
Reverse this string and compare if they are the same

"""

class Solution:
    def isPalindrome(self, s):
        # Empty string is trivially a palindrome
        if s == "":
            return True
        
        stripped = ""
        
        # Ignore case
        lowercase = s.lower()
        for letter in lowercase:
            if letter.isalnum():
                stripped += letter
        
        # True if reverse of the stripped string is same
        return stripped[::-1] == stripped