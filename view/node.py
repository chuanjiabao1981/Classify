# coding=utf-8
import web
import os
from model.model  import *
from model.member import *
from model.node   import *
from model.topic  import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
import config
from template import template_desktop



urls = (
    '/go/(.*)','NodeList'
)

app = web.application(urls, globals())


class NodeList:
	def GET(self,node_name):
		try: 
			return template_desktop.get_template('node.html').render()
		except:
			return exceptions.html_error_template().render()

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
