#coding=utf-8
from model.topic import *
from model.reply import *

def get_topic_info(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,topic_id):
			self.topic = find_topic_by_id(topic_id)
			if not self.topic:
				raise web.seeother(redirect_path)
			return method(self,topic_id)
		return __f
	return __inner_wrapper

def get_reply_info(web):
	def __inner_wrapper(method):
		def __f(self,topic_id):
			self.replies = get_reply_by_topic_id(topic_id)
			return method(self,topic_id)
		return __f
	return __inner_wrapper

