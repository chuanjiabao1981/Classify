from model.node import *
from model.model import *
import config
def update_topic_node_info(node,collection_name):
	connection[config.classify_database][collection_name].update
	(
	 {'node_ref':node._id},
	 {
	 '$set':{"node_url":node.url,"node_name":node.name}
	 },
	 multi=True
	)
	

if __name__ == '__main__':
	print "hello"
	
