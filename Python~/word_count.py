#--coding:utf-8--
def count_words(filename):
	#计算一个文件大致包含多少个单词
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except IOError:
		msg = "Sorry"
		print msg
	else:
		#计算文件大致包含多少个单词
		print contents
		words = contents.split()
		num_words = len(words)
		print num_words
filename = 'programing.txt'
count_words(filename)