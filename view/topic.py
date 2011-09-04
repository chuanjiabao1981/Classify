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
from util.node_tools import *
from util.member_tools import *
from model.reply import *




urls = (
    '/topic/(.*)','TopicShow',
    '/newtopic/(.*)','NewTopic'
)

app = web.application(urls, globals())


class NewTopic:
	@get_node_info(web,"/")
	@get_user_info(web)
	@check_user_login(web,"/")
	def GET(self,node_url_name):
		try: 
			return template_desktop.get_template('new_topic.html').render(node=self.node,site=config.site)
		except:
			return exceptions.html_error_template().render()

	@get_node_info(web,"/")
	@get_user_info(web)
	@check_user_login(web,"/")
	def POST(self,node_url_name):
		topic		= add_a_new_topic(self.node,self.member,web.input())
		return web.seeother('/topic/%s'%(topic._id))  



class TopicShow:
	def GET(self,topic_id):
		_t		= {}
		topic 		= find_topic_by_id(topic_id)
		member_name	=	""
		member		= get_member_by_name(member_name)
		replies		= get_reply_by_topic_id(topic_id) 

		_t["topic"]	= topic
		_t["member"]	= member
		_t["replies"]	= replies
		_t["video"]	= False
		
		hit_topic_by_topic_id(topic_id)
		try :
			return template_desktop.get_template('video_topic2.html').render(**_t)
		except:
			return exceptions.html_error_template().render()
	def POST(self,topic_id):
		topic			= find_topic_by_id(topic_id)
		replyer			= get_member_by_name("")
		reply			= connection.Reply()
		reply_time		= datetime.datetime.now()
		reply.topic_id		= topic._id
		reply.author		= replyer.name
		reply.content		= web.input().content
		reply.content_length	= len(reply.content)
		reply.create_time	= reply_time
		reply.save()
		
		add_new_reply_to_topic(topic._id,reply_time,replyer.name)
		web.seeother('/topic/%s'%(topic_id))

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
