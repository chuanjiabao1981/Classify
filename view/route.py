# coding=utf-8
import web
from topic   import *
from node    import *
from main    import *
from upload  import *
from video   import *
from backend import *

urls = (
    '/topic/(.*)','TopicShow',
    '/newtopic/(.*)','NewTopic',
    '/go/(.*)','NodeList',
    '/','MainPage',
    '/upload','UploadVideo',
    '/videotopic/(.*)','VideoTopicShow',
    '/newvideo/(.*)','NewVideoTopic',
    '/backend/classify/add','ClassifyAdd',
    '/backend/classify/edit/([^/]+)','ClassifyEdit',
    '/backend/classify','Classify',
    '/backend/member','MemberOverView',
    '/backend/member/add','MemberAdd',
    '/backend/node','NodeOverView',
    '/backend/node/add','NodeAdd',
    '/backend/node/edit/([^/]+)','NodeEdit',
    '/backend/main','Backend',
    
)

app = web.application(urls, globals())

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
