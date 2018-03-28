#--coding:utf-8--
import json
def get_stored_username():
	#如果存储了用户名，就获取它
	filename = 'username.json'
	try:
		with open(filename) as file_object:
			username = json.load(file_object)
	except IOError:
		return None
	else:
		return username

def greet_user():
	#问候用户，并指出其名字
	username = get_stored_username()
	if username:
		print "Welcome back, " + username + " !"
	else:
		username = raw_input("What is your name? ")
		filename = 'username.json'
		with open(filename,'w') as file_object:
			json.dump(username,file_object)
			print "We will remember you when you come back, " + username + "!"
greet_user()