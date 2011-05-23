#coding=utf-8
from mongokit import *
import pymongo
import datetime
import config
## 创建链接
connection		= Connection(config.mongodb_host,config.mongodb_port)

"""
1.  没有把 replies 作为array embeded into 到topic中
    1. 性能。拿插入来讲，独立的document 是 embed array 的10倍 参考《mongodb definitive guide》page 36
    2. 权衡。embeded array最要用在项数比较少的情况，例如投票，或者 插入比较少的情况
    3. 简单。"一次查询把一个topic全部内容都获取到不是挺好么"。如果维持现状这个当然是一个好的选择。
       但是涉及到，replies的修改、trees replies，pages等需求的时候，我们就要操作一个embeded的array，
       这个代码相对来讲较复杂。不想给自己找麻烦。
"""

@connection.register
class Topic(Document):

	__collection__ 	= 'topic'
	__database__	= config.classify_database
	structure = {
		"title"			:unicode,
		"content"		:unicode,
		"content_length"	:int,
		"author"		:unicode,
		"author_ref"		:Member,			# 作者引用
		"video"			:{
						"where":unicode,	# 视频位置
						"image":unicode,	# 视频截图的位置
						"time" : int 
					 },	
		"create_time"		:datetime.datetime,		# topic 创建时间
		"node_url"		:unicode,			# 节点的url
		"node_name"		:unicode,			# 节点的引用
		"node_ref"		:Node,				# 
		"last_reply_time"	:datetime.datetime,
		"last_reply_by"		:unicode,			# 最后回复
		"reply_num"		:int			
	}

@connection.register
class Member(Document):
	__collection__ = 'member'
	__database__   = config.classify_database
	structure = {
			"name"		:unicode,
			"email"		:unicode,
			"password"	:unicode
		    }
@connection.register
class Reply(Document):
	__collection__ 	= 'reply'
	__database__	= config.classify_database	
	structure = {
			"topic_id"		:pymongo.objectid.ObjectId,
			"author"  		:unicode,
			"create_time"		:datetime.datetime,
			"content"		:unicode,
			"content_length"	:int
		    }

@connection.register
class Node(Document):
	__collection__ = 'node'
	__database__   = config.classify_database
	structure      = {
				"node_url"		: unicode, 		# url 
				"node_name"		: unicode,		# 用于展示的 比如汉字
				"create_time"		: datetime.datetime
			 }

if __name__ == '__main__':
	"""
	t = connection.Topic()
	t['title'] = u"你好"
	t['content']	= u" 谁知道好不好"
	t['content_length']	=123	
	t.save()
	print t.validate()
	m = connection.Member()
	m["name"] 	= u"maguowei"
	m["email"]	= u"chuanjiabao1981@gmail.com"
	m["password"]   = u"mgw"

	n = connection.Node()
	n["node_url"]		= 	u"test"
	n["node_name"]		=	u"测试"
	n["create_time"]	=	datetime.datetime.now()
	n.save()

	"""

