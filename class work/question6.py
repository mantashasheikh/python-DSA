#power (x,n) (50)
class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        k = self.findpow(x,n//2)
        if n%2==0:
            return k*k
        else:
            return k*k*x
    def findpow(self,x,n):
        if n>0:
            return self.myPow(x,n) 
        else:
            return 1/self.myPow(x,(n)*(-1))  