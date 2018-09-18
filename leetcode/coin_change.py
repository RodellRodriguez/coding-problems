""" https://leetcode.com/problems/coin-change/description/

Dp Bottom-Up solution.
The idea is to recognize that if n = amount and F(n) = answer
then to calculate F(n) we need to compute all minimum counts for amounts up to n.
So we need the min count all the way up to F(n - c) where c is current coin in the iteration. Then you add +1 to it to include the current coin as part of the coin count.

The key insight for this problem is to recognize the F(n-c) + 1 relationship and why that makes sense.

Time Complexity: O(n * i) where n is the desired amount of change and i is the number of coin denominations we have

Space Complexity: O(n) since we need a value in every index to cache the coin denomination results for every amount of change
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #Set up largest amount possible
        max_amount = amount + 1
        #Set up the cache where you fill in each index with the ceiling value
        cache = [max_amount for _ in range(max_amount)]
        #There are 0 coins to get an amount of 0
        cache[0] = 0
        #Iterate linearly through each amount value
        for i in range(1, max_amount):
            for coin in coins:
                #For each coin, check if we can use it in our current amount value
                if coin <= i: 
                    #This is the crux of of the solution and is the recursive formula
                    #You add +1 to count the current coin
                    cache[i] = min(cache[i], cache[i - coin] + 1)
        if cache[amount] > amount: return -1
        else: return cache[amount]