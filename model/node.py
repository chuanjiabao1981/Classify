from model import *
def get_node_by_url_name(name):
	return connection.Node.find_one()	


if __name__ == "__main__":
	node = get_node_by_url_name("")
	print node.node_url
