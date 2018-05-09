def longestCommonPrefix(strs):

	if len(strs) == 0:
		return ("")
	if len (set(strs)) == 1:
		return (strs[0])
	li = sorted(strs,key = lambda key:len(key))
	str = ""
	for i in range(len(li[0])):
		lif = sorted(li,key = lambda key:(key[i]))
		lir = sorted(li,key = lambda key:(key[i]),reverse = True)
		if lif == lir:
			str += li[0][i]
		else:
			break
	return str
		



li1 = ["flower","flow","flight"] # fl
li2 = ['a','b'] #
li3 = ['a'] # a
li4 = ['a','b','c'] #
li5 = ['ba','b','bc'] # b
li6 = ["aca","cba"]
print (longestCommonPrefix(li1))
print (longestCommonPrefix(li2))
print (longestCommonPrefix(li3))
print (longestCommonPrefix(li4))
print (longestCommonPrefix(li5))
print (longestCommonPrefix(li6))