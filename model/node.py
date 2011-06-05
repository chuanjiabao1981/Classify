from model import *
def get_node_by_url_name(name):
	return connection.Node.find_one()	

def inc_topic_num_by_node_url_name(name):
	# only update the first one
        # because url is uniqu
	connection[config.classify_database][config.collection_name.Node].update(
		{'url':name}, 
		{ '$inc':{"topic_num":1} } 
	)



if __name__ == "__main__":
	node = get_node_by_url_name("")
	print node
	#inc_topic_num_by_node_url_name("begin")
