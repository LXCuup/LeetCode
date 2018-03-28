prompt = "How old are you?"
answer = raw_input(prompt)
if int(answer) < 3:
	print "Free"
elif int(answer) > 12:
	print "$15"
else:
	print "$10"