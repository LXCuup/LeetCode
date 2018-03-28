def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print msg

usernames = ['hannah','ty','margot']
usernames.append('mike')
greet_users(usernames)