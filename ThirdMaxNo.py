import collections
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = collections.defaultdict()
        numset = list(set(nums))
        n = len(numset)
        numset.sort()
        for i in range(n):
            d[i] = numset[i]
        #print d,n
        for k, v in d.items():
            if len(d)>=3:
                return d[n-3]
    
        return d[max(d)]
