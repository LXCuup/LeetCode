filename = 'programing.txt'

with open(filename,'w') as file_object:
	file_object.write("I love programming.")
	file_object.write("I love creating new games.\n")
	file_object.write("\n")
	line1 = raw_input("line1:")
	line2 = raw_input("line2:")
	line3 = raw_input("line3:")
	file_object.write(line1)
	file_object.write("\n")
	file_object.write(line2)
	file_object.write("\n")
	file_object.write(line3)