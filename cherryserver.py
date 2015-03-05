import cherrypy
import json


data = json.loads(open("data.paysdelaloire.fr.activite.json").read())


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
    def show_all(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        return json.dumps(data)

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