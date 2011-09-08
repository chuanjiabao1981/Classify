from model.reply 	import *
from model.topic 	import *
from model.node  	import *
from model.member 	import *
import unittest

class TestTopicApi(unittest.TestCase):
	class testinput:
		def __init__(self,content):
			self.content	= content

	def setUp(self):
		self.topic  		= None
		self.member		= None
		for i in get_all_topic():
			self.topic = i
			break

		#get a member
		for i in get_all_member():
			self.member = i
			break

		self.assertNotEqual(self.topic,None,"No Topic:please insert one topic")
		self.assertNotEqual(self.member,None,"No Member:please insert one member")

	def tearDown(self):
		pass

	def test_add_new_reply_to_topic(self):
		webinput1 	= TestTopicApi.testinput("No.1 yesterday i have a dream")
		webinput2 	= TestTopicApi.testinput("No.2 yesterday i have a dream")
		#reply1 		= add_a_new_reply(self.topic,self.member,webinput1)
		#reply2 		= add_a_new_reply(self.topic,self.member,webinput2)

		add_new_reply_to_topic(self.topic,self.member,webinput1)
		add_new_reply_to_topic(self.topic,self.member,webinput2)

		
		topic_after_reply = find_topic_by_id(self.topic._id)
		print self.topic._id
		print self.topic.reply_num
		print topic_after_reply.reply_num
		
		self.assertEqual(self.topic.reply_num,topic_after_reply.reply_num-2,"add a new reply error")
	
	def test_add_a_new_topic(self):
		class testinput:
			def __init__(self):
				self.title 	= "test_add_case"
				self.content	= "yesterday i have a dream"
		#get a node
		for i in get_all_node():
			node = i
			break;
		#get a member
		for i in get_all_member():
			member = i
			break

		self.assertNotEqual(node,None,"Not have a node")
		self.assertNotEqual(member,None,"Not have a member")
		
		#add a topic 
		new_topic = add_a_new_topic(node,member,testinput())
		print "topic id:%s"%(str(new_topic._id))
		#get the topic
		k 	  = find_topic_by_id(new_topic._id)
		#get the node
		k2	  = find_node_by_id(node._id)
		
		self.assertEqual(new_topic._id,k._id,"Save Not success[%s:%s]"%(str(new_topic._id),str(k._id)))
		self.assertEqual(node.topic_num+1,k2.topic_num,"Topic Num is Not Right[%d:%d]"%(node.topic_num,k2.topic_num))
		print "Before:%d\tAfter:%d"%(node.topic_num,k2.topic_num)
		#remove the topic
		remove_a_topic(node,new_topic)
		#
		k3	  = find_topic_by_id(new_topic._id)
		#
		k4	  = find_node_by_id(node._id)
		
		self.assertEqual(k3,None,"Topic Not remove")
		self.assertEqual(node.topic_num,k4.topic_num,"Topic Num is Not Right[%d:%d]"%(node.topic_num,k4.topic_num))
		print "Before:%d\tAfter:%d"%(node.topic_num,k4.topic_num)

if __name__ == '__main__':
	unittest.main()
	
