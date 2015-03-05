import json
import installation
import equipement
import activite
from pprint import pprint

with open('data.paysdelaloire.fr.activite.json') as data_file:    
    data = json.load(data_file)

   

for item in data["actCode"] : 


