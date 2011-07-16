#coding=utf-8
video_status_wait_process 	= 0
video_status_wait_published	= 5
video_status_published	  	= 10


class MemberStatus:
	active				= 0
	StatusName			= {}
	StatusName[active]		= u"激活"

class MemberAuthority:
	##权限类型
	admin				= 0	#管理员标识
	upload_video			= 1	#是否可以上传视频
	reply				= 2	#是否可以回复topic
	loggin_backend			= 3	#是否可以登录后台管理
	edit_backend			= 4	#是否可以编辑后台数据

	##
	default_authority		= 1l<<reply
	
	##
	AuthorityName						= {}
	AuthorityName[admin]			= u'管理员'
	AuthorityName[upload_video]		= u'视频上传'
	AuthorityName[reply]			= u'评论'
	AuthorityName[loggin_backend]		= u'后台登录权限'
	AuthorityName[edit_backend]		= u'后台编辑权限'

	@staticmethod
	def build_authority(authority):
		v	=	MemberAuthority.default_authority
		if not authority:
			return v
		if "admin" in authority:
			v 	= v | 1l<<MemberAuthority.admin
		if "upload_video" in authority:
			v 	= v | 1l<<MemberAuthority.upload_video
		if "reply" in authority:
			v	= v | 1l<<MemberAuthority.reply
		if "loggin_backend" in authority:
			v	= v | 1l<<MemberAuthority.loggin_backend
		if "edit_backend" in authority:
			v 	= v | 1l<<MemberAuthority.edit_backend 
		return v
		
if __name__ == '__main__':
	print MemberAuthority.AuthorityName[MemberAuthority.admin]
	authority=	{}
	authority["admin"] = "1"
	authority["upload_video"]	= "2"
	authority["edit_backend"]	= "3"
	print MemberAuthority.build_authority(authority)
