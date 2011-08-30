# coding=utf-8
from model import *
from classify import *
from topictools import *
def get_node_by_url_name(url_name):
	k=connection.Node.find_one({'url':url_name})	
	return k

def inc_topic_num_by_node_url_name(name):
	# only update the first one
        # because url is uniqu
	connection[config.classify_database][config.collection_name.Node].update(
		{'url':name}, 
		{ '$inc':{"topic_num":1} } 
	)
def get_all_node():
	return connection.Node.find().sort('create_time')

def find_a_node(node_id):
	return connection.Node.find_one({'_id':bson.objectid.ObjectId(node_id)})
"""
这个函数是以前的nested结构的时候,
一旦classify更新后，更新对应的node节点信息。
目前的结构，不推荐使用。
"""
def update_node_classify_info(classify_info):
	connection[config.classify_database][config.collection_name.Node].update(
		{'classify_ref':classify_info._id},
		{
		 '$set':{
				'classify_ref'	:	classify_info._id,
				'classify_name'	:	classify_info.name,
				'classify_url'	:	classify_info.url
			}
		},
		multi=True
	)
def update_a_node(node_info,web_info):
	try:
		# first
		classify_item	=	find_a_classify(web_info.classify_id)
		if not classify_item:
			return (False,-2)
		#second
		t= connection[config.classify_database][config.collection_name.Node].update(
		{'_id':node_info._id},
		{
	 	'$set':{
			 'url'			:	web_info.url,
			 'name'			:	web_info.name,
			 'header'		:	web_info.header,
			 'classify'		:	classify_item.get_dbref()
		       }
		},
		safe=True
		)
		#third
		update_classify_node_num(node_info.classify._id,-1)
		update_classify_node_num(classify_item._id,1)

		#forth
		#update_topic_node_info(node_info._id,config.collection_name.Video)
		#update_topic_node_info(node_info._id,config.collection_name.Topic)

	
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)

	return (True,0)

	
def add_a_node(info):
	node			= 	connection.Node()
	classify_item		=	find_a_classify(info.classify_id)
	print classify_item
	if not classify_item:
		return (False,-2)
	node.name		=	info.name
	node.url		=	info.url
	node.header		=	info.header
	node.classify		=	classify_item.get_dbref()
	print node.classify
	print classify_item.get_dbref()
	try:
		node.save()
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	update_classify_node_num(classify_item._id,1)
	return (True,0)
def inc_video_topic_num(node,num):

	connection[config.classify_database][config.collection_name.Node].update(
		{'_id':node._id}, 
		{ '$inc':{"video_num":num} 
		},safe=True 
	)


if __name__ == "__main__":
	#i= connection.Node.find_one({'url':'testnode'})	
	class info:
		def __init__(self):
			self.name 		=	'ddd'
			self.classify_id	=	'4e5cdde3decbef0919000001'
			self.url		=	'ddd'
			self.header		=	'cdd'
	a = info()
	add_a_node(a)
	all = get_all_node()
	for i in all:
		print i
		print i.classify
