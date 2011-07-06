# coding=utf-8
import web
import os
from model.video  import *
from model.model  import *
from model.member import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop
import config

class Backend:
	def GET(self):
		node_url_name	= ""
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)


		try: 
			return  template_desktop.get_template('backend.html').render(node=node,site=config.site)

		except:
			return exceptions.html_error_template().render()



