with open('/Users/appie/desktop/Pride.txt') as file_object:
	contents = file_object.read()
	words = contents.split()
	num_words = len(words)
	print num_words


try:
	with open('/user/appie/desktop/Pride.txt') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = "sorry"
	print msg
else:
	words = contents.split()
	num_words = len(words)
	print num_words