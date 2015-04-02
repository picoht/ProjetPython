class Installation : 

	def __init__(self, insNumeroInstall, insNom, insCodePostal, comLib, insLibelleVoie, longitude, latitude):
		""" 
		classe Installation
		""" 
		self.insNom = insNom
		self.insNumeroInstall = insNumeroInstall
		self.comLib = comLib
		self.insCodePostal = insCodePostal
		self.insLibelleVoie = insLibelleVoie
		self.longitude = longitude
		self.latitude = latitude

	def get_insNumeroInstall(self) : 
		return str(self.insNumeroInstall)

	def get_insNom(self) : 
		return str(self.insNom)

	def get_comLib(self) : 
		return str(self.comLib)

	def get_insCodePostal(self) : 
		return str(self.insCodePostal)

	def get_insLibelleVoie(self) : 
		return str(self.insLibelleVoie)

	def get_longitude(self) : 
		return str(self.longitude) 

	def get_latitude(self) : 
		return str(self.latitude) 


	def set_insNumeroInstall(self, t) : 
		self.insNumeroInstall = t

	def set_insNom(self, t) : 
		self.insNom = t 

	def set_comLib(self, t) : 
		self.comLib = t 

	def set_insCodePostal(self, t) : 
		self.insCodePostal = t 

	def set_insLibelleVoie(self, t) : 
		self.insLibelleVoie = t 

	def set_longitude(self, t) : 
		self.longitude = t 

	def set_latitude(self, t) : 
		self.latitude = t 	