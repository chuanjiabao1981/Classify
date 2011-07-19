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
import config

class VideoTopicShow:
	def GET(self,topic_id):
		topic 		= find_video_topic_by_id(topic_id)
		member_name	=	""
		member		= get_member_by_name('飞龙在天')
		replies		= get_reply_by_topic_id(topic_id) 
		hit_video_topic_by_topic_id(topic_id)
		try: 
			return template_desktop.get_template('video_topic2.html').render(topic=topic,member=member,replies=replies)
		except:
			return exceptions.html_error_template().render()


	def POST(self,topic_id):
		t			= {}
		t["error"]		= None
		t["member"]		= get_member_by_name('飞龙在天')
		t["topic"]		= find_video_topic_by_id(topic_id)
		reply_to_topic(web.input(),t["member"],t["topic"])
		t["replies"]		= get_reply_by_topic_id(topic_id)
		if t["error"]:
			return template_desktop.get_template('video_topic2.html').render(**t)
		else:
			return web.seeother('/videotopic/'+topic_id)

class NewVideoTopic:
	def GET(self,node_url_name):
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		try: 
			return template_desktop.get_template('new_video.html').render(node=node,site=config.site)
		except:
			return exceptions.html_error_template().render()

