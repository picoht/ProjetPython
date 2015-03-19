import json
import service.dataBase as db 
from pprint import pprint

with open('data.paysdelaloire.fr.activite.json') as data_file:    
    data = json.load(data_file)

base = db.dataBase()
base.createBase()

base.insertActivite(data["data"])

base.selectActivites()

