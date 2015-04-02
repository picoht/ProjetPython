class Activite : 

	def __init__(self, actCode, actLib, equipementId):
		""" 
		classe activite 
		""" 
		self.equipementId = equipementId
		self.actCode = actCode
		self.actLib = actLib

	def get_EquipementId(self) : 
		return str(self.equipementId)

	def get_actCode(self) : 
		return str(self.actCode)

	def get_actLib(self) : 
		return str(self.actLib)


	def set_EquipementId(self, t) : 
		self.equipementId = t

	def set_actCode(self, t) : 
		self.actCode = t 

	def set_actLib(self, t) : 
		self.actLib = t 

