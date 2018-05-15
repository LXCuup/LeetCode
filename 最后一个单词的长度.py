class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1 = s.strip()
        if len(s1) == 0:
        	return 0
        return len(s1.split(' ')[-1])
        


s = Solution()
print (s.lengthOfLastWord('Hello World  '))
print (s.lengthOfLastWord('World  '))
print (s.lengthOfLastWord('  '))