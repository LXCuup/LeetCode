class Solution:
    def mySqrt(self,x):
        # 84ms
        """
        :type x: int
        :rtype: int
        """
        from math import sqrt,floor
        return floor(sqrt(x))

class Solution:
    def mySqrt(self,x):
        # 76ms
        """
        :type x: int
        :rtype: int
        """
        return int(x ** (1/2))

s = Solution()
print (s.mySqrt(4))
print (s.mySqrt(8))
print (s.mySqrt(0))