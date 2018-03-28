print "Give me two number,and I'll divide them."
print "Enter 'q' to quit."

while True:
	first_number = raw_input("\n first_number:")
	if first_number == 'q':
		break
	second_number = raw_input("second_number:")
	if second_number =='q':
		break
try:
	answer = int(first_number) / int(second_number)
except ZeroDivisionError:
	print "You can't divide by zero!"
else:
	print answer