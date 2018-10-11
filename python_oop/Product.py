class product(object):
	"""docstring for product"""
	def __init__(self,price,item_name,weight,brand):
		self.price=price
		self.item_name=item_name
		self.weight=weight
		self.brand=brand
		self.status= 'for sale'

	def sell(self):
		self.status = 'sold'
		return self
	def tax(self):
		self.price = self.price*1.08
		return self
	def returned(self,reason):
		self.reason = reason
		if self.reason == 'defective':
			self.price = 0
			self.status = 'defective'
		if self.reason == 'open':
			self.status = 'used'
			self.price = self.price*0.8
		if self.reason == 'like new':
			self.status = 'for sale'
		return self
	def display_all(self):
		print '{} {} {} {} {}'.format(self.item_name,self.weight,self.brand,self.status,self.price)
		return self
product1 = product(3.99,'chips','1lb','pringles')
product2 = product(8.99,'jerky','3lb','beefy')
product3 = product(4.99,'watermelon','5lb','fresh place')
product4 = product(2.99,'crackers','1lb','ritz')
product5 = product(.99,'water','1lb','spring')
product6 = product(1.99,'milk','3lb','store brand')

product1.returned('defective').display_all()
product2.tax().sell().display_all()
product3.returned('open').display_all()