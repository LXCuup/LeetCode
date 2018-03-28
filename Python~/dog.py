#--coding:utf-8--
class Dog(object):

	def __init__(self,name,age):#初始化属性
		self.name = name
		self.age = age

	def sit(self):
		print self.name.title() + ", is now sitting."

	def roll_over(self):
		print self.name.title() + "'rolled over."

my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print "My dog's name is " + my_dog.name.title() + "."
print "my dog is " + str(my_dog.age) + " years old."
my_dog.sit()