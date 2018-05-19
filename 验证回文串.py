class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        new_s = re.sub(r'[^\w]','',s.lower())
        num = int(len(new_s)/2)
        
        the_set = set('1')
        for i in range(num):
        	if new_s[i] == new_s[-1-i]:
        		the_set.add('1')
        	else:
        		the_set.add('0')

        if the_set == {'1'}:
        	return True
        else:
        	return False

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(filter(str.isalnum,s.lower()))
        if s == s[::-1]:
            return True
        else:
            return False

so = Solution()
print (so.isPalindrome("A man, a plan, a canal: Panama"))
print (so.isPalindrome("race a car"))
