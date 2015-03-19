import sqlite3

class dataBase : 



	def __init__(self):
		
		self.conn = sqlite3.connect('Bd.db')

		self.c = self.conn.cursor()

		print("Base initialisée")

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


	def insertActivite(self, items): 

		for item in items: 
			self.c.execute("INSERT INTO activites VALUES (?, ?, ?)",(item["ActCode"], item["ActLib"], item["EquipementId"])) 

		self.conn.commit() 

	def insertInstallation(self, items): 

		for item in items : 

			print('''INSERT INTO installations VALUES ({}, "{}", {}, "{}", "{}", {}, {})'''.format
				(item["InsNumeroInstall"], int (item["InsPartLibelle"].replace("none",0)),  item["InsCodePostal"], item["ComLib"], item ["InsLieuDit"], item["Longitude"], item["Latitude"]))


			self.c.execute('''INSERT INTO installations VALUES ({}, "{}", {}, "{}", "{}", {}, {})'''.format
				(item["InsNumeroInstall"], int (item["InsPartLibelle"].replace("none",0)) ,  item["InsCodePostal"], item["ComLib"], item ["InsLieuDit"], item["Longitude"], item["Latitude"]))

		self.conn.commit()


	def insertEquipement(self, items): 

		for item in items :
			self.c.execute('''INSERT INTO equipements VALUES ({}, "{}", {})'''.format
				(item["EquipementId"], item["EquNom"].replace('"', "'"), item["InsNumeroInstall"]))

		self.conn.commit()

	def selectActivites(self): 

		return self.c.execute("SELECT * FROM activites ORDER BY numeroAct")


	def selectEquipements(self): 

		return self.c.execute("SELECT * FROM equipements ORDER BY numeroEqu")


	def selectInstallations(self): 

		 return self.c.execute("SELECT * FROM installations ORDER BY numeroIns")
			


