import json
import dataBase as db 
from pprint import pprint

with open('data.paysdelaloire.fr.activite.json') as data_file:    
    data = json.load(data_file)

base = db.dataBase()
base.createBase()

for item in data["actCode"] : 
	base.insertActivite(item["actCode"], item["actLib"], item["equipementId"])

base.selectActivites()