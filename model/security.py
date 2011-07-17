#coding=utf-8
from pyDes import *
from config import *

def encrypt_data(data):
	k = des(security.key,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5)	
	d = k.encrypt(data)
	return d
def dencrypt_data(en_data):
	k = des(security.key,CBC,"\0\0\0\0\0\0\0\0",pad=None,padmode=PAD_PKCS5)
	d = k.decrypt(en_data)
	return  d

if '__main__' == __name__:
	s = encrypt_data("123:321")
	print dencrypt_data(s)
