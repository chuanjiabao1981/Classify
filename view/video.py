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
		member		= get_member_by_name(member_name)
		#replies	= get_reply_by_topic_id(topic_id) 
		replies		= None
		hit_video_topic_by_topic_id(topic_id)

		return template_desktop.get_template('video_topic2.html').render(topic=topic,member=member,replies=replies)


class NewVideoTopic:
	def GET(self,node_url_name):
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		try: 
			return template_desktop.get_template('new_video.html').render(node=node,site=config.site)
		except:
			return exceptions.html_error_template().render()

