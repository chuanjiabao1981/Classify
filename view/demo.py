# coding=utf-8
import web
import os,shutil

class DemoPost:
	def POST(self):
		##这个必须读
		print web.input()
		return "<html><strong>aaaa</strong><html>";

class DemoGet:
	def GET(self):
		return "{'img':'1'}";
