#coding=utf-8
from model.security import *
from model.member import *
from model.default import *
##获取用户信息
def get_user_info(web):
	def __inner_wrapper(method):
		def __f(self,*a,**n):
			if not 'auth' in web.cookies():
				self.member = None
				return method(self,*a,**n)
			de	=	dencrypt_data(web.cookies().auth)
			user	= 	parse_auth(de)
			if not user:
				self.member = None
				return method(self,*a,**n)
			self.member	=	get_member_by_name(user["name"])
			if not self.member :
				self.member = None
				return method(self,*a,**n)
			print user["password"]
			print self.member.password
			if not (user["password"] == self.member.password):
				self.member = None
				return method(self,*a,**n)
			##TODO::log some info
			return method(self,*a,**n)
		return __f
	return __inner_wrapper

##检查用户是否loggin
def check_user_login(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,*a,**n):
			if self.member == None or self.member.status == MemberStatus.block:
				return web.seeother(redirect_path)
			print self.member.authority
			print self.member.status
			return method(self,*a,**n)
		return __f
	return __inner_wrapper
			

			
