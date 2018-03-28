def make_car(brand,style,**car_info):
	car = {}
	car['brand'] = brand
	car['style'] = style
	for key,value in car_info.items():
		car[key] = value
	return car
car = make_car('subaru','outback',color = 'blue',size = 'big')
print car
car['color'] = 'red'
print car