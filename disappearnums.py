#find numbers not present in the array
class Solution(object):
    def findDisappearedNumbers(self, nums):
       
        l = len(nums)
        result = []
        temp = None
        for i in range(0,l):
            nums[(nums[i]-1) % l] += l
        for i in range(0,l):
            if nums[i]<=l:
                result.append(i+1)
        return result
                
