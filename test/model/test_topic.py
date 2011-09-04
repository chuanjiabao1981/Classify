from model.reply 	import *
from model.topic 	import *
from model.node  	import *
from model.member 	import *
import unittest

class TestTopicApi(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
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
	
