# coding=utf-8
import sys
from model import *
from node import *
import bson.objectid
import config


def get_all_classify():
	return connection.Classify.find().sort('create_time')


def add_a_classify(web_info):
	
	classify = connection.Classify()	
	classify.name = web_info.name.strip(" ").strip("\n");
	classify.url  = web_info.url.strip(" ").strip("\n");
	classify.des  = web_info.des.strip(" ").strip("\n");
	print type(classify.name)
	print web_info.name
	print classify.name
	try:
		classify.save()
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	return (True,0)

def find_a_classify(topic_id):
	return connection.Classify.find_one({'_id':bson.objectid.ObjectId(topic_id)})

def update_a_classify(web_info):
	try:
		connection[config.classify_database][config.collection_name.Classify].update(
		{'_id':bson.objectid.ObjectId(web_info.id)},
		{
	 	'$set':{'url'		:web_info.url.strip(" ").strip("\n"),
			'name'		:web_info.name.strip(" ").strip("\n"),
			'des'		:web_info.des.strip(" ").strip("\n")
			}
		},
		safe=True
		)
		i = find_a_classify(web_info.id)
		update_node_classify_info(i)
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	return (True,0)

	
def update_classify_node_num(classify_id,num):
	connection[config.classify_database][config.collection_name.Classify].update(
		{'_id':bson.objectid.ObjectId(classify_id)},
		{'$inc':{"node_num":num}} ,
		safe=True
	)


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
