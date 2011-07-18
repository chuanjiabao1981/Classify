# coding=utf-8
import web
import os
from model.video  import *
from model.model  import *
from model.member import *
from model.classify import *
from model.node  import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop
import config
import re

Backend_File ={'main':'backend_classify.html',
	       'classify':'backend_classify.html'}
class Backend:
	def GET(self):
		node_url_name	= ""
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		arg		= 'main'
		if not arg in Backend_File:
			return web.notfound('这个真没有');
		admin_file	= Backend_File[arg]

		try: 
			return  template_desktop.get_template('backend.html').render(node=node,site=config.site,admin_file=admin_file)

		except:
			return exceptions.html_error_template().render()

class NodeOverView:
	def GET(self):
		all_node = get_all_node()
		return template_desktop.get_template('backend.html').render(all_node=all_node,admin_file='backend_node.html')

def NodeVerifyPostInput():
	p		=	re.compile('^[a-zA-Z0-9_]+$')
	url_len_limit	=	64
	name_len_limit	=	10
	error		=	None
	if not web.input().url:
		error = u'节点 url不能为空!'	
	elif not p.match(web.input().url):
		error = u'节点 url只能为字母、数字、下划线!'
	elif len(web.input().url) > url_len_limit:
		error = u'节点 url不能超过'+str(url_len_limit)+u'个字符!'
	elif not web.input().name:
		error = u'节点名称不能为空!'
	elif len(web.input().name) > name_len_limit:
		error = u'节点名称不能超过'+str(name_len_limit)+u'个字符!'
	elif not web.input().classify_id:
		error = u'类别id异常'
	return error
	
class NodeEdit:
	def GET(self,arg):
		if not arg:	
			return web.notfound("这个真没有")
		i = find_a_node(arg)
		if not i:
			return web.notfound("这个真没有")

		all_classify		= get_all_classify()
		t = {}
		t["admin_file"]		= 'backend_node_add.html'
		t["error"]		= None
		t["action_type"]	= 'edit'
		t["all_classify"]	= all_classify
		t["node_item"]		= i
		t["web"]		= web
		t["node_item_id"]	= arg
		return template_desktop.get_template('backend.html').render(**t)

	def POST(self,arg):
		t			= {}
		t["error"]		= NodeVerifyPostInput()
		t["admin_file"]		= 'backend_node_add.html'
		t["action_type"]	= 'edit'
		t["all_classify"]	= get_all_classify()
		t["node_item"]		= find_a_node(arg)
		t["web"]		= web
		t["node_item_id"]	= arg
		if not t["node_item"]:
			return web.notfound("这个真没有")
		if t["error"]:
			return template_desktop.get_template('backend.html').render(**t)

		(status,code)		= update_a_node(t["node_item"],web.input())
		if code == -1 and status == False:
			t["error"]	= u'节点的url或者节点名称已经存在'
			return template_desktop.get_template('backend.html').render(**t)
		return web.seeother('/backend/node')

	
class NodeAdd:
	def GET(self):
		all_classify = get_all_classify()
		t			= {}
		t["admin_file"] 	= 'backend_node_add.html'
		t["error"]		= None
		t["action_type"]	= 'add'
		t["all_classify"]	= all_classify
		return template_desktop.get_template('backend.html').render(**t)
	def POST(self):
		t			= {}
		t["admin_file"] 	= 'backend_node_add.html'
		t["action_type"]	= 'add'
		t["error"]		= NodeVerifyPostInput()
		t["all_classify"] 	= get_all_classify()
		t["web"]	  	= web	

		if t["error"]:
			return template_desktop.get_template('backend.html').render(**t)
		(status,code)		= add_a_node(web.input())
		if code == -1 and status == False:
			t["error"]	= u'节点的url或者节点名称已经存在'
			return template_desktop.get_template('backend.html').render(**t)
		return web.seeother('/backend/node')

		

class Classify:
	def GET(self):
		all_classify = get_all_classify()
		try:
			return template_desktop.get_template('backend.html').render(all_classify=all_classify,admin_file='backend_classify.html')
		except:
			return exceptions.html_error_template().render()

class ClassifyOverView:
	def GET(self):
		t			=	{}
		t['all_classify']	=	get_all_classify()
		t['admin_file']		=	'backend_classify.html'
		return template_desktop.get_template('backend.html').render(**t)


def ClassifyEditAddPost(action_type,classify_item_id):
	url_len_limit	=	1024
	name_len_limit	=	10
	des_len_limit	=	1024
	p		=	re.compile('^[a-zA-Z0-9_]+$')
	error		=	None
	if not web.input().url:
		error = u'类别 url不能为空!'	
	elif not p.match(web.input().url):
		error = u'类别 url只能为字母、数字、下划线!'
	elif len(web.input().url) > url_len_limit:
		error = u'类别 url不能超过'+str(url_len_limit)+u'个字符!'
	elif not web.input().name:
		error = u'类别名称不能为空!'
	elif len(web.input().name) > name_len_limit:
		error = u'类别名称不能超过'+str(name_len_limit)+u'个字符!'
	elif len(web.input().des) > des_len_limit:
		error = u'类别说明不能超过'+str(des_len_limit)+u'个字符!'
	if error:
		return template_desktop.get_template('backend.html').render(error=error,\
					web=web,\
					admin_file='backend_classify_add.html',\
					action_type=action_type,\
					classify_item_id=classify_item_id)
	if action_type == 'add':
		(status,code) = add_a_classify(web.input())
	elif action_type == 'edit':
		(status,code) = update_a_classify(web.input())
 					  
	if not status and code == -1:
		error = u'这个分类已经存在(url名称或者类别名称已经重复)'
	if error:
		return template_desktop.get_template('backend.html').render(error=error,\
									    web=web,\
									    admin_file='backend_classify_add.html',\
									    action_type=action_type,\
									    classify_item_id=classify_item_id
										)
	return web.seeother('/backend/classify')

class ClassifyEdit:
	def GET(self,arg):
		if not arg:
			return web.notfound("这个真没有")
		i= find_a_classify(arg)
		if not i:
			return web.notfound("这个真没有")
		return template_desktop.get_template('backend.html').render(admin_file='backend_classify_add.html',\
									   action_type='edit',\
									   classify_item=i,\
									   classify_item_id=arg)
	def POST(self,arg):
		if not arg:		
			return web.notfound("这个真没有")
		return ClassifyEditAddPost('edit',arg)



class ClassifyAdd:
	def GET(self):
		return template_desktop.get_template('backend.html').render(admin_file='backend_classify_add.html',error=None,action_type='add')
	def POST(self):
		return ClassifyEditAddPost('add',None)

class MemberOverView:
	def GET(self):
		t		=	{}
		t["all_member"]	=	get_all_member()
		t["admin_file"]	=	'backend_member.html'
		return template_desktop.get_template('backend.html').render(**t)
def MemberVerifyPostInput():
	user_name_len_limit	= 20
	if not web.input().name:
		return u"用户名不可为空"
	elif len(web.input().name) > user_name_len_limit:
		return u"用户名不可超过"+str(user_name_len_limit)+u"个字符！"

	if web.input().password != web.input().password_again:
		return u"密码两次输入不一致"
	if not '@' in web.input().email:
		return u"电子邮件格式错误"

	return None
class MemberEdit:
	def GET(sef,arg):
		t			=	{}
		t["admin_file"]		=	'backend_member_add.html'
		t["action_type"]	=	'edit'
		t["error"]		=	None #MemberVerifyPostInput()
		t["web"]		=	web
		t["item"]		=	get_member_by_id(arg)
		if not t["item"]:
			return web.notfound()
		return template_desktop.get_template('backend.html').render(**t)
	def POST(self,arg):
		t			=	{}
		t["admin_file"]		=	'backend_member_add.html'
		t["action_type"]	=	'edit'
		t["error"]		=	MemberVerifyPostInput()
		t["web"]		=	web
		t["item"]		=	get_member_by_id(arg)
		if not t["item"]:
			return web.notfound()
		if t["error"]:
			return template_desktop.get_template('backend.html').render(**t)
		(status,t["error"])	= update_member_info(t["item"],web.input())
		if t["error"]:
			return template_desktop.get_template('backend.html').render(**t)
		return web.seeother('/backend/member')

	
		
	
class MemberAdd:
	def GET(self):
		t			=	{}
		t["admin_file"]		=	'backend_member_add.html'
		t["action_type"]	=	'add'
		return template_desktop.get_template('backend.html').render(**t)
	def POST(self):
		t			=	{}
		t["admin_file"]		=	'backend_member_add.html'

		t["error"]		=	MemberVerifyPostInput()
		t["web"]		=	web
		t["action_type"]	=	'add'
		try:
			if t["error"]:
				return template_desktop.get_template('backend.html').render(**t)
			(status,t["error"]) = add_a_member(web.input())
			if t["error"]:
				return template_desktop.get_template('backend.html').render(**t)
			return web.seeother('/backend/member')
		except:
			return exceptions.html_error_template().render()
			return web.input()


