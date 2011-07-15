from model import *

ADMIN			=	0
UPLOAD_VIDEO		=	1

def get_member_by_name(name):
	return connection.Member.find_one()	

if __name__ == '__main__':
	print get_member_by_name("").name
	
