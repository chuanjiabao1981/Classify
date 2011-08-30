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
		topic_list = connection.Video.find({"node":node.get_dbref()}).sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)
	else:
		topic_list = connection[config.classify_database][collection_name].\
				find().sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)

	#print topic_list.explain()
	#for i in topic_list:
	#	print type(i)
	return topic_list

if __name__ == '__main__':
	#all = get_latest_topic(config.collection_name.Video,None,0,config.page_num)
	all = connection["shitao_debug_2"]["video"].find()
	alld = connection["shitao_debug_2"]["video"]
	
	#all = connection.Video.find()
	all = alld.find()
	for i in all:
		print type(i["node"])
