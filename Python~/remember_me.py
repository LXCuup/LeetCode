#--coding:utf-8--
import json

username = raw_input("What is your name? ")
filename = 'username.json'
with open(filename,'w') as file_object:
	json.dump(username,file_object)
	print "We will remember you when you come back, "+ username + "!"