# coding=utf-8
import web
import os
from model.video import *
from model.member import *
from model.node   import *


class UploadVideo:
	def POST(self):
		member 		= get_member_by_name("")
		node		= get_node_by_url_name("")
		video		= add_a_new_video(node,member,web.input())
		return video
		

