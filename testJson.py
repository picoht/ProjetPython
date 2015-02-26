import json
import installation
import equipement
import activite
from pprint import pprint

with open('data.paysdelaloire.fr.activite.json') as data_file:    
    data = json.load(data_file)


i = 0 

while i < 10 :
	i += 1  
	print(data["data"][i]["ActCode"])
	print(data["data"][i]["ActLib"]) 
	print(data["data"][i]["EquipementId"]) 

