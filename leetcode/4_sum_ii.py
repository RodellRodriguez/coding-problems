""" https://leetcode.com/problems/4sum-ii/

Brute force solution is iterating through each number in each list and seeing
if the sum == 0. That is a time complexity of O(n^4) which is terrible.

We can improve on this by cutting the search time by 50% by building a hash table.
We know we have found a match if A[a] + B[b] + C[c] + D[d] == 0. But if we move
C and D to the other side of the equation then we get:

    A[a] + B[b] == - C[c] - D[d]

Therefore what we need to do is we build a hash table and count the number of occurences
that some A[a] + B[b] occur (a+b is the respective key). Then if we find some - C[c] - D[d]
that exists as a key in the hash table then we increase our count variable by the value of
A[a] + B[b]. This is because if say A[0] + B[1] == 2 and A[1] + B[2] == 2 and C[0] and D[2] == -2
then we want to account for both occurences of the summation of 2 i.e. we can get 0 in two ways:

    A[0] + B[1] + C[0] + D[2] == 0
    A[1] + B[2] + C[0] + D[2] == 0


Time Complexity is reduced to O(n^2) and space complexity of O(2n)
"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB_dict = {}        
        for a in A:
            for b in B:
                AB_dict[a+b] = AB_dict.setdefault(a+b, 0) + 1
        count = 0
        for c in C:
            for d in D:
                count += AB_dict.get(-c-d, 0)
                    
        return count