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
import config
from template import template_desktop
from util.member_tools import *



urls = (
    '/go/(.*)','NodeList'
)

app = web.application(urls, globals())


class NodeList:

	def DealVideo(self,node_url_name):
		t			= {}
		t["node"]		= get_node_by_url_name(node_url_name)
		t["video_list"]		= find_latest_video_topics_in_the_node(t["node"]) # find_video_topic_by_id(t["node"]._id)
		t["file"]		= "video_list.html"
		print t["node"]._id
		print t["video_list"].count()
		print node_url_name
		try: 
			return template_desktop.get_template('video_node.html').render(**t)
		except:
			return exceptions.html_error_template().render()

	
	@get_user_info(web)
	def GET(self,node_url_name):
		return self.DealVideo(node_url_name)
		member_name 	= ""
		member 		= get_member_by_name(member_name)

		node		= get_node_by_url_name(node_url_name)
		can_create	= True
		is_member	= True
		latest		= find_all_node_topic_by_node_url_name(node_url_name)

		try: 
			return template_desktop.get_template('video_node.html').render(node=node,can_create=can_create,is_member=is_member,latest=latest,member=self.member)
		except:
			return exceptions.html_error_template().render()

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
