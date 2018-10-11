class car(object):

	def __init__(self,price,speed,fuel,mileage,tax):
		self.price=price
		self.speed=speed
		self.fuel=fuel
		self.mileage=mileage
		self.tax=tax
		if (self.price > 10000):
				self.tax = '15%'

	def display_all(self):
		return '{} {} {} {} {}'.format(self.price,self.speed,self.fuel,self.mileage,self.tax)

car1=car(1000,'30mph','full','20mpg','12%')
car2=car(2000,'40mph','not full','40mpg','12%')
car3=car(3000,'50mph','half','30mpg','12%')
car4=car(4000,'120mph','full','35mpg','12%')
car5=car(11000,'160mph','sort of full','20mpg','12%')
car6=car('neg','how fast can you push it?','fullish','your lucky if you get there','12%')

print car5.display_all()