def build_person (first_name,last_name,age = '',middle_name = ''):
	person = {'first':first_name,'last':last_name}
	
	if age:
		person['age'] = age

	if middle_name:
		person['middle_name'] = middle_name
	return person	
musician = build_person('jimi','hendrix',age = 27,middle_name = 'mike')
print musician

def build_person (first_name,last_name):
	person = {'first':first_name,'last':last_name}

	return person	

musician = build_person('jimi','hendrix')
print musician