from node import *
from model import *
import config
def update_topic_node_info(node_id,collection_name):
	node = connection.Node.find_one({'_id':bson.objectid.ObjectId(node_id)})
	connection[config.classify_database][collection_name].update(
	 	{'node_ref':node._id},
	 	{
	 		'$set': {
				  	"node_url":node.url,
					"node_name":node.name
				}
	 	},
	 	multi=True
	)
	
def get_latest_topic(collection_name,node,skip,limit):
	if node:
		#topic_list= connection[config.classify_database][collection_name].find({"node_ref":node._id}).sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)
		topic_list = connection.Video.find({"node_ref":node._id}).sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)

	else:
		print "test"
		topic_list= connection[config.classify_database][collection_name].\
				find().sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)

	#print topic_list.explain()
	#for i in topic_list:
	#	print type(i)
	return topic_list

