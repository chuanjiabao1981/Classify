# coding=utf-8
import web
import os
from model.video  import *
from model.model  import *
from model.member import *
from model.classify import *
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from template import template_desktop
import config
import re

Backend_File ={'main':'backend_classify.html',
	       'classify':'backend_classify.html'}
class Backend:
	def GET(self,arg):
		node_url_name	= ""
		member_name 	= ""
		member 		= get_member_by_name(member_name)
		node		= get_node_by_url_name(node_url_name)
		
		if not arg in Backend_File:
			return web.notfound('这个真没有');
		admin_file	= Backend_File[arg]

		try: 
			return  template_desktop.get_template('backend.html').render(node=node,site=config.site,admin_file=admin_file)

		except:
			return exceptions.html_error_template().render()


class Classify:
	def GET(self):
		all_classify = get_all_classify()
		try:
			return template_desktop.get_template('backend.html').render(all_classify=all_classify,admin_file='backend_classify.html')
		except:
			return exceptions.html_error_template().render()

class ClassifyAdd:
	def GET(self):
		try:
			return template_desktop.get_template('backend.html').render(admin_file='backend_classify_add.html')
		except:
			return exceptions.html_error_template.render()	
	def POST(self):
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
			return template_desktop.get_template('backend.html').render(error=error,web=web,admin_file='backend_classify_add.html')
		###去首尾空白 
		(status,code) = add_a_classify(web.input().url.strip(" "),web.input().name.strip(" "),web.input().des.strip(" "))
		if not status and code == -1:
			error = u'这个分类已经存在(url名称或者类别名称已经重复)'
		if error:
			return template_desktop.get_template('backend.html').render(error=error,web=web,admin_file='backend_classify_add.html')
		return web.seeother('/backend/classify')
