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
	topic = connection.Reply.find({'topic_id':bson.objectid.ObjectId(topic_id)})
	return topic

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
	return connection.Reply.find({'topic_id':topic._id}).sort([("create_time",pymongo.DESCENDING)]).limit(1)


	
	
