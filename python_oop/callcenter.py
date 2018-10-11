class call(object):
	iD=0
	def __init__(self,name,number,time,reason):
		self.name=name
		self.number=number
		self.time=time
		self.reason=reason
	def display(self):
		print('{} {} {} {} {}'.format(call.iD,self.name,self.number,self.time,self.reason))
		return self

class callcenter(call):
	calllog = []
	def __init__(self,name):
		self.name=name
	def add_call(self, arg):
		callcenter.calllog.append(arg)
		return self
	def pickup(self):
		callcenter.calllog.pop(0)
		return self
	def display(self):
		for i in callcenter.calllog:
			i.display()
		return self
call1=call('dave', 123, '12:00', 'complain')
call2=call('brock', 123, '11:00', 'complain')
call3=call('chris', 123, '9:00', 'happy')

callcenter('main').add_call(call1).add_call(call2).pickup().display()

		
		
		