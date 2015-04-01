import sqlite3
import modele.activite as act
import modele.equipement as equ
import modele.installation as inst

class dataBase : 



	def __init__(self):
		
		self.conn = sqlite3.connect('Bd.db')

		self.c = self.conn.cursor()

		print("Base initialisée")

	def createBase(self): 

		

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

		print(activite.get_actCode(), activite.get_actLib(), activite.get_EquipementId())


		if activite.get_actCode() == "None" : 
			activite.set_actCode(0)
	
		if activite.get_actLib() == "None" : 
			activite.set_actLib("null")

		print(activite.get_actCode(), activite.get_actLib(), activite.get_EquipementId())

		self.c.execute('''INSERT INTO activites VALUES ({}, "{}", {})'''.format(activite.get_actCode(), activite.get_actLib(), activite.get_EquipementId()))


	def insertInstallation(self, installation): 

		if installation.get_insCodePostal() == "None" : 
			installation.set_insCodePostal("0")

		self.c.execute('''INSERT INTO installations VALUES ({}, "{}", {}, "{}", "{}", {}, {})'''.format
				(installation.get_insNumeroInstall(), installation.get_insNom(), installation.get_insCodePostal(), installation.get_comLib(), installation.get_insLibelleVoie(), installation.get_longitude(), installation.get_latitude()))




	def insertEquipement(self, equipement): 

		self.c.execute('''INSERT INTO equipements VALUES ({}, "{}", {})'''.format
			(equipement.get_EquipementId(), equipement.get_equNom(), equipement.get_insNumeroInstall()))


	def selectActivites(self): 

		items = self.c.execute("SELECT * FROM activites ORDER BY numeroAct")

		activites = []
		for activite in items: 

			activites.append(act.Activite(activite[0],activite[1], activite[2]))

		return activites


	def selectEquipements(self): 

		items = self.c.execute("SELECT * FROM equipements ORDER BY numeroEqu")

		equipements = []

		for equipement in items: 

			equipements.append(equ.Equipement(equipement[0], equipement[1], equipement[2]))

		return equipements

	def selectInstallations(self): 

		items = self.c.execute("SELECT * FROM installations ORDER BY numeroIns")
			
		installations = []

		for installation in items: 
			installations.append(inst.Installation(installation[0], installation[1], installation[2], installation[3], installation[4], installation[5], installation[6]))

		return installations

	def commit(self):
		self.conn.commit()

