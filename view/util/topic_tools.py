#coding=utf-8
from model.topic import *
##获取node信息
def get_topic_info(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,topic_id):
			self.topic = find_topic_by_id(topic_id)
			if not self.topic:
				raise web.seeother(redirect_path)
			return method(self,topic_id)
		return __f
	return __inner_wrapper

