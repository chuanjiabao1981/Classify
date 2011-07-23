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
from template import template_desktop
import config
from util.member_tools import *

class MainPage:
	def __init__(self):
		self.cookies = web.cookies()

	@get_user_info(web)
	@check_user_login(web,"/login")
	def GET(self):
		member_name 	= ""
		#member 		= get_member_by_name(member_name)
		#node		= get_node_by_url_name(node_url_name)
		try: 
			return template_desktop.get_template('index.html').render(site=config.site)
		except:
			return exceptions.html_error_template().render()

