# coding=utf-8
import web
import os
from model.model  import *
from model.member import *
from model.node   import *
from model.video  import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop
from util.member_tools import *
from util.topic_tools  import *

import config

class VideoTopicShow:
	URL_PREFIX = '/videotopic/'
	def __init__(self):
		pass
			
	@get_videotopic_info(web,"/")  	## topic
	@get_user_info(web)		## member	
	@get_reply_info(web)		## replies
	def GET(self,topic_id):
		_t			= {}
		_t["topic"]		= self.topic
		_t["member"]		= self.member
		_t["replies"]		= self.replies
		_t["video"]		= True
		_t["url_prefix"]	= VideoTopicShow.URL_PREFIX
		try: 
			return template_desktop.get_template('topic.html').render(**_t)
		except:
			return exceptions.html_error_template().render()
	

	@get_videotopic_info(web,"/")  		## topic
	@get_user_info(web)	       		## member
	@check_user_login(web,"/login")
	@get_reply_info(web)			## replies
	def POST(self,topic_id):
		_t			= {}
		reply_check		= TopicReplyCheck()		
		_t["error"]		= reply_check.check_input(web.input())
		if _t["error"]:
			_t["topic"]		= self.topic
			_t["member"]		= self.member
			_t["replies"]		= self.replies
			_t["video"]		= True
			_t["url_prefix"]	= VideoTopicShow.URL_PREFIX
			return template_desktop.get_template('topic.html').render(**_t)
		else:
			add_new_reply_to_video(self.topic,self.member,web.input())
			return web.seeother('%s%s'%(VideoTopicShow.URL_PREFIX,topic_id))

class NewVideoTopic:
	@get_user_info(web)
	@check_user_login(web,"/login")
	def GET(self,node_url_name):
		_t		= {}
		node		= get_node_by_url_name(node_url_name)
		_t["node"]	= node
		_t["site"]	= config.site
		if not node:
			return web.seeother("/")
		try: 
			return template_desktop.get_template('new_video.html').render(**_t)
		except:
			return exceptions.html_error_template().render()

class UploadVideo:
	def verifyArgument(self):
		if not "file_path" in web.input() or not 'node_url_name' in web.input():
			if web.ctx.env['HTTP_REFERER']:
				raise web.seeother( web.ctx.env['HTTP_REFERER'])
			else:
				raise web.seeother('/')
		
	@get_user_info(web)
	@check_user_login(web,"400")
	def POST(self):
		###TODO::错误后返回templage
		###TODO::上传之前先验证
		self.verifyArgument()
		node		= get_node_by_url_name(web.input().node_url_name)
		if not node:
			raise web.webapi.HTTPError('400', {},"Crazy Man!")
		video		= add_a_new_video(node,self.member,web.input())
		###TODO::当前的链接
		raise web.seeother('/go/'+node.url)
