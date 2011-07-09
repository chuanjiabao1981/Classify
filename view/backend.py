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

Backend_File ={'main':'backend_classify.html',
	       'classify':'backend_classify.html'}
class Backend:
	def GET(self,arg):
		node_url_name	= ""
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		
		if not arg in Backend_File:
			return web.notfound('这个真没有');
		admin_file	= Backend_File[arg]

		try: 
			return  template_desktop.get_template('backend.html').render(node=node,site=config.site,admin_file=admin_file)

		except:
			return exceptions.html_error_template().render()



