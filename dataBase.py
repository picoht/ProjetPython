import sqlite3


Class 
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
c.execute('''CREATE TABLE equipements
             (numeroAct integer, nomAct text, numeroEqu integer)''')

conn.commit()
conn.close()



