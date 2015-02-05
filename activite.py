class Activite : 

	def __init__(self, equipementId, equActiviteSalleSpe, equActivitePratique, equActivitePraticable, comLib, actCode, actNivLib, comInsee, actLib, equNbEquIdentique):
		self.equipementId = equipementId
		self.equActiviteSalleSpe = equActiviteSalleSpe
		self.equActivitePratique = equActivitePratique
		self.equActivitePraticable = equActivitePraticable
		self.comLib = comLib
		self.actCode = actCode
		self.actNivLib = actNivLib
		self.comInsee = comInsee
		self.actLib = actLib
		self.equNbEquIdentique = equNbEquIdentique

	def get_EquipementId(self) : 
		return str(self.equipementId)

	def get_equActiviteSalleSpe(self):
		return str(self.equActiviteSalleSpe) 

	def get_equActivitePratique(self) : 
		return str(self.equActivitePratique)

	def get_equActivitePraticable(self) : 
		return str(self.equActivitePraticable)

	def get_comLib(self) : 
		return str(self.comLib)

	def get_actCode(self) : 
		return str(self.actCode)

	def get_actNivLib(self) : 
		return str(self.actNivLib)

	def get_comInsee(self) : 
		return str(self.comInsee)

	def get_actLib(self) : 
		return str(self.actLib)

	def get_equNbEquIdentique(self) :
		return str(self.equNbEquIdentique) 



	def set_EquipementId(self, t) : 
		self.equipementId = t

	def set_equActiviteSalleSpe(self, t):
		self.equActiviteSalleSpe = t  

	def set_equActivitePratique(self, t) : 
		self.equActivitePratique = t 

	def set_equActivitePraticable(self, t) : 
		self.equActivitePraticable = t 

	def set_comLib(self, t) : 
		self.comLib = t 

	def set_actCode(self, t) : 
		self.actCode = t 

	def set_actNivLib(self, t) : 
		self.actNivLib = t

	def set_comInsee(self, t ) : 
		self.comInsee = t 

	def set_actLib(self, t) : 
		self.actLib = t 

	def set_equNbEquIdentique(self, t) :
		self.equNbEquIdentique = t 

