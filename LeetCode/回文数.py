"""
判断一个整数是否是回文数。回文数是指正序（从左向右）
和倒序（从右向左）读都是一样的整数。
"""
def isPalindrome(x):
	'''
	执行用时：252ms
	'''
	dics ={}
	li = []
	for i,num in enumerate(str(x)):
		dics[i] = num
	for j in dics:
		if dics[j] == dics[len(dics)-1-j]:
			li.append('right')
		else:
			li.append('wrong')
	if set(li) == {'right'}:

		return True
	else:
		return False

print (isPalindrome(121))
print(isPalindrome(10))

def isPalindromes(x):
	"""
	执行用时：224 ms
	"""
	if x < 0:
		return False
	if x >= 0 :
		li1 = list(str(x))
		li2 = li1[::-1]
		if li2 == li1:
			return True
		else:
			return False
print (isPalindromes(121))
print(isPalindromes(10))

def isPalindromex(x):
	"""
	执行用时：192 ms
	"""
	li1 = list(str(x))
	li2 = li1[::-1]
	if li2 == li1:
		return True
	else:
		return False
print (isPalindromex(121))
print(isPalindromex(10))

def isPalindromey(x):
	"""
	执行用时：256 ms
	"""
	return str(x) ==str(x)[::-1]
print (isPalindromey(121))
print(isPalindromey(10))