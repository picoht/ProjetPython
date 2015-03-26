import cherrypy
import json
import service.dataBase as db 
import modele.activite as activite
import modele.equipement as aquipement
import modele.installation as installation

base = db.dataBase() 
base.createBase()


with open('ressources/activite.json') as data_file:    
    data = json.load(data_file)


for item in data["data"]: 
    base.insertActivite(activite.Activite(item["ActCode"], item["ActLib"], item["EquipementId"]))

with open('ressources/equipement.json') as data_file:    
    data = json.load(data_file)

for item in data["data"]: 
    base.insertEquipement(equipement.Equipement(item["InsNumeroInstall"], item["InsPartLibelle"],  item["InsCodePostal"], item["ComLib"], item ["InsLieuDit"], item["Longitude"], item["Latitude"])))

with open('ressources/installation.json') as data_file:    
    data = json.load(data_file)

base.insertInstallation(data["data"])


class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        return "There are {0} items".format(len(data))

    @cherrypy.expose
    def show_activites(self):
        """
        Exposes the service at localhost:8080/show_activites/
        """
        base2 = db.dataBase() 
        results = base2.selectActivites()

        s = ""

        for row in results:
            s += str(row)
            
        return s

    @cherrypy.expose
    def show_equipements(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        base2 = db.dataBase() 
        results = base2.selectEquipements()

        s = ""

        for row in results:
            s += str(row)
            
        return s

    @cherrypy.expose
    def show_installations(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        base2 = db.dataBase() 
        results = base2.selectInstallations()

        s = ""

        for row in results:
            

        return s

    @cherrypy.expose
    def show(self, id):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        try:
            item = data[int(id)]
        except (IndexError, IOError):
            return "Invalid ID"

        return json.dumps(item)


cherrypy.quickstart(WebManager())