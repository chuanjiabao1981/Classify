from model import *
def get_member_by_name(name):
	return connection.Member.find_one()	

if __name__ == '__main__':
	print get_member_by_name("").name
	
