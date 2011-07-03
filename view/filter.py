# coding=utf-8
def linebreaksbr(text):
	return text.replace("\r\n","<br/>").replace("\n","<br/>").replace("\r","<br>")
def htmlspace(text):
	return text.replace(" ","&nbsp;");
## mako filter 带参数
def avatar(arg):
	def filter(text):
    		default = "/static/img/avatar_" + str(arg) +".png"
		return '<img src="' + default + '" border="0" />'  
		return default
	return filter

def video_image(arg):
	def filter(text):
		default = "/static_file/video_img/"+text+"_"+arg+".jpg"
		return default
	return filter

def float2int(arg):
	return "%d"%(float(arg))

if __name__=="__main__":
	print linebreaksbr("a\r\nb")
	print htmlspace("   ab  ")
	print avatar("normal")("xx")
