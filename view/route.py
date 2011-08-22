# coding=utf-8
import web
from topic   import *
from node    import *
from main    import *
from upload  import *
from video   import *
from backend import *
from login   import *
from demo    import *
from member  import *

urls = (
    '/topic/(.*)','TopicShow',
    '/newtopic/(.*)','NewTopic',
    '/go/(.*)','NodeList',
    '/','MainPage',
    '/uploadsizeerror','UploadSizeError',
    '/upload','UploadVideo',
    '/uploadimage','UploadImage',
    '/videotopic/(.*)','VideoTopicShow',
    '/newvideo/(.*)','NewVideoTopic',
    '/login','Login',
    '/backend/classify/add','ClassifyAdd',
    '/backend/classify/edit/([^/]+)','ClassifyEdit',
    '/backend/classify','ClassifyOverView',
    '/backend/member','MemberOverView',
    '/backend/member/add','MemberAdd',
    '/backend/member/edit/([^/]+)','MemberEdit',
    '/backend/member/edit/avatar/([^/]+)','SetAvatarBackend',
    '/backend/node','NodeOverView',
    '/backend/node/add','NodeAdd',
    '/backend/node/edit/([^/]+)','NodeEdit',
    '/backend/main','Backend',
    '/setavatar','SetAvatar',
    '/demoget','DemoGet',
    '/demopost','DemoPost',
    
)

app = web.application(urls, globals())

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
