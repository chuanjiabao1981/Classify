from model import *
from classify import *
def get_node_by_url_name(url_name):
	return connection.Node.find_one({'url':url_name})	

def inc_topic_num_by_node_url_name(name):
	# only update the first one
        # because url is uniqu
	connection[config.classify_database][config.collection_name.Node].update(
		{'url':name}, 
		{ '$inc':{"topic_num":1} } 
	)
def get_all_node():
	return connection.Node.find().sort('create_time')

def find_a_node(node_id):
	return connection.Node.find_one({'_id':bson.objectid.ObjectId(node_id)})

def update_node_classify_info(classify_info):
	connection[config.classify_database][config.collection_name.Node].update(
		{'classify_ref':classify_info._id},
		{
		 '$set':{
				'classify_ref'	:	classify_info._id,
				'classify_name'	:	classify_info.name,
				'classify_url'	:	classify_info.url
			}
		},
		multi=True
	)
def update_a_node(node_info,web_info):
	try:
		# first
		classify_item	=	find_a_classify(web_info.classify_id)
		if not classify_item:
			return (False,-2)

		#second
		connection[config.classify_database][config.collection_name.Node].update(
		{'_id':node_info._id},
		{
	 	'$set':{
			 'url'			:	web_info.url,
			 'name'			:	web_info.name,
			 'header'		:	web_info.header,
			 'classify_ref'		:	classify_item._id,
			 'classify_name'	:	classify_item.name,
			 'classify_url'		:	classify_item.url
		       }
		},
		safe=True
		)

		#third
		update_classify_node_num(str(node_info.classify_ref),-1)
		update_classify_node_num(str(web_info.classify_id),1)

		#forth

	
	except pymongo.errors.DuplicateKeyError:
		return (False,-1)

	return (True,0)

	
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
	update_classify_node_num(info.classify_id,1)
	return (True,0)

if __name__ == "__main__":
	node = get_node_by_url_name("")
	print node
	#inc_topic_num_by_node_url_name("begin")
