"""

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