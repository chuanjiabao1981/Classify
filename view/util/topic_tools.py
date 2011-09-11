#coding=utf-8
from model.topic import *
from model.reply import *
from model.video import *

def get_topic_info(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,topic_id):
			self.topic = find_topic_by_id(topic_id)
			if not self.topic:
				raise web.seeother(redirect_path)
			return method(self,topic_id)
		return __f
	return __inner_wrapper

def get_videotopic_info(web,redirect_path):
	def __inner_wrapper(method):
		def __f(self,topic_id):
			self.topic = find_video_topic_by_id(topic_id)
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


class TopicReplyCheck:

	def __init__(self):
		self.content_length_up 		=	2000
		self.content_length_down	=	3

		self.inputerror_str			=	{}
		self.inputerror_str[0]		=	None
		self.inputerror_str[1]		=	u'八个呀路!'
		self.inputerror_str[2]		=	u'输入字符不能超过'+unicode(str(self.content_length_up))+u'个字符'
		self.inputerror_str[3]		=	u'写点啥,别空着!'
		self.inputerror_str[4]		=	u'写的太少了、再写点。至少写'+unicode(str(self.content_length_down))+u'个字符'

	def check_input(self,webinput):
		if not 'content' in webinput:
			return self.inputerror_str[1]
		if len(webinput.content) > self.content_length_up:
			return self.inputerror_str[2]
		if len(webinput.content.strip()) == 0:
			return self.inputerror_str[3]
		if len(webinput.content.strip()) < self.content_length_down:
			return self.inputerror_str[4]

		return self.inputerror_str[0]
