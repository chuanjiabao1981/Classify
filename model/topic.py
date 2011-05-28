# coding=utf-8
from model import *
from node  import *
from member import *
import bson.objectid
import datetime
import config

def add_new_topic(node,member,title,video,content):
	topic	= connection.Topic()
	topic.title		=	title
	topic.content		= 	content
	topic.content_length	= 	len(topic.content)
	topic.author		= 	member.name
	topic.author_ref	=	member._id
	topic.video.where	=	video
	topic.node_url		=	node.url
	topic.node_name		=	node.name
	topic.node_ref		=	node._id
	topic.save()
	return topic

def add_new_reply_to_topic(topic_id,reply_time,reply_author):
	## 这里必须这样用
	## connection.Topic不好使
	connection[config.classify_database][config.collection_name.Topic].update(
		{'_id':topic_id}, 
		{ '$inc':{"reply_num":1} ,
		  '$set':{"last_reply_by":reply_author,"last_reply_time":reply_time}
		
		} 
	)



def find_topic_by_id(topic_id):
	return connection.Topic.find_one({'_id':bson.objectid.ObjectId(topic_id)})

def get_reply_by_topic_id(topic_id):
	return connection.Reply.find({'topic_id':bson.objectid.ObjectId(topic_id)})

	

	
if __name__=='__main__':
	#add_new_reply_to_topic(bson.objectid.ObjectId('4ddc49c0decbef09c3000000'),datetime.datetime.now(),u"mgw")
	for reply in get_reply_by_topic_id('4ddc49c0decbef09c3000000'):
		print reply
	#print find_topic_by_id('4ddc49c0decbef09c3000000')
