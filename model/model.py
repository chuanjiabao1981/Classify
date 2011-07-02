#coding=utf-8
from mongokit import *
from default  import *
import pymongo
import datetime
import config
## 创建链接
connection		= Connection(config.mongodb_host,config.mongodb_port)


@connection.register
class Node(Document):
	__collection__ = config.collection_name.Node
	__database__   = config.classify_database
	structure      = {
#TODO:保证url和name是唯一的

				"url"		: unicode, 		# url 
				"name"		: unicode,		# 用于展示的 比如汉字
				"header"	: unicode,		# 节点的说明
				"topic_num"	: int,			# 节点topic总数
				"create_time"		: datetime.datetime
			 }
	use_dot_notation	=	True
	default_values		=	{"topic_num":0,"header":""}


@connection.register
class Member(Document):
	__collection__ = config.collection_name.Member
	__database__   = config.classify_database
	structure = {
#TODO:保证name和email唯一
			"name"		:unicode,
			"email"		:unicode,
			"password"	:unicode
		    }
	use_dot_notation	=	True

@connection.register
class Video(Document):
	__collection__ = config.collection_name.Video
	__database__   = config.classify_database
	structure = {
		"title"			:unicode,
		"content"		:unicode,
		"content_length"	:int,
		"time"			:int,	#视频时间,单位s
		"node_url"		:unicode,
		"node_name"		:unicode,
		"node_ref"		:pymongo.objectid.ObjectId,
		"create_time"		:datetime.datetime,
		"author"		:unicode,
		"author_ref"		:pymongo.objectid.ObjectId,
		"last_reply_time"	:datetime.datetime,
		"last_reply_by"		:unicode,			# 最后回复
		"reply_num"		:int,
		"view_num"		:int,
		"tag"			:unicode,
		"location"		:unicode,
		"video_md5"		:unicode,
		"image_time"		:int,	# 截图的时间 单位 s
		"image"			:unicode,
		"fail_reason"		:unicode,
		"status"		:int			
	}
	use_dot_notation		= True
	default_values		=	{"reply_num":0,"create_time":datetime.datetime.now(),
					  "view_num":0,"last_reply_time":datetime.datetime.now(),
					  "status"  :video_status_wait_process,
					  "image_time" : 5,
					  "image"   :""}


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

	__collection__ 	= config.collection_name.Topic
	__database__	= config.classify_database
	structure = {
		"title"			:unicode,
		"content"		:unicode,
		"content_length"	:int,
		"hits"			:int,
		"author"		:unicode,
		"author_ref"		:pymongo.objectid.ObjectId,			# 作者引用
		"video"			:{
						"where":unicode,	# 视频位置
						"image":unicode,	# 视频截图的位置
						"time" : int 
					 },	
		"create_time"		:datetime.datetime,		# topic 创建时间
		"node_url"		:unicode,			# 节点的url
		"node_name"		:unicode,			# 节点的引用
		"node_ref"		:pymongo.objectid.ObjectId,				# 
		"last_reply_time"	:datetime.datetime,
		"last_reply_by"		:unicode,			# 最后回复
		"reply_num"		:int			
	}
	#TODO:
	#content title 长度限制
	use_dot_notation	=	True
	default_values		=	{"reply_num":0,"create_time":datetime.datetime.now(),"hits":0,"last_reply_time":datetime.datetime.now()}


@connection.register
class Reply(Document):
	__collection__ 	= config.collection_name.Reply
	__database__	= config.classify_database	
	structure = {
			"topic_id"		:pymongo.objectid.ObjectId,
			"author"  		:unicode,
			"create_time"		:datetime.datetime,
			"content"		:unicode,
			"content_length"	:int
		    }
	use_dot_notation	=	True

