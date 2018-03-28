from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'pthon'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
	print name.title() + "'s favorite language is " + language.title() + "."
print favorite_languages

print "\n"
languages = {}

languages['jen'] = 'pthon'
languages['sarah'] = 'c'
languages['edward'] = 'ruby'
languages['phil'] = 'python'

for name,language in languages.items():
	print name.title() + "'s favorite language is " + language.title() + "."
print languages