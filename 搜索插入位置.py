class Solution:
    def searchInsert(self, nums, target):
    	# 执行用时 52ms
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        li = nums
        li.append(target)
        li1 = sorted(li)
        return li1.index(target)

class Solution:
    def searchInsert(self, nums, target):
    	# 执行用时 48ms
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,num in enumerate(nums):
        	if num >= target:
        		return i
        return len(nums)

s = Solution()
print (s.searchInsert([1,3,5,6],5))
print (s.searchInsert([1,3,5,6],2))
print (s.searchInsert([1,3,5,6],7))
print (s.searchInsert([1,3,5,6],0))
