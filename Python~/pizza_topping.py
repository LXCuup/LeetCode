#coding:utf-8
def make_pizza(size,*toppings):
	#概述要制作的披萨
	print "Making a " + str(size) + "-inch pizza with the following topping:"
	for topping in toppings:
		print "-" + topping
	print '\n'

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')