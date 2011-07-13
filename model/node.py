from model import *
from classify import *
def get_node_by_url_name(name):
	return connection.Node.find_one()	

def inc_topic_num_by_node_url_name(name):
	# only update the first one
        # because url is uniqu
	connection[config.classify_database][config.collection_name.Node].update(
		{'url':name}, 
		{ '$inc':{"topic_num":1} } 
	)
def get_all_node():
	return connection.Node.find().sort('create_time')


def add_a_node(info):
	node			= 	connection.Node()
	classify_item		=	find_a_classify(info.classify_id)
	if not classify_item:
		return (False,-2)
	node.name		=	info.name
	node.url		=	info.url
	node.header		=	info.header
	node.classify_ref	=	classify_item._id
	node.classify_name	=	classify_item.name
	node.classify_url	=	classify_item.url
	try:
		node.save()
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)
	return (True,0)

if __name__ == "__main__":
	node = get_node_by_url_name("")
	print node
	#inc_topic_num_by_node_url_name("begin")
