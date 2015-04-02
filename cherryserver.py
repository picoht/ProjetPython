import cherrypy
import json
import service.dataBase as db 
import modele.activite as activite
import modele.equipement as equipement
import modele.installation as installation

from mako.template import Template
from mako.lookup import TemplateLookup 

lookup = TemplateLookup(directories=[""]) 

base = db.dataBase() 
base.createBase()


with open('ressources/activite.json') as data_file:    
    data = json.load(data_file)


for item in data["data"]: 
    base.insertActivite(activite.Activite(item["ActCode"], item["ActLib"], item["EquipementId"]))

base.commit()

with open('ressources/equipement.json') as data_file:    
    data = json.load(data_file)

for item in data["data"]: 
    base.insertEquipement(equipement.Equipement(item["EquipementId"], item["EquNom"].replace('"', "'"), item["InsNumeroInstall"]))

base.commit()

with open('ressources/installation.json') as data_file:    
    data = json.load(data_file)

for item in data["data"]: 
    base.insertInstallation(installation.Installation(item["InsNumeroInstall"], item["InsPartLibelle"],  item["InsCodePostal"], item["ComLib"], item ["InsLieuDit"], item["Longitude"], item["Latitude"]))

base.commit()


class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        view = Template(filename="template.html", lookup=lookup)

        base2 = db.dataBase() 
        listCom = base2.liste_installation(); 
        listAct = base2.liste_activite(); 

        return view.render(
            com = listCom, 
            act = listAct, 
            rows=[], 
            ths=[],
            titre = "rechercher une activite ou une commune"
        )        


    @cherrypy.expose
    def show_activites(self):
        """
        Exposes the service at localhost:8080/show_activites/
        """
        base2 = db.dataBase() 
        results = base2.selectActivites()

        view = Template(filename="template.html", lookup=lookup)

        return view.render(
            com = [],
            act = [],
            rows=[[activite.get_actCode(),activite.get_actLib(),activite.get_EquipementId()] for activite in results],
            ths = ["numero de l'activite", "nom de l'activite", "numero de l'equipement"],
            titre = "affichage des activites"
        )            

    @cherrypy.expose
    def show_equipements(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        base2 = db.dataBase() 
        results = base2.selectEquipements()

        view = Template(filename="template.html", lookup=lookup)

        return view.render(
            com = [],
            act = [],
            rows=[[equipement.get_EquipementId(), equipement.get_equNom(), equipement.get_insNumeroInstall()] for equipement in results],
            ths = ["numero de l'équiment", "nom de l'equipement", "numero de l'installation"],
            titre = "affichage des equipememts"
        )    

    @cherrypy.expose
    def show_installations(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        base2 = db.dataBase() 
        results = base2.selectInstallations()

        view = Template(filename="template.html", lookup=lookup)

        return view.render(
            com = [],
            act = [],
            rows=[[installation.get_insNumeroInstall(), installation.get_insNom, installation.get_comLib(), installation.get_insCodePostal(), installation.get_longitude(), installation.get_latitude()] for installation in results],
            ths = ["numero installation", " nom de l'installation", "commune", "code postal", " longitude", "latitude"],
            titre = "affichage des installations"
        )    

    @cherrypy.expose
    def requete(self, commune, activite): 

        base2 = db.dataBase() 

        view = Template(filename="template.html", lookup=lookup)
        

        if activite == "all" and commune == "all" : 
            results = base2.selection_all()
            titres = ["activite", "ville", "equipement", "latitude", "longitude"]
            nom = "recherche des activites dans toutes les communes " 
        elif commune == "all": 
            results = base2.selection_act(activite) 
            titres = ["commune", "equipement", "latitude", "longitude"]
            nom = "recherche des communes où on peut faire l'activité :" + activite 
        elif activite == "all":
            results = base2.selection_ins(commune)
            titres = ["activite", "equipement", "latitude", "longitude"]
            nom = "recherche des activites dans la commune de " + commune 
     
        else: 
            results = base2.selection_act_ins(activite, commune)
            titres = ["equipement", "latitude", "longitude"]
            nom = "recherche des equipements de " + activite + " dans la commune de " + commune 

        return view.render(
            com = [],
            act = [],
            rows=results, 
            ths = titres,
            titre = nom
        )


cherrypy.quickstart(WebManager())