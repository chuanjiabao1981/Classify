from model.reply import *
from model.topic import *
import unittest

class TestReplyApi(unittest.TestCase):
	class testinput:
		def __init__(self,content):
			self.content	= content

	def setUp(self):
		self._id 		= '4e60d3f2decbef0c12000000'
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

	def test_get_rely_by_topic_id(self):
		a = get_reply_by_topic_id(self._id)

	def test_del_a_reply(self):
		webinput1 	= TestReplyApi.testinput("No.1 yesterday i have a dream")
		webinput2 	= TestReplyApi.testinput("No.2 yesterday i have a dream")
		before_num	= get_reply_num(self.topic)
		print "Topic Before Reply[%d]"%(before_num)

		reply1 = add_a_new_reply(self.topic,self.member,webinput1)
		reply2 = add_a_new_reply(self.topic,self.member,webinput2)

		after_insert_reply_num = get_reply_num(self.topic)
		print "Topic After Reply[%d]"%(after_insert_reply_num)

		self.assertEqual(before_num+2,after_insert_reply_num,"Reply del api Error")

		del_a_reply(reply1)
		del_a_reply(reply2)
		after_del_reply_num	= get_reply_num(self.topic)
		print "Topic Del Rely[%d]"%(after_del_reply_num)
		self.assertEqual(before_num,after_del_reply_num,"Reply del api Error")

		

	def test_find_latest_reply_of_topic(self):
		
		webinput1 	= TestReplyApi.testinput("No.1 yesterday i have a dream")
		webinput2 	= TestReplyApi.testinput("No.2 yesterday i have a dream")

				
		reply0 = add_a_new_reply(self.topic,self.member,webinput1)
		reply1 = add_a_new_reply(self.topic,self.member,webinput2)
		latest_reply = find_latest_reply_of_topic(self.topic)
		
		print reply
		"""
		replies = [i for i in find_latest_reply_of_topic(self.topic)]
		
		print replies[0]._id,reply1._id
		print replies[1]._id,reply0._id
	
		self.assertEqual(reply0._id,replies[1]._id,"sequence error")
		self.assertEqual(reply1._id,replies[0]._id,"sequence error")
		"""
		del_a_reply(reply0)
		del_a_reply(reply1)

if __name__ == '__main__':
	unittest.main()
	
