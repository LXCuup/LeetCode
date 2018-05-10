def isValid(s):
	li = []
	for c in s:
		if (c == '('):
			li.append(')')
		elif (c == '{'):
			li.append('}')
		elif (c == '['):
			li.append(']')
		elif (not li or c != li.pop()):
			return False
	return not li