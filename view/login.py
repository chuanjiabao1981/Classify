# coding=utf-8
import web
import os
from template import template_desktop
from pyDes import *
from model.security import *
from model.member import *
from config import cookie

class Login:
	def GET(self):
		try: 
			return template_desktop.get_template('login.html').render()
		except:
			return exceptions.html_error_template().render()

	def POST(self):
		t			= {}
		if not web.input().name.strip(' ').strip('\n'):
			t["error"]	=	u'用户名不能为空'
			return t["error"]
		(status,r)		= verify_login(web.input())
		if not status:
			t["error"]	= r
			return t["error"]
		web.setcookie('auth',r,cookie.period)
		password	= web.input().password
		return "sucess"
		
