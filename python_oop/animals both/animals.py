
from anna import animal
class dog(animal):
	"""docstring for dog"""
	def __init__(self,name):
		self.name=name
		self.health = 150
	def pet(self):
		self.health+=5
		return self
Dog=dog('fido').walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
	"""docstring for dragon"""
	def __init__(self,name):
		self.name=name
		self.health = 170
	def fly(self):
		self.health-=10
		return self
	def display_health(self):
		super(dragon, self).display_health()
		print 'I am a dragon!'
		return self
dragon=dragon('puff').fly().display_health()
		
