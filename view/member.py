# coding=utf-8
import web
import os
import json
import config
import re
from model.model  import *
from model.member import *
from PIL import Image

class SetAvatar:
	def __init__(self):
		self.cookies = web.cookies()
	def post_arg_check(self):
		a = ['x1','y1','x2','y2','img']
		for i in a:
			if not i in web.input():
				##TODO:some log
				return False
		if web.input().x1.isdigit() and web.input().y1.isdigit() and web.input().x2.isdigit() and web.input().y2.isdigit():
			## TODO::some log
			return False
		#前缀匹配临时图片目录
		p = re.compile("^"+config.path_setting.tmp_img_root_dir)
		if not p.match(web.input().img):
			##TODO:some log
			return False
		return True
	def resize_avatar_img(self):
		img_file = config.path_setting.html_document_root + web.input().img
		des_path = config.path_setting.html_document_root + config.path_setting.avatar_root_dir
		try:
			im = Image.open(img_file)
		except IOError,a:	
			##TODO:some log
			print a
			return False
		x1	= int(web.input().x1)
		y1      = int(web.input().y1)
		x2	= int(web.input().x2)
		y2	= int(web.input().y2)
		crop_im = im.resize((config.avatar.origin_width,config.avatar.origin_height)).crop((x1,y1,x2,y2))  #.save('/home/work/tmp/1.jpg')
		
		#保存各种大小


	@get_user_info(web)
	def POST(self):
		r = {}
		r["status"] = False
		if self.member == None or self.member.status == MemberStatus.block:
			r["err"] = "请登录后再保存图片"
			return json.dumps(r)
		if not self.post_arg_check():
			r["err"] = "上传错误"
			return json.dumps(r)
		
		a = {}
		a["status"] =True
		return 	json.dumps(a)