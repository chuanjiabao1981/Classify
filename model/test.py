# coding=utf-8
from model import *
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
if __name__ == "__main__":
	add_node_test()
