class Car(object):
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't roll back an odometer!"

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print "This car has " + str(self.odometer_reading) + " miles on it."

	def get_name(self):
		name = str(self.year) + ' ' + self.make + ' ' + self.model + ' '+ str(self.odometer_reading)
		print name

my_new_car = Car('audi','a4',2016)
print my_new_car.get_descriptive_name()
my_new_car.read_odometer()

my_old_car = Car('auto','a1','2000')
my_old_car.year = 2001
print my_old_car.get_descriptive_name()
my_old_car.update_odometer(18)
my_old_car.read_odometer()

my_old_car.update_odometer(19)
my_old_car.read_odometer()

my_car = Car('bens','s1',2002)
my_car.odometer_reading = 26
my_car.get_name()