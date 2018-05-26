class Solution():
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in nums:
            num ^= i
        return num

class Solution():
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
        	if i in dic.keys():
        		dic.pop(i)
        	else:
        		dic[i] = i
        return dic.popitem()[0]


s = Solution()
print (s.singleNumber([2,2,1]))
print (s.singleNumber([4,1,2,2,1]))