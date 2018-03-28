#--coding:utf-8--
print "Enter 'q' at any time to quit."
while True:
	first = raw_input("Please give me a first name: ")
	if first == 'q':
		break
	last = raw_input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = first + ' ' + last
	print "Neatly formatted name: " + formatted_name + "."
	print "\n"