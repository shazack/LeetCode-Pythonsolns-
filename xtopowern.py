class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n<0:
            return 1.0 / self.myPow(x,-n)
        if n%2 == 0:
            temp = self.myPow(x,n/2)
            return temp*temp
        else:
            return x * self.myPow(x, n-1)
            
            
    

        
