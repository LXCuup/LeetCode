#--coding:utf-8--
class Car(object):
	#一次模拟汽车的简单尝试
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print "This car has " + str(self.odometer_reading) + " miles on it."

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print "You can't roll back an odometer!"

	def increment_odometer(self,miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	#电动车的独特之处
	def __init__(self,make,model,year):
		#初始化父类的属性
		super(ElectricCar,self).__init__(make,model,year)
		self.odometer_reading = 10
		self.battery_size = 70

	def describe_battery(self):
		#打印一条描述电瓶容量的消息
		print "This car has a " + str(self.battery_size) + "-kWh battery."

	def fill_gas_tank(self):
		#电瓶车没有邮箱
		print "This car doesn't need a gas tank."

my_tesla = ElectricCar('tesla','model s',2016)
print my_tesla.get_descriptive_name()

my_tesla.read_odometer()

my_tesla.update_odometer(20)
my_tesla.update_odometer(15)

my_tesla.read_odometer()

my_tesla.increment_odometer(100)
my_tesla.read_odometer()

my_tesla.describe_battery()
my_tesla.fill_gas_tank()