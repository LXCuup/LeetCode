#--coding:utf-8--
import json
def greet_user():
#问候用户，并指出其名字
	filename = 'username.json'
	try:
		with open(filename) as file_object:
		username = json.load(file_object)
	except IOError:
		username = raw_input("What is your name? ")
		filename = 'username.json'
		with open(filename,'w') as file_object:
			json.dump(username,file_object)
			print "We will remember you when you come back, " + username + " !"
	else:
		print "Welcome back, " + username + "！"
greet_user()