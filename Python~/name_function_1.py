#--coding:utf-8--
def get_formatted_name(first,last,middle = ''):
	print "Enter 'q' at any time to quit."
	while True:
		first = raw_input("Please give me a first name: ")
		if first == 'q':
			break
		middle = raw_input("Please give me a middle name: ")
		if middle == 'q':
			break
		last = raw_input("Please give me a last name: ")
		if last == 'q':
			break
		if middle:
			full_name = first + ' ' + middle + ' ' + last
		else:
			full_name = first + ' ' + last
		print full_name.title()
get_formatted_name('first','last')
get_formatted_name('first','last','middle')