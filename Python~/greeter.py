#--coding:utf-8--
def greet_user():
	print "Hello!"
greet_user()	

def greet_user(username,sexy):
	print "Hello, " + username.title() + ", you are a beautiful " + sexy + "!"
greet_user('jesse','girl')
greet_user('Mike','boy')