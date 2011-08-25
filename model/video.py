# coding=utf-8
from model import *
from node  import *
from member import *
from default import *
from reply import *
import bson.objectid
import datetime,time
import config
import os,shutil

def process_tag(tags):
	return tags

def video_verify(location):
	##'file_content_type': u'video/mp4"'
	## if md5 is same return False
	return True
def video_time(video):
	return True

def video_image(video):
	## 在正确的目录下生成缩略图
	image_file_name = config.video_setting.image_path+'/'+video.video_md5 
	cmd = "/usr/bin/ffmpeg -y -i " + \
	      video.location + " -ss " + \
	      str(video.image_time)    + \
	      " -s " + config.video_setting.image_small + " -vframes 1 -an -sameq -f image2 "+image_file_name+"_small.jpg"
	re	=	os.system(cmd)
	if re !=0 :
		video.fail_reason = u"video image samll process fail!";
		return False

	cmd = "/usr/bin/ffmpeg -y -i " + \
	      video.location + " -ss " + \
	      str(video.image_time)    + \
	      " -s " + config.video_setting.image_big + " -vframes 1 -an -sameq -f image2 "+image_file_name+"_big.jpg"
	re	=	os.system(cmd)
	if re !=0 :
		video.fail_reason = u"video image big process fail!";
		return False

	video.image = video.video_md5
	return True;

def video_move(video):
	video_name = video.video_md5
##################这里不应该完全是mp4#########################################
##############################################################################
	video_name =  config.video_setting.video_path+'/'+video_name+".mp4";
	shutil.move(video.location,video_name)
	video.location = video.video_md5
	return True;

def process_video(video):
	if video.status != video_status_wait_process:
 		return
	if not video.location  or video.location.strip() == '':
		video.fail_reason = u"video location is null";
		return 
	if not video_verify(video.location):
		video.fail_reason = u"video verify fail"
		return
	if not video_time(video):
		video.fail_reason = u"video cal time fail"
		return
	if not video_image(video):
		return
	if not video_move(video):
		video.fail_reason = u"video move fail"
		return
	video.status = video_status_wait_published

	return

	

	
	
def add_a_new_video(node,member,webinput):
	video = connection.Video();
	# webinput引用的字段都是必须要有的
	video.title		=	webinput.title
	video.content   	=       webinput.content
	video.content_length	=	len(video.content)
	if webinput.image_time.isdigit():
		video.image_time	=	int(webinput.image_time)
	video.node_url		=	node.url
	video.node_name		=	node.name
	video.node_ref		=	node._id
	video.author		=	member.name
	video.author_ref	=	member._id
	video.author_avatar	=	member.avatar
	video.location		=	webinput.file_path
	video.tags		=	process_tag(webinput.tags)
	video.video_md5		=	webinput.file_md5
## 这个过程应该放在后台任务
	process_video(video)
	video.save()
	return video

def find_video_topic_by_id(topic_id):
	return connection.Video.find_one({'_id':bson.objectid.ObjectId(topic_id)})

def find_latest_video_topics_in_the_node(node):
	return connection.Video.find({'node_ref':node._id}).sort([('last_reply_time',-1)])

def hit_video_topic_by_topic_id(topic_id):
	connection[config.classify_database][config.collection_name.Video].update(
		{'_id':bson.objectid.ObjectId(topic_id)},
		{ '$inc':{"view_num":1}}
	)
def reply_to_topic(web_info,member,topic):
	reply_time	= datetime.datetime.utcnow()
	add_a_reply(web_info,member,topic)
	connection[config.classify_database][config.collection_name.Video].update(
		{'_id':topic._id}, 
		{ '$inc':{"reply_num":1} ,
		  '$set':{"last_reply_by":member.name,"last_reply_time":reply_time}
		
		} 
	)

def page_video_topic_(node,skip,limit):
	
	topic_list= connection.Video.find({"node_ref":node._id}).sort([("last_reply_time",pymongo.DESCENDING)]).skip(skip).limit(limit)
	#print topic_list.explain()
	return topic_list
	

##这个是传说中的优化版本
def page_video_topic(node,timestamp,pagenum):
	###
	### 最终生产环境用这个
	### print datetime.datetime.utcfromtimestamp(k).timetuple()
	### #############
	"""
		timestamp:0 是第一页
	"""

	if timestamp == 0:
		con    = {	"node_ref"		:	node._id}	
	else:
		con    = {
				"node_ref"		: node._id,
				"last_reply_time"	: {"$lt" : datetime.datetime.fromtimestamp(timestamp)}
		 	 }
	all_set=connection.Video.find(con).sort([("last_reply_time",pymongo.DESCENDING)]).limit(pagenum)
	##这个需要研究下到底用的哪个索引
	##print all_set.explain()
	#for i in all_set:
	#	print i.last_reply_time
	return all_set
	
	

class video_test:
	def __init__(self):
		self.location 		= '/var/tmp/upload_video/2/0000000002'
		self.image_time		= 5
		self.video_md5		= 'xxrrrdddssss'
	def test_page(self):
		node			= get_node_by_url_name("beginbegin")
		#node			= get_node_by_url_name("a")
		                     #1309596238.0
		#page_video_topic(node,1609595790.0,2)
		timestamp		= 1309655764.0
		timestamp		= 0
		page			= 0
		while True:
			print "====="+str(timestamp)+"======"
			all_set		= page_video_topic(node,timestamp,10)
			if all_set.count() == 0:
				break
			print "page" + str(page+1)+"\t"+str(timestamp)
			page	=page+1
			num 	= 0
			for i in all_set:
				num = num+1
				#print i
				#print time.mktime(i.last_reply_time.timetuple())
				#timestamp = time.mktime(i.last_reply_time.timetuple())
				print all_set[num-1]
				print str(num)+"\t"+str(timestamp)
		"""
		for i in find_latest_video_topics_in_the_node(node):
			#print i.last_reply_time.timetuple()
			k = time.mktime(i.last_reply_time.timetuple())
			print k
			###最终生产环境用这个
			#print datetime.datetime.utcfromtimestamp(k).timetuple()
			#print datetime.datetime.fromtimestamp(k).timetuple()
		"""



if __name__ == '__main__':
	"""
	a = video_test ()
	if video_image(a):
		print "ok"
		print a.image
		print a.location
		#video_move(a)
		print a.location
	"""	
	m	= video_test()
	m.test_page()
