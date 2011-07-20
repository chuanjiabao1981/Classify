#coding=utf-8
from model import *
from default import *
import hashlib
import bson.objectid
from security import *
import json


def get_member_by_id(_id):
	return connection.Member.find_one({"_id":bson.objectid.ObjectId(_id)})	
def get_member_by_name(name):
	return connection.Member.find_one({"name":name})
def get_member_by_email(email):
	return connection.Member.find_one({"email":email})
	
def verify_login(web_info):
	t	=	None
	if '@' in web_info.name:
		t = get_member_by_email(web_info.name)
	else:
		t = get_member_by_name(web_info.name)
	if not t:
		return (False,'这个用户不存在!')
	pp	=	unicode(hashlib.md5(web_info.password.strip(' ').strip('\n')).hexdigest().upper())
	if pp != t.password:
		return (False,'密码错误!!')
	aa	= {'name':t.name,'password':t.password}
	tt	= json.dumps(aa)
	dd	= encrypt_data(tt)
	return (True,dd)

def update_member_info(member_info,web_info):
	t		=	{}
	t['name']	=	web_info.name.strip(' ').strip('\n')
	t['email']	=	web_info.email.strip(' ').strip('\n')
	t['readme']	=	web_info.readme
	t['authority']	=	MemberAuthority.build_authority(web_info)
	if web_info.password.strip(' ').strip('\n') :
		t['password'] = unicode(hashlib.md5(web_info.password.strip(' ').strip('\n')).hexdigest().upper())
	try:
		connection[config.classify_database][config.collection_name.Member].update(
		{'_id':member_info._id},
		{'$set': t }	
		)
	except pymongo.errors.DuplicateKeyError,a:
		if 0 != connection.Member.find({'name':member.name}).count():
			return (False,u"用户名已经存在")
		if 0 != connection.Member.find({'email':member.email}).count():
			return (False,u"Email已经存在")
		return (False,u"错了么")
	return (True,None)

	
def get_all_member():
	return connection.Member.find()

def add_a_member(web_info):
	member		=	connection.Member()
	member.name	=	web_info.name.strip(' ').strip('\n')
	member.email	=	web_info.email.strip(' ').strip('\n')
	member.password	=	unicode(hashlib.md5(web_info.password.strip(' ').strip('\n')).hexdigest().upper())
	member.readme	=	web_info.readme.strip(' ').strip('\n')
	if connection.Member.find().count() == 0:
		member.authority	=	~0l	
	else:
		member.authority	= MemberAuthority.build_authority(web_info)
	try:
		member.save()	
	except pymongo.errors.DuplicateKeyError,a:
		if 0 != connection.Member.find({'name':member.name}).count():
			return (False,u"用户名已经存在!")
		if 0 != connection.Member.find({'email':member.email}).count():
			return (False,u"Email已经存在!!")
		return (False,u"错了么")
	return (True,None)

##check 用户登录
"""
def xxx(method):
	def newxx(self,*a,**n):
		self.t ="aa"
		method(self,*a,**n)
	return newxx
	
class a:
	def __init__(self):
		pass
	@xxx
	def test(self,a,b):
		print a
		print b
		print self.t

if __name__ == '__main__':
	t = a()
	t.test("1","2")
"""

if __name__ == '__main__':
	p		= get_member_by_name("")
	"""
	for i in get_all_member():
		print i
	if (is_admin(p)):
		print "admin"
	a		= connection.Member()
	a.name		= u"混世魔王"
	a.email		= u"chuanjiabao19811@gmail.com"
	a.password	= u"123"
	"""
	#print add_a_member(a)
	#print get_member_by_name(a.name)
	print get_member_by_name(u'飞龙在天')
	print get_member_by_email(u'chuanjiabao19811@gmail.com')

	a		= connection.Member()
	a.name		= u"混世魔王"
	a.email		= u"chuanjiabao19811@gmail.com"
	a.password	= u"123"
	print verify_login(a)
