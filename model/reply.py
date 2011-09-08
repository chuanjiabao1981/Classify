# coding=utf-8
from model import *
from node  import *
from member import *
import bson.objectid
import datetime
import config


def add_a_reply(web_info,member,topic):
	reply			= connection.Reply()
	reply.topic_id		= topic._id
	reply.author		= member.get_dbref()
	reply.content		= web_info.content
	reply.content_length	= len(reply.content)
	reply.save()

def get_reply_by_topic_id(topic_id):
	##TODO::翻页??
	##索引
	replies = connection.Reply.find({'topic_id':bson.objectid.ObjectId(topic_id)}).sort([("create_time",pymongo.ASCENDING)])
	return replies

def add_a_new_reply(topic,member,webinput):
	reply			= connection.Reply()
	reply.topic_id		= topic._id
	reply.author		= member.get_dbref()
	reply.content		= webinput.content
	reply.content_length	= len(webinput.content)
	reply.create_time	= datetime.datetime.utcnow()
	reply.save()
	return reply

def del_a_reply(reply):
	reply.delete()

def get_reply_num(topic):
	return connection.Reply.find({'topic_id':topic._id}).count()
def find_latest_reply_of_topic(topic):
	##TODO::create_time建立索引
	k = connection.Reply.find({'topic_id':topic._id}).sort([("create_time",pymongo.DESCENDING)]).limit(1)
	if not k or k.count() == 0:
		return None
	else:
		return k[0]

def get_all_reply_num():
	return connection.Reply.find().count()

def del_all_reply():
	connection[config.classify_database][config.collection_name.Reply].remove()

if '__main__' == __name__:
	k = connection.Reply.find().limit(1)
	#print k[0].create_time
	print k[0]["create_time"]

	
	
