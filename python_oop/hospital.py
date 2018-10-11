class patient(object):
	"""docstring for patient"""
	def __init__(self,iD,name,allergies,bed_number):
		self.iD=iD
		self.name=name
		self.allergies=allergies
		self.bed_number=0

class hospital(patient):
	patients = []
	pcapacity = 0
	def __init__(self, name):
		self.name = name

	def admit(self, *arg):
		if (hospital.pcapacity>=150):
			print 'Over capacity, Can not admit.'
		else:
			hospital.patients.append(arg)
			print hospital.patients
			hospital.pcapacity+=1
			return self

	def discharge(self,name):
		for a in hospital.patients:
			for i in range(0,len(a)):
				if a[i].name==name:
					hospital.patients.remove(a)
					print a[i].name +" was discharged"
		print hospital.patients
		return self			

patient1=patient(1,'kalvin','none',1)
patient2=patient(2,'malvin','asthma',2)

hospital('main').admit(patient1).admit(patient2).discharge('kalvin')

