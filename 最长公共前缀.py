def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	if len(strs) == 0:
		return ""
	if len(set(strs)) == 1:
		return strs[0]
	l1 = sorted(strs,key=lambda key:len(key))
	







print (longestCommonPrefix(["flower","flow","flight"]))
print (longestCommonPrefix(["dog","racecar","car"]))
print (longestCommonPrefix(["flower","flow","floght"]))
print (longestCommonPrefix(["flower","fiow","floght"]))
print (longestCommonPrefix(['aa','a']))
print (longestCommonPrefix(["a"]))
print (longestCommonPrefix(["a",'a']))
print (longestCommonPrefix([""]))
print (longestCommonPrefix([]))
print (longestCommonPrefix(['']))