def reverse(x):
	y = list(str(abs(x)))
	a = ''	
	for i in range(len(y)):
		a = a + str(y[len(y)-i-1])
	if abs(x) == x:
		if int(a) > 2**31-1:
			return 0
		else:
			return int(a)
	if abs(x) == -x:
		if -int(a) < -2**31:
			return 0
		else:
			return -int(a)

print (reverse(123))
print (reverse(-123))
print (reverse(120))
print (reverse(-120))
print (reverse(1534236469))