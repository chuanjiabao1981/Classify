# coding=utf-8
import sys
from model import *
import bson.objectid
import config


def get_all_classify():
	return connection.Classify.find().sort('create_time')


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

def find_a_classify(topic_id):
	return connection.Classify.find_one({'_id':bson.objectid.ObjectId(topic_id)})

def update_a_classify(classify_id,url,name,des):
	try:
		connection[config.classify_database][config.collection_name.Classify].update(
		{'_id':bson.objectid.ObjectId(classify_id)},
		{
	 	'$set':{'url':url,'name':name,'des':des}
		},
		safe=True
		)
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	return (True,0)

	

if __name__ == '__main__':
	update_a_classify('4e1b8c3cdecbef10a9000000','test1','aa','test')
	#sys.exit(1)
	#k = get_all_classify()
	#print type(k) 
	"""
	try:
		print add_a_classify(u'm1',u'u1',u'test')
	except pymongo.errors.DuplicateKeyError,a:
		print a
	"""
