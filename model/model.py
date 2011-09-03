# coding=utf-8
from mongokit import *
from default  import *
import pymongo
import datetime
import config
## 创建链接
connection		= Connection(config.mongodb_host,config.mongodb_port)



@connection.register
class Classify(Document):
	__collection__ = config.collection_name.Classify
	__database__   = config.classify_database
	structure      = {
			 "url"			:basestring,### 类型的url名称
			 "name"			:basestring,### 用于展示
			 "des"			:basestring,
			 "node_num"		:int,	 ### classify中包含的node个数
			 "create_time"		:datetime.datetime
	}
	use_dot_notation	=	True
	default_values		=	{"node_num":0,"create_time":datetime.datetime.utcnow()}
	indexes			=	[
						{
							'fields':["url"],
							'unique':True
						}, 
						{
							'fields':["name"],
							'unique':True
						}
					]

@connection.register
class Node(Document):
	__collection__ = config.collection_name.Node
	__database__   = config.classify_database
	structure      = {

				"url"		: basestring, 		# url 
				"name"		: basestring,		# 用于展示的 比如汉字
				"header"	: basestring,		# 节点的说明
				#TODO::这个要拆分为 topic_num video_topic_num image_topic_num
				#TODO::后端管理 要判断 都不为空
				"topic_num"	: int,			# 节点topic总数
				"video_num"	: int,			# 节点video总数
				"image_num"	: int,			# 节点image总数
				"image"		: basestring,		# 节点图片
				"classify"	: Classify,		# 节点所属类别
				"create_time"	: datetime.datetime
			 }
	use_dot_notation	=	True
	use_autorefs		= 	True
	default_values		=	{"topic_num":0,"video_num":0,"image_num":0,"header":"","create_time":datetime.datetime.utcnow()}
	indexes			=	[
						{
							'fields':["url"],
							'unique':True
						},
						{
							'fields':["name"],
							'unique':True
						},
						{
							'fields':[("classify",pymongo.ASCENDING)]

						}	
					]



@connection.register
class Member(Document):
	__collection__ = config.collection_name.Member
	__database__   = config.classify_database
	structure = {
			"name"		:basestring,
			"email"		:basestring,
			"password"	:basestring,
			"authority"	:long,
			"status"	:int,
			"readme"	:basestring,
			"avatar"	:basestring,
			"register_time"	:datetime.datetime
		    }
	use_dot_notation	=	True
	default_values		=	{"authority"		:MemberAuthority.default_authority,
					 "status"		:MemberStatus.active,
					 "register_time"	:datetime.datetime.utcnow(),
					 "readme"		:"",
					 "avatar"		:"avatar"
					  }
	indexes			=	[
						{
							"fields":["name"],
							"unique":True
						},
						{	"fields":["email"],
							"unique":True
						}
					]

@connection.register
class Video(Document):
	__collection__ = config.collection_name.Video
	__database__   = config.classify_database
	structure = {
		"title"			:basestring,
		"content"		:basestring,
		"content_length"	:int,
		"time"			:int,	#视频时间,单位s
		"node"			:Node,
		"create_time"		:datetime.datetime,
		"author"		:Member,
		"last_reply_time"	:datetime.datetime,
		"last_reply_by"		:basestring,			# 最后回复
		"reply_num"		:int,
		"view_num"		:int,
		"tag"			:basestring,
		"location"		:basestring,
		"video_md5"		:basestring,
		"image_time"		:int,	# 截图的时间 单位 s
		"image"			:basestring,
		"fail_reason"		:basestring,
		"status"		:int			
	}
	use_dot_notation		= True
	use_autorefs			= 	True
	default_values			=	{"reply_num"		:0,
						 "create_time"		:datetime.datetime.utcnow(),
						 "view_num"		:0,
						 "last_reply_time"	:datetime.datetime.utcnow(),
					  	 "status"  		:video_status_wait_process,
					  	 "image_time" 		: 5,
					  	 "image"   		:""
						}
	indexes				= [
						{

						###这个索引顺序有待研究
						  'fields':[("node",pymongo.ASCENDING),("last_reply_time",pymongo.DESCENDING)]
						},
						{
						###这个索引用于在首页，展示
						  'fields':[("last_reply_time",pymongo.DESCENDING)]
						},
						{
						  'fields':[("author",pymongo.ASCENDING)]
						}
					  ]


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
		"title"			:basestring,
		"content"		:basestring,
		"content_length"	:int,
		"hits"			:int,
		"author"		:basestring,
		"author_ref"		:pymongo.objectid.ObjectId,			# 作者引用
		"author_avatar"		:basestring,
		"video"			:{
						"where":basestring,	# 视频位置
						"image":basestring,	# 视频截图的位置
						"time" : int 
					 },	
		"create_time"		:datetime.datetime,		# topic 创建时间
		"node_url"		:basestring,			# 节点的url
		"node_name"		:basestring,			# 节点的引用
		"node_ref"		:pymongo.objectid.ObjectId,				# 
		"last_reply_time"	:datetime.datetime,
		"last_reply_by"		:basestring,			# 最后回复
		"reply_num"		:int			
	}
	#TODO:
	#content title 长度限制
	use_dot_notation	=	True
	default_values		=	{"reply_num":0,"create_time":datetime.datetime.utcnow(),"hits":0,"last_reply_time":datetime.datetime.utcnow()}


@connection.register
class Reply(Document):
	__collection__ 	= config.collection_name.Reply
	__database__	= config.classify_database	
	structure = {
			"topic_id"		:pymongo.objectid.ObjectId,
			"author"  		:Member,
			"create_time"		:datetime.datetime,
			"content"		:basestring,
			"content_length"	:int
		    }
	use_dot_notation	=	True
	use_autorefs		= 	True

	default_values		= {"create_time":datetime.datetime.utcnow()}
	indexes			= [
					{'fields':[("author",pymongo.ASCENDING),("create_time",pymongo.DESCENDING)]},
					{'fields':[("topic_id",pymongo.ASCENDING),("create_time",pymongo.DESCENDING)]}
				  ]
