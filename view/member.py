# coding=utf-8
import web
import os
import json
import config
import re
from model.model  import *
from model.member import *
from PIL import Image
from util.member_tools import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop



class SetAvatar:
	def __init__(self):
		self.cookies = web.cookies()
	def post_arg_check(self):
		a = ['x1','y1','x2','y2','img']
		for i in a:
			if not i in web.input():
				##TODO:some log
				return False
		if not (web.input().x1.isdigit() and web.input().y1.isdigit() and web.input().x2.isdigit() and web.input().y2.isdigit()):
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
		crop_im = im.resize((config.avatar.origin_width,config.avatar.origin_height),Image.ANTIALIAS).crop((x1,y1,x2,y2))  #.save('/home/work/tmp/1.jpg')
		
		#保存各种大小
		for i in config.avatar.save_size:
			try:
				
				crop_im.resize(config.avatar.save_size[i],Image.ANTIALIAS).save(des_path + '/'+ str(self.member._id)+'_'+i+'.jpg',quality=100)
			except IOError,a:
				##TODO:some log
				return False
		return True

	def GET(self,user_id):
		t = {}
		t["admin_file"] =  'backend_member_avatar.html'
		return template_desktop.get_template('backend.html').render(**t)
	@get_user_info(web)
	def POST(self):
		print web.input()
		print self.member
		r = {}
		r["status"] = False
		if self.member == None or self.member.status == MemberStatus.block:
			r["err"] = "请登录后再保头像"
			return json.dumps(r)
		if not self.post_arg_check():
			r["err"] = "上传头像错误"
			return json.dumps(r)
		if not self.resize_avatar_img():
			r["err"] = "上传头像错误"
			return json.dumps(r)
		
		r["status"] =True
		r["err"]    ="头像保存成功"
		print self.member
		return 	json.dumps(r)

class SetAvatarBackend(SetAvatar):
	def __init__(self):
		SetAvatar.__init__(self)
	def GET(self,member_id):
		t = {}
		t["admin_file"]    =  'backend_member_avatar.html'
		t["admin_title"]   =  'aaa'
		t["member_id"]	   =   member_id
		return template_desktop.get_template('backend.html').render(**t)

AccoutSettingList = (
			(0,'/account/setting',"基本信息"),
			(1,'/account/setting/security',"密码管理"),
			(2,'/account/setting/avatar',"头像设置")
		    )
class AccountSetting:

	@get_user_info(web)
	@check_user_login(web,"/")
	def GET(self):
		_t = {}
		_t["settings"] 		= AccoutSettingList 
		_t["select_setting"]	= 0 
		_t["member"]		= self.member
		return template_desktop.get_template('account_setting.html').render(**_t)
