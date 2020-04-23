import webapp2
import jinja2
import os

import requests_toolbelt.adapters.appengine

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('templates/home.html')
        self.response.write(template.render())

requests_toolbelt.adapters.appengine.monkeypatch()
app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)