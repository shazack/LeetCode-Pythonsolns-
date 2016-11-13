class Solution(object):
    def moveZeroes(self, arr):
        count = 0
        for i in range(len(arr)):
           if arr[i]!=0:
            arr[count],arr[i] = arr[i],arr[count]
            #print arr[count],arr[i]
            count += 1

        for i in range(count+1,len(arr)):
            arr[i] = 0
                
