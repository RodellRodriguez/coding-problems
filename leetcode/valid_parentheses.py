"""https://leetcode.com/problems/valid-parentheses/description/

"""


class Solution:
    def isValid(self, s):
        def isClosingSymbol(symbol, paren_dict):
            if symbol in paren_dict: return True
            return False
        
        paren_dict = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []
        for symbol in s:
            if isClosingSymbol(symbol, paren_dict):
                if stack:
                    open_symbol = stack.pop()
                    if open_symbol != paren_dict[symbol]: return False
                else: return False
            else: stack.append(symbol)
        return stack == []