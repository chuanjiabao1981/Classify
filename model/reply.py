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
	reply.author		= member
	reply.content		= web_info.content
	reply.content_length	= len(reply.content)
	reply.save()

def get_reply_by_topic_id(topic_id):
	topic = connection.Reply.find({'topic_id':bson.objectid.ObjectId(topic_id)})
	return topic



	
	
