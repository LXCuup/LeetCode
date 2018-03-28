class Age(object):
    def __init__(self, age):
        self.age = age

    def print_age(self):
        print "Happy", self.age, "Birthday"
ages = ['20','21','22','23']
for age in ages:
	age_number = Age(age)
	age_number.print_age()