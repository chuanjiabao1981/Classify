#coding=utf-8
from model.node import *
##获取node信息
def get_node_info(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,node_url_name):
			self.node = get_node_by_url_name(node_url_name)
			if not self.node:
				raise web.seeother(redirect_path)
			return method(self,node_url_name)
		return __f
	return __inner_wrapper

