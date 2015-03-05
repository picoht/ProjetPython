import sqlite3

class dataBase : 


	def __init__(self):
		print("Base initialisée")

	def createBase(self): 

		conn = sqlite3.connect('installations.db')

		c = conn.cursor()

		c.execute("DROP TABLE IF EXISTS installations")
		c.execute('''CREATE TABLE installations
		             (numeroIns integer, nomIns text,code postal text, commune text, adresse text, longitude integer, latitude integer)''')

		conn.commit()
		conn.close()

		conn = sqlite3.connect('equipements.db')

		c = conn.cursor()

		c.execute("DROP TABLE IF EXISTS equipements")
		c.execute('''CREATE TABLE equipements
		             (numeroEqu integer, nomEqu text, numeroIns integer)''')

		conn.commit()
		conn.close()

		conn = sqlite3.connect('activites.db')

		c = conn.cursor()

		c.execute("DROP TABLE IF EXISTS activites")
		c.execute('''CREATE TABLE activites
		             (numeroAct integer, nomAct text, numeroEqu integer)''')

		conn.commit()
		conn.close()

	def insertActivite(self, actCode, actLib, equipementId): 

		conn = sqlite3.connect('activites.db')

		c = conn.cursor()

		c.execute('''INSERT INTO activites 
  			  VALUES ({}, {}, {]})'''.format(actCode, actLib, equipementId))

		conn.commit()
		conn.close()

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
		conn = sqlite3.connect('activites.db')

		c = conn.cursor()

		for row in c.execute("SELECT * FROM activites ORDER BY numeroAct"):
			print(row)

		conn.close()

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
