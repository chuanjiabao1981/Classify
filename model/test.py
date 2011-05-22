from model import *

if __name__ == "__main__":
	m = connection.Member()
	for member in connection.Member.find():
		print member
