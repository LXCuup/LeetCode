# Python3.5.1
# -*- coding:UTF-8 -*-
def twoSum(nums, target):
      #执行时间 6852ms
        thenum = len(nums)
        for i in range(thenum):
            for j in range(thenum):
                if nums[i]+nums[j]==target and i != j:
                    return [i,j]

print (twoSum([2,7,11,15],9))
print (twoSum([2,1,3,9],4))

def twoSum2nd(nums, target):
	#执行时间 1124ms
	thenum = len(nums)
	for i in range(thenum):
		j = target-nums[i]
		if (j in nums) and (i != nums.index(j)) :
			return [i,nums.index(j)]
print (twoSum([2,7,11,15],9))
print (twoSum([3,1,5,9],6))
print (twoSum([3,3,1,5,9],6))