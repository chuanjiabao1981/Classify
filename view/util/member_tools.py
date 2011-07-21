#coding=utf-8
from model.security import *
from model.member import *
##check 用户登录
def check_user_login(web):
	def __inner_wrapper(method):
		def __f(self,*a,**n):
			if not 'auth' in web.cookies():
				self.member = None
				return web.seeother("/login")
			de   = dencrypt_data(web.cookies().auth)
			user = parse_auth(de)
			if not user:
				self.member = None
				return web.seeother("/login")
			self.member = get_member_by_name(user["name"])
			#print self.member
			if self.member == None:
				return web.seeother("/login")
			return method(self,*a,**n)
		return __f
	return __inner_wrapper

