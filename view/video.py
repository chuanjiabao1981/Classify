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

import config

class VideoTopicShow:
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
			
	def GET(self,topic_id):
		topic 		= find_video_topic_by_id(topic_id)
		member_name	=	""
		member		= get_member_by_name('chuanjiabao')
		replies		= get_reply_by_topic_id(topic_id) 
		hit_video_topic_by_topic_id(topic_id)
		try: 
			return template_desktop.get_template('video_topic2.html').render(topic=topic,member=member,replies=replies)
		except:
			return exceptions.html_error_template().render()
	


	def POST(self,topic_id):
		t			= {}
		t["error"]		= None
		##TODO:未登录 用decorator
		t["member"]		= get_member_by_name('chuanjiabao')
		t["topic"]		= find_video_topic_by_id(topic_id)
		if not t["topic"]:
			return web.notfound()
		t["replies"]		= get_reply_by_topic_id(topic_id)
		(status,error_code)	=self.InputCheck()
		t["error"]		= self.inputerror_str[error_code]
		if t["error"]:
			return template_desktop.get_template('video_topic2.html').render(**t)
		else:
			reply_to_topic(web.input(),t["member"],t["topic"])
			return web.seeother('/videotopic/'+topic_id)

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

