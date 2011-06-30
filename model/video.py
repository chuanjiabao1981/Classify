# coding=utf-8
from model import *
from node  import *
from member import *
from default import *
import bson.objectid
import datetime
import config

def process_tag(tags):
	return tags

def video_verify(location):
	return true;

def video_image(video):
	return true;

def video_move(video):
	# move vidoe 
	#  image
	# del temp
	return true;
def process_video(video):
	"""ffmpeg -y -i $1 -ss 5 -s 160x90 -vframes 1 -an -sameq -f image2 $2_small.jpg"""
	if video.status != video_status_wait_process:
 		return
	if not video.location  || video.location.strip() == '':
		video.fail_reason = "video location is null";
		return 
	if not video_verify(video.location):
		video.fail_reason = "video verify fail"
		return
	if not video_image(video):
		video.fail_reason = "video produce image error"
		return
	if not video_move(video):
		video.fail_reason = "video move fail"
		return

	
	
	
def add_a_new_video(node,member,webinput):
	video = connection.Video();
	video.title		=	webinput.title()
	video.content   	=       webinput.content()
	video.content_length	=	len(video.content)
	video.node_url		=	node.url
	video.node_name		=	node.name
	video.node_ref		=	node._id
	video.author		=	member.name
	video.author_ref	=	member._id
	video.location		=	webinput.file_location()
	video.tags		=	process_tag(tags)
	video.save()
	return video

