sandwisch_orders = ['a','pastrami','b','pastrami','c','pastrami']
finished_sandwiches = []

while sandwisch_orders:
	order = sandwisch_orders.pop()
	print "I made your tunasandwich: "+ order
	finished_sandwiches.append(order)

print "All the sandwish are here:"
for sandwish in finished_sandwiches:
	print sandwish
