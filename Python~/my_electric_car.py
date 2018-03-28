from Cars import ElectricCar,Car

my_beetle = Car('Volkswagen','beetle',2016)
print my_beetle.get_descriptive_name()

my_tesla = ElectricCar('tesla','model s',2016)
print my_tesla.get_descriptive_name()

my_tesla.battery.describe_battery()
my_tesla.battery.battery_size = 85
my_tesla.battery.get_range()
