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
from util.topic_tools import *

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
	URL_PREFIX='/topic/'
	@get_topic_info(web,"/")
	@get_user_info(web)
	@get_reply_info(web)
	def GET(self,topic_id):
		_t		= {}

		_t["topic"]		= self.topic
		_t["member"]		= self.member
		_t["replies"]		= self.replies
		_t["video"]		= False
		_t["url_prefix"]	= TopicShow.URL_PREFIX
		
		hit_topic_by_topic_id(topic_id)
		try :
			return template_desktop.get_template('video_topic2.html').render(**_t)
		except:
			return exceptions.html_error_template().render()

	@get_topic_info(web,"/")
	@get_user_info(web)
	@check_user_login(web,"/login")
	def POST(self,topic_id):
		add_new_reply_to_topic(self.topic,self.member,web.input())
		web.seeother('%s%s'%(TopicShow.URL_PREFIX,topic_id))

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
