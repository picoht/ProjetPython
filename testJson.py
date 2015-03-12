import json
import dataBase as db 
from pprint import pprint

with open('data.paysdelaloire.fr.activite.json') as data_file:    
    data = json.load(data_file)

base = db.dataBase()
base.createBase()
i = 0 

for item in data["data"] : 
	i+= 1 
	base.insertActivite(item["ActCode"], item["ActLib"], item["EquipementId"])
	print("insere !! " + str(i))

base.selectActivites()

