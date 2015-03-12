import sqlite3

class dataBase : 



	def __init__(self):
		print("Base initialisée")
		self.conn = sqlite3.connect('Bd.db')

		self.c = self.conn.cursor()

	def createBase(self): 

		

		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations
		             (numeroIns integer, nomIns text,code postal text, commune text, adresse text, longitude integer, latitude integer)''')

		self.c.execute("DROP TABLE IF EXISTS equipements")
		self.c.execute('''CREATE TABLE equipements
		             (numeroEqu integer, nomEqu text, numeroIns integer)''')

		self.c.execute("DROP TABLE IF EXISTS activites")
		self.c.execute('''CREATE TABLE activites
		             (numeroAct integer, nomAct text, numeroEqu integer)''')

		self.conn.commit()


	def insertActivite(self, actCode, actLib, equipementId): 

		self.c.execute("INSERT INTO activites VALUES (?, ?, ?)",(actCode, actLib, equipementId))

		self.conn.commit()

	def insertInstallation(self, insNom, insNumeroInstall, comLib, insCodePostal, insLibelleVoie, longitude, latitude): 

		conn = sqlite3.connect('installations.db')

		c = conn.cursor()

		c.execute('''INSERT INTO installations 
  			  VALUES ({}, {}, {}, {}, {}, {}, {})'''.format(insNumeroInstall, insNom, insCodePostal, comLib, insLibelleVoie, longitude, latitude))

		conn.commit()
		conn.close()


	def insertEquipement(self, equipementId, equNom, insNumeroInstall): 

		conn = sqlite3.connect('equipements.db')

		c = conn.cursor()

		c.execute('''INSERT INTO equipements
  			  VALUES ({}, {}, {})'''.format(equipementId, equNom, insNumeroInstall))

		conn.commit()
		conn.close()

	def selectActivites(self): 

		for row in self.c.execute("SELECT * FROM activites ORDER BY numeroAct"):
			print(row)


	def selectEquipements(self): 
		conn = sqlite3.connect('equipements.db')

		c = conn.cursor()

		for row in c.execute("SELECT * FROM equipements ORDER BY numeroEqu"):
			print(row)

		conn.close()


	def selectInstallations(self): 
		conn = sqlite3.connect('installations.db')

		c = conn.cursor()

		for row in c.execute("SELECT * FROM installations ORDER BY numeroIns"):
			print(row)

		conn.close()
