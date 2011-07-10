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
    '/backend/classify','Classify',
    '/backend/main','Backend',
)

app = web.application(urls, globals())

application = app.wsgifunc()
if __name__ == "__main__":
	app.run()
