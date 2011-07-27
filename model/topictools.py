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
	
