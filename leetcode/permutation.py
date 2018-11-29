""" Recursive Solution
1.) Strip off the last num recursively (we could've also used the first number, this only affects the ordering of the final list)
Until we have an empty list. 
2.) Upon getting an empty list we return an empty list of lists.
3.) Now each time the call stack returns we take the returned list of lists which will be the previous
permutations. 
4.) Create an empty list for space for our updated permutations
5.) Iterate through each list of previous permutations then take the number we stripped off and 
inserting that number in every possible position of each list of permutations
6.) The result of step 5 will result in a list of lists, each inner list representing the updated
permutation therefore you must concatenate this new list to the updated permutations empty list
that was created in step 4
7.) Return the updated permutations list
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        prev_permutations = self.permute(nums[:-1])
        updated_permutation = []
        for permutation in prev_permutations:
            updated_permutation += self.insertAtEveryPosition(permutation, nums[-1])
        return updated_permutation
            
    def insertAtEveryPosition(self, permutation, num):
        new_permutations = []
        for index in range(len(permutation) + 1):
            permutation_to_append = permutation[:index] + [num] + permutation[index:]
            new_permutations.append(permutation_to_append)
        return new_permutations


""" Iterative Solution
The idea is to insert the current number into each possible position of our current
list of permutations. The result of that is a new list of permutations so we update
our current list of permutations to be equal to this new list of permutations. We do this
until we reach the end of our list of nums.

This solution could be done all in 1 function but it's better for code readability
to separate the functionality. This is important because the insertAtEveryPosition function
was a tricky to come up with. Initially I ended up with off by 1 type bugs so it was even more
important to separate this function from the main function.
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = [[]]
        for n in nums:
            new_permutations = []
            for perm in permutations:
                new_permutations += self.insertAtEveryPosition(perm, n)
            permutations = new_permutations
        return permutations
            
    def insertAtEveryPosition(self, permutation, num):
        new_permutations = []
        for index in range(len(permutation) + 1):
            permutation_to_append = permutation[:index] + [num] + permutation[index:]
            new_permutations.append(permutation_to_append)
        return new_permutations