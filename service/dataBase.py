import sqlite3
import modele.activite as act
import modele.equipement as equ
import modele.installation as inst

class dataBase : 



	def __init__(self):
		"""
   		connection à la base de donnees 
    	"""
		self.conn = sqlite3.connect('Bd.db')

		self.c = self.conn.cursor()

		print("Base initialisée")

	def createBase(self): 
		"""
   		creation des tables activites, installations et equipements
    	"""
		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations
		             (numeroIns integer, nomIns varchar,code postal integer, commune varchar, adresse varchar, longitude integer, latitude integer)''')

		self.c.execute("DROP TABLE IF EXISTS equipements")
		self.c.execute('''CREATE TABLE equipements
		             (numeroEqu integer, nomEqu varchar, numeroIns integer)''')

		self.c.execute("DROP TABLE IF EXISTS activites")
		self.c.execute('''CREATE TABLE activites
		             (numeroAct integer, nomAct varchar, numeroEqu integer)''')

		self.conn.commit()


	def insertActivite(self, activite): 
		"""
   		insert une activite
    	"""
		if activite.get_actCode() == "None" : 
			activite.set_actCode(0)
	
		if activite.get_actLib() == "None" : 
			activite.set_actLib("null")

		if activite.get_actCode() != "0" :  
			self.c.execute('''INSERT INTO activites VALUES ({}, "{}", {})'''.format(activite.get_actCode(), activite.get_actLib(), activite.get_EquipementId()))


	def insertInstallation(self, installation): 
		"""
   		insert une installation
    	"""

		if installation.get_insCodePostal() == "None" : 
			installation.set_insCodePostal("0")

		self.c.execute('''INSERT INTO installations VALUES ({}, "{}", {}, "{}", "{}", {}, {})'''.format
				(installation.get_insNumeroInstall(), installation.get_insNom(), installation.get_insCodePostal(), installation.get_comLib(), installation.get_insLibelleVoie(), installation.get_longitude(), installation.get_latitude()))




	def insertEquipement(self, equipement): 
		"""
   		insert un equipement
    	"""
		self.c.execute('''INSERT INTO equipements VALUES ({}, "{}", {})'''.format
			(equipement.get_EquipementId(), equipement.get_equNom(), equipement.get_insNumeroInstall()))


	def selectActivites(self): 
		"""
   		recupere toutes les activites
    	"""

		items = self.c.execute("SELECT * FROM activites ORDER BY numeroAct")

		activites = []
		for activite in items: 

			activites.append(act.Activite(activite[0],activite[1], activite[2]))

		return activites


	def selectEquipements(self): 
		"""
   		recupere tous les equipements 
    	"""
		items = self.c.execute("SELECT * FROM equipements ORDER BY numeroEqu")

		equipements = []

		for equipement in items: 

			equipements.append(equ.Equipement(equipement[0], equipement[1], equipement[2]))

		return equipements

	def selectInstallations(self): 
		"""
   		recupere toutes les activites
    	"""
		items = self.c.execute("SELECT * FROM installations ORDER BY numeroIns")
			
		installations = []

		for installation in items: 
			installations.append(inst.Installation(installation[0], installation[1], installation[2], installation[3], installation[4], installation[5], installation[6]))

		return installations

	def liste_installation(self):
		"""
   		liste toutes les installations 
    	"""
		results = self.c.execute("SELECT DISTINCT commune FROM installations ORDER BY commune")

		insts = []
		insts.append("all")

		for inst in results:
			insts.append(inst[0])

		return insts

	def liste_activite(self):
		"""
   		liste toutes les activites 
    	"""
		results = self.c.execute("SELECT DISTINCT nomAct FROM activites ORDER BY nomAct")

		acts= []
		acts.append("all")

		for act in results: 
			acts.append(act[0])

		return acts

	def selection_act(self,activite):
		"""
   		selectionne tout les equipements des communes par rapport a une activite
    	"""
		return self.c.execute("SELECT i.commune, e.nomEqu, i.longitude, i.latitude FROM activites a, installations i, equipements e where i.numeroIns = e.numeroIns and e.numeroEqu = a.numeroEqu and a.nomAct = '{}' ".format(activite))

	def selection_ins(self,commune):
		"""
   		selectionne tout les equipements des activites par rapport a une commune 
    	"""
		return self.c.execute("SELECT a.nomAct, e.nomEqu, i.longitude, i.latitude FROM activites a, installations i, equipements e where i.numeroIns = e.numeroIns and e.numeroEqu = a.numeroEqu and i.commune = '{}' ".format(commune))


	def selection_act_ins(self,activite, commune):
		"""
   		selectionne tout les equipements par rapport a une commune et une activite 
    	"""
		return self.c.execute("SELECT e.nomEqu, i.longitude, i.latitude FROM activites a, installations i, equipements e where i.numeroIns = e.numeroIns and e.numeroEqu = a.numeroEqu and i.commune = '{}' and a.nomAct = '{}' ".format(commune, activite))

	def selection_all(self):
		"""
   		affiche tous les equipemnts de toutes la activites
    	"""
		return self.c.execute("SELECT a.nomAct, i.commune, e.nomEqu, i.longitude, i.latitude FROM activites a, installations i, equipements e where i.numeroIns = e.numeroIns and e.numeroEqu = a.numeroEqu ") 

	def commit(self):
		"""
   		realise un commit
    	"""
		self.conn.commit()

