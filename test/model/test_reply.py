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

	def test_del_all_reply(self):
		print get_all_reply_num()
		del_all_reply()
		self.assertEqual(get_all_reply_num(),0,"Del all err")

	def test_find_latest_reply_of_topic_case1(self):
		del_all_reply()
		latest_reply = find_latest_reply_of_topic(self.topic)
		self.assertEqual(latest_reply,None,"Api Error")

	def test_find_latest_reply_of_topic(self):
		
		webinput1 	= TestReplyApi.testinput("No.1 yesterday i have a dream")
		webinput2 	= TestReplyApi.testinput("No.2 yesterday i have a dream")

				
		reply0 = add_a_new_reply(self.topic,self.member,webinput1)
		reply1 = add_a_new_reply(self.topic,self.member,webinput2)
		latest_reply = find_latest_reply_of_topic(self.topic)
		print reply1.create_time,reply1._id
		print reply0.create_time,reply0._id

		print latest_reply["create_time"],latest_reply["_id"]
		self.assertEqual(reply1._id,latest_reply["_id"],"Not Same id")

		del_a_reply(reply0)
		del_a_reply(reply1)

if __name__ == '__main__':
	unittest.main()
	
