from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        i = 0
        j = 0 
        ans = 0
        map_index = defaultdict(int)
        for j in range(0,n):
            if s[j] in map_index:
                i = max(map_index[s[j]],i)
            ans = max(ans,j-i+1)
            map_index[s[j]] = j+1
        return ans
