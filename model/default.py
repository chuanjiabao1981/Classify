#coding=utf-8
video_status_wait_process 	= 0
video_status_wait_published	= 5
video_status_published	  	= 10


class MemberStatus:
	active				= 0
	StatusName			= {}
	StatusName[active]		= u"激活"

class MemberAuthority:
	admin				= 0	#管理员标识
	upload_video			= 1	#是否可以上传视频
	reply				= 2	#是否可以回复topic
	loggin_backend			= 3	#是否可以登录后台管理
	edit_backend			= 4	#是否可以编辑后台数据

	AuthorityName						= {}
	AuthorityName[admin]			= u'管理员'
	AuthorityName[upload_video]		= u'视频上传'
	AuthorityName[reply]			= u'评论'
	AuthorityName[loggin_backend]		= u'后台登录权限'
	AuthorityName[edit_backend]		= u'后台编辑权限'
if __name__ == '__main__':
	print MemberAuthority.AuthorityName[MemberAuthority.admin]
