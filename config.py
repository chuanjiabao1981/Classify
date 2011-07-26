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
class collection_name():
	pass;

collection_name.Topic		= 'topic'
collection_name.Reply		= 'reply'
collection_name.Node		= 'node'
collection_name.Member		= 'member'
collection_name.Video		= 'video'
collection_name.Classify	= 'classify'


### 模板相对的路径都是以view/template为前缀的
## 桌面模板 
template_desktop_path		= "desktop/"

class template():
	pass;
## 
template.chevron = u'<span class="chevron">&nbsp;›&nbsp;</span>' 
template.split   = u'<span class="snow">•</span>'
template.add_a_reply_now 	= u'现在添加一条回复'
template.reply		 	= u'回复'
template.till		 	= u'直到'
template.send		 	= u'回复'
template.create_new_topic 	= u"创建新主题"
template.total_topics 		= u'主题总数'
template.total_videos		= u'视频总数'
template.create			= u'创建'
template.no_reply		= u'目前尚无回复'
template.reply_content_cannot_be_empty	= u'回复内容不能为空'




class site():
	pass

## 网站名称
site.title			= u"视淘"
site.use_topic_types		= False

class video_setting():
	pass

####目录权限也可以通过，把webserver和uwsgi的用户组设为同一个解决
#这个必须要有写权限,上级目录必须要有执行权限
video_setting.image_path	= '/srv/www/shitao.com/public_html/static_file/video_img/'
## 这个目录最终要放在不可下载目录下,这个必须是绝对路径
#这个必须要有写权限,上级目录必须要有执行权限
video_setting.video_path	= '/srv/www/shitao.com/upload_video/'
video_setting.image_small	= '160x90'
video_setting.image_big		= '480x270'


class backend():
	class node():
		class field():
			pass
		pass
	class member():
		class field():
			pass
	pass

backend.node.title			= u'节点管理'
backend.node.add			= u'添加节点'
backend.node.edit			= u'编辑节点'
backend.node.field.url			= u'节点url'
backend.node.field.name			= u'节点名称'
backend.node.field.header		= u'节点header（用于展示）'
backend.node.field.topic_num		= u'节点包含的topic个数'
backend.node.field.classify_name	= u'节点所属类别'
backend.member.title			= u'用户管理'
backend.member.add			= u'添加用户'
backend.member.edit			= u'编辑用户信息'
backend.member.field.name		= u'用户名'
backend.member.field.register_time	= u'用户注册时间'
backend.member.field.email		= u'电子邮件'
backend.member.field.status		= u'用户状态'
backend.member.field.password		= u'密码'
backend.member.field.readme		= u'自我简介'


class security:
	pass
##这个必须是8个字符##
security.key				= '12345678'

class cookie:
	pass
##cookie 时间 单位s
cookie.period				= 3600

##页面个数
page_num				= 8 

if __name__ == "__main__":
	print site.title
	print backend.node.title
