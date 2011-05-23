#coding=utf-8
from pymongo import Connection

##
version			= ('0','1','0')
##
debug			= True
##数据库配置
mongodb_host 		= "127.0.0.1"
mongodb_port 		= 27017
## 数据库名称
if debug:
	classify_database	= "shitao_debug"
else:
	classify_database	= "shitao"

