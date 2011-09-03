from model.reply import *
import unittest

class TestReplyApi(unittest.TestCase):
	def setUp(self):
		self._id = '4e60d3f2decbef0c12000000'
	def test_get_rely_by_topic_id(self):
		a = get_reply_by_topic_id(self._id)

if __name__ == '__main__':
	unittest.main()
	
