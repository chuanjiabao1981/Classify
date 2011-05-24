# coding=utf-8
import web
import os
from model.model  import *
from model.member import *
from model.node   import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
import config



urls = (
    '/newtopic/(.*)','NewTopic'
)

app = web.application(urls, globals())


template_desktop = TemplateLookup(directories		=[ os.path.join(os.path.dirname(__file__),'template',config.template_desktop_path)],
				  module_directory	= os.path.join(os.path.dirname(__file__),'..','tmp'),
				  output_encoding       ='utf-8', 
				  encoding_errors	='replace',
				  input_encoding	='utf-8'
				 );


class NewTopic:
	def GET(self,node_url_name):
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		try: 
			return template_desktop.get_template('new_topic.html').render(node=node,site=config.site)
		except:
			return exceptions.html_error_template().render()
	def POST(self,node_url_name):
		node		= get_node_by_url_name(node_url_name)
		member		= get_member_by_name(member_name)
		topic		= connection.Topic()
		topic.title	= web.input().title
		topic.content	= web.input().content
		topic


application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
