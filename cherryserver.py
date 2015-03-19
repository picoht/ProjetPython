import cherrypy
import json
import service.dataBase as db 

base = db.dataBase() 
base.createBase()


with open('ressources/activite.json') as data_file:    
    data = json.load(data_file)

base.insertActivite(data["data"])

with open('ressources/equipement.json') as data_file:    
    data = json.load(data_file)

base.insertEquipement(data["data"])

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
        return base.selectActivites() 

    @cherrypy.expose
    def show_equipements(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        return base.selectEquipements()

    @cherrypy.expose
    def show_installations(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        return base.selectInstallations()

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