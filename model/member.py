#coding=utf-8
from model import *
from default import *

def is_admin(member):
	if not member:
		return False
	if (member.authority & ( 1 << member_authority_admin)):
		return True
	return False

def get_member_by_name(name):
	return connection.Member.find_one()	

def update_member_info(member_info,web_info):
	pass
def get_all_member():
	return connection.Member.find()
def add_a_member(web_info):
	member		=	connection.Member()
	member.name	=	web_info.name
	member.email	=	web_info.email
	member.password	=	web_info.password
	if connection.Member.find().count() == 0:
		member.authority	=	~0l	
	try:
		member.save()	
	except pymongo.errors.DuplicateKeyError,a:
		if 0 != connection.Member.find({'name':member.name}).count():
			return (False,u"用户名已经存在")
		if 0 != connection.Member.find({'email':member.email}).count():
			return (False,u"Email已经存在")
		return (False,u"错了么")
	return (True,None)
if __name__ == '__main__':
	p		= get_member_by_name("")
	for i in get_all_member():
		print i
	if (is_admin(p)):
		print "admin"
	a		= connection.Member()
	a.name		= u"混世魔王"
	a.email		= u"chuanjiabao19811@gmail.com"
	a.password	= u"123"
	print add_a_member(a)
