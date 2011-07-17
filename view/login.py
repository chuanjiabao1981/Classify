# coding=utf-8
import web
import os
from pyDes import *
from model.security import *

class Login:
	def GET(self):
		data = "Please encrypt my data你好草"
		if 'auth' in web.cookies():
			return dencrypt_data(web.cookies().auth)
		web.setcookie('auth', encrypt_data(data), 360)	
		return web.cookies()
