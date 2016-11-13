
#Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

#Find all the elements that appear twice in this array.
"""
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

Could you do it without extra space and in O(n) runtime?
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        soln = []
        n = len(nums)
        nums.sort()
        for i in range(0,n-1):
            if nums[i] == nums[i+1]:
                soln.append(nums[i])
        
        return soln
            
