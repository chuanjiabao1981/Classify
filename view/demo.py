# coding=utf-8
import web
import os,shutil

class DemoPost:
	def POST(self):
		##这个必须读
		print web.input()
		return """{"img":"1"}""";

class DemoGet:
	def GET(self):
		return "{'img':'1'}";
