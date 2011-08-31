# coding=utf-8
import web
import os
from model.model  import *
from model.member import *
from model.node   import *
from model.topic  import *
from model.video  import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop
from util.member_tools import *
import config


class MainPage:
	def __init__(self):
		self.cookies = web.cookies()

	@get_user_info(web)
	@check_user_login(web,"/login")
	def GET(self):
		member_name 	= ""
		#member 		= get_member_by_name(member_name)
		#node			= get_node_by_url_name(node_url_name)
		t			= {}
		t["video_list"]		= get_latest_video_topic(config.collection_name.Video,None,0,config.page_num)
		t["site"]		= config.site
		t["index_page"]		= True

		try: 
			return template_desktop.get_template('index.html').render(**t)
		except:
			return exceptions.html_error_template().render()

