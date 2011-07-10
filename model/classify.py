# coding=utf-8
from model import *

def get_all_classify():
	return connection.Classify.find()


def add_a_classify(url,name,des):
	classify = connection.Classify()	
	classify.name = name;
	classify.url  = url;
	classify.des  = des;
	try:
		classify.save()
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	return (True,0)


if __name__ == '__main__':
	k = get_all_classify()
	print type(k) 
	try:
		print add_a_classify(u'test',u'test_url',u'test')
	except pymongo.errors.DuplicateKeyError,a:
		print a
