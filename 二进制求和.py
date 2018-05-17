class Solution:
    def addBinary(self, a,b):
    	# 执行用时68ms
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        cc = str(int(a) + int(b))
        ccc = list(cc)
        c = []
        [c.append(int(i)) for i in ccc]
        	

        num = 0
        for i in range(len(c)-1,-1,-1):
        	c[i] += num
        	num = 0
        	if c[i] >= 2:
        		c[i] = c[i]-2
        		num = 1
        if num == 1:
        	c.insert(0,1)

        answer = 0
        ans = c[::-1]
        for i in range(len(ans)):
        	answer += ans[i]*(10**(i))
        return str(answer)

        

s = Solution()
print (s.addBinary('11','1')) # 100
print (s.addBinary('1010','1011')) #10101
print (s.addBinary('1111','1111')) #11110