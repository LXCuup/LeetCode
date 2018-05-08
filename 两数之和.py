class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        thenum = len(nums)
        for i in range(thenum):
		j = target-nums[i]
		if (j in nums) and (i != nums.index(j)):
			return [i,nums.index(j)]