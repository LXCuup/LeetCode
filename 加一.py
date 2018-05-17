class Solution:
    def plusOne(self, digits):
        # 执行用时 52ms
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        word = ''
        for i in digits:
        	word += str(i)
        new_word = int(word) + 1
        li = list(str(new_word))
        new_li = []
        [new_li.append(int(j)) for j in li]	
        return new_li

class Solution:
    def plusOne(self, digits):
        # 执行用时 36ms
        """
        :type digits: List[int]
        :rtyrtype: List[int]
        """

        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            carry = 0
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1

        if carry == 1:
            digits.insert(0,1)
        return digits

s = Solution()
print (s.plusOne([1,2,3,9]))
