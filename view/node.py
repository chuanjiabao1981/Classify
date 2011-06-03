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



urls = (
    '/go/(.*)','NodeList'
)

app = web.application(urls, globals())


class NodeList:
	def GET(self,node_name):
		return "hello world"

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
