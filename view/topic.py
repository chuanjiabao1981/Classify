# coding=utf-8
import web
from model.member import *


urls = (
    '/newtopic/(.*)','NewTopic'
)

app = web.application(urls, globals())

class NewTopic:
	def GET(self,node_name):
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		return member

if __name__ == "__main__":
	app.run()
