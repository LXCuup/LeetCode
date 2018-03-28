def get_formatted_name(first_name,last_name,middle_name = ''):
	if middle_name:
		full_name = first_name + ' '+ middle_name + ' ' + last_name
	else:
		full_name = first_name +' ' + last_name
	return full_name.title()

while True:
	print "\nPlease tell me your name:"
	print "Eenter 'q' at any time to quit"
	f_name = raw_input("First_name:")
	if f_name == 'q':
		break
	m_mame = raw_input("Middle_name:")
	if m_mame == 'q':
		break
	l_name = raw_input("Last_name:")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name,l_name,m_mame)
	print "\nHello," + formatted_name + "!"