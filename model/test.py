# coding=utf-8
from model import *
from node import *
from member import *
import datetime

def add_member_test():
	member = connection.Member.find_one();
	print member
	topic  = connection.Topic()
	topic["author_ref"] = member["_id"]
	topic.save()

def add_node_test():
	node = connection.Node()
	node.name = u"开始测试"
	node.url  = u"begin"
	node.create_time	=	datetime.datetime.now()
	node.save()

def add_topic_test():
	node 	= get_node_by_url_name("")
	member	= get_member_by_name("")
	topic	= connection.Topic()
	topic.title		=	u"你啊到底是哥啥米人"
	topic.content		= 	u"web 设计也是重点，方方面面都不能放"
	topic.content_length	= 	len(topic.content)
	topic.author		= 	member.name
	topic.author_ref	=	member._id
	topic.node_url		=	node.url
	topic.node_name		=	node.name
	topic.node_ref		=	node._id
	topic.save()
if __name__ == "__main__":
	add_topic_test()
