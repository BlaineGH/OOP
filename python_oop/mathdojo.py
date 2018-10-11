class Mathdojo(object):
	"""docstring for Mathdojo"""
	count = 0
	def add(self, *arg):
		for a in arg:
			if(isinstance(a, (int))):
				Mathdojo.count+=a
			if(isinstance(a, (list))):
				for i in range(0,len(a)):
					Mathdojo.count+=a[i]
			if(isinstance(a,(set))):
				b=list(a)
				for i in range(0,len(b)):
					Mathdojo.count+=b[i]
		return self
	def subtract(self, *arg):
		for a in arg:
			if(isinstance(a, (int))):
				Mathdojo.count-=a
			if(isinstance(a, (list))):
				for i in range(0,len(a)):
					Mathdojo.count-=a[i]
			if(isinstance(a,(set))):
				b=list(a)
				for i in range(0,len(b)):
					Mathdojo.count-=b[i]
		return self
	def result(self):
		print Mathdojo.count
		return self
md=Mathdojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3],{3,4,5,6}, [1.1,2.3]).result()

		
		