from model import *

def add_member_test():
	member = connection.Member.find_one();
	print member
	topic  = connection.Topic()
	topic["author_ref"] = member["_id"]
	topic.save()


if __name__ == "__main__":
	add_member_test()
