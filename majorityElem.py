import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        n = len(nums)
        maj = 0 
        for k,v in c.items():
            if v > n/2:
                maj = k
        print maj
        return maj
                
            
