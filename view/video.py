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
		self.content_length_up 		=	2000
		self.content_length_down	=	3

		self.inputerror_str			=	{}
		self.inputerror_str[0]		=	None
		self.inputerror_str[1]		=	u'八个呀路!'
		self.inputerror_str[2]		=	u'输入字符不能超过'+unicode(str(self.content_length_up))+u'个字符'
		self.inputerror_str[3]		=	u'写点啥,别空着!'
		self.inputerror_str[4]		=	u'写的太少了、再写点。至少写'+unicode(str(self.content_length_down))+u'个字符'

	def InputCheck(self):
		if not 'content' in web.input():
			return (False,1)
		if len(web.input().content) > self.content_length_up:
			return (False,2)
		if len(web.input().content.strip()) == 0:
			return (False,3)
		if len(web.input().content.strip()) < self.content_length_down:
			return (False,4)
		return (True,0)
			
	@get_videotopic_info(web,"/")
	@get_user_info(web)
	@get_reply_info(web)
	def GET(self,topic_id):
		_t			= {}
		_t["topic"]		= self.topic
		_t["member"]		= self.member
		_t["replies"]		= self.replies
		_t["video"]		= True
		_t["url_prefix"]	= VideoTopicShow.URL_PREFIX
		try: 
			hit_video_topic_by_topic_id(topic_id)
			return template_desktop.get_template('video_topic2.html').render(**_t)
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
			return template_desktop.get_template('video_topic2.html').render(**_t)
		else:
			add_new_reply_to_topic(self.topic,self.member,web.input())
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
