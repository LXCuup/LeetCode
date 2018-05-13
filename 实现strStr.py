#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

class Solution(object):
	def strStr(self,haystack,needle):
		# 执行用时 112ms
		"""
		:type haystack:str
		:type needle:str
		:rtype:int
		"""
		import re
		m = re.search(needle,haystack)
		if m is not None:
			return m.start()
		else:
			return -1


class Solution(object):
	def strStr(self,haystack,needle):
		# 执行用时 28ms
		"""
		:type haystack:str
		:type needle:str
		:rtype:int
		"""
		if needle in haystack:
			return haystack.index(needle)
		else:
			return -1

s = Solution()
print (s.strStr("hello","ll"))
print (s.strStr("aaaaa","bba"))
print (s.strStr("a","a"))