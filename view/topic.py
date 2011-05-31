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
import config



urls = (
    '/topic/(.*)','TopicShow',
    '/newtopic/(.*)','NewTopic'
)

app = web.application(urls, globals())


template_desktop = TemplateLookup(directories		=[ os.path.join(os.path.dirname(__file__),'template',config.template_desktop_path),
							   os.path.join(os.path.dirname(__file__),'template','portion')
							 ],
				  module_directory	= os.path.join(os.path.dirname(__file__),'..','tmp'),
				  output_encoding       ='utf-8', 
				  encoding_errors	='replace',
				  input_encoding	='utf-8'
				 );

######上边的东东 必须重启uwsgi才能生效##########
######下边的东东 不需要重启uwsgi就能生效########

class NewTopic:
	def GET(self,node_url_name):
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		try: 
			return template_desktop.get_template('new_topic.html').render(node=node,site=config.site)
		except:
			return exceptions.html_error_template().render()
	def POST(self,node_url_name):
		member_name	=	""
		node		= get_node_by_url_name(node_url_name)
		member		= get_member_by_name(member_name)
		topic		= add_new_topic(node,member, 
						web.input().title,
						web.input().video,
						web.input().content)  
		web.seeother('/newtopic/%s'%(node.name))  



class TopicShow:
	def GET(self,topic_id):
		topic 		= find_topic_by_id(topic_id)
		member_name	=	""
		member		= get_member_by_name(member_name)
		replies		= get_reply_by_topic_id(topic_id)

		return template_desktop.get_template('topic.html').render(topic=topic,member=member,replies=replies)
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
