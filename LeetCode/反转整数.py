"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 
[−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""
def reverse(x):
	y = list(str(abs(x)))
	a = ''	
	for i in range(len(y)):
		a = a + str(y[len(y)-i-1])
	if abs(x) == x:
		if int(a) > 2**31-1:
			return 0
		else:
			return int(a)
	if abs(x) == -x:
		if -int(a) < -2**31:
			return 0
		else:
			return -int(a)

print (reverse(123))
print (reverse(-123))
print (reverse(120))
print (reverse(-120))
print (reverse(1534236469))