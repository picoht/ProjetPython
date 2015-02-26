class Equipement : 

	def __init__(self, comInsee, equipementId, equNom, insNumeroInstall): 
		self.comInsee = comInsee
		self.equipementId = equipementId
		self.equNom = equNom
		self.insNumeroInstall = insNumeroInstall

	def get_EquipementId(self) : 
		return str(self.equipementId)

	def get_comInsee(self) : 
		return str(self.comInsee)

	def get_equNom(self) : 
		return str(self.equNom)

	def get_insNumeroInstall(self) : 
		return str(sefl.insNumeroInstall)

	def set_EquipementId(self, t) : 
		self.equipementId = t

	def set_comInsee(self, t) : 
		self.comInsee = t 

	def set_equNom(self, t) : 
		self.equNom = t 

	def set_insNumeroInstall(self, t) : 
		self.insNumeroInstall = t
		
	