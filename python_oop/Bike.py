class bike(object):

	rdistance = 10
	revdistance = 5
	
	def __init__(self, price, max_speed, miles):
		self.price=price
		self.max_speed=max_speed
		self.miles=miles
	def ride(self):
		self.miles = int(self.miles + self.rdistance)
		return 'Riding'
	def reverse(self):
		self.miles = int(self.miles - self.revdistance)
		return 'Reversing'
	def displayinfo(self):
		return '{} {} {}'.format(self.price,self.max_speed,self.miles)

		

bike_1 = bike('$100', '15mph', 0)
bike_2 = bike('$200', '20mph', 0)
bike_3 = bike('$300', '25mph', 0)

print bike_1.ride()
print bike_1.ride()
print bike_1.ride()
print bike_1.reverse()
print bike_1.displayinfo()
print bike_1.ride()
print bike_1.ride()
print bike_1.reverse()
print bike_1.reverse()
print bike_1.displayinfo()
print bike_1.reverse()
print bike_1.reverse()
print bike_1.reverse()
print bike_1.displayinfo()