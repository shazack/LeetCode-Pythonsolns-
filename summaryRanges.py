class Solution(object):
    def summaryRanges(self, arr):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp = ""
        result = []
        i=0
        #Initialize a start and an end pointer
        start = 0
        end = 0
        while end <= len(arr)-1:
            #Keep incrementing the end pointer until we meet a number not in this range
            if end!=len(arr)-1 and arr[end+1]-arr[end] == 1:
                if end == len(arr)-1:
                    break
            else:
               #once you meet another range, add this to the final result
                temp = str(arr[start])+"->"+str(arr[end])
                #checks if this range is actually a range or a single number
                if arr[end] - arr[start] >= 1:
                    result.append(temp)
                else:
                    result.append(str(arr[end]))
                #now start comes to the beginning of the new range
                start = end + 1
            end += 1
        return result
