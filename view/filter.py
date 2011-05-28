def linebreaksbr(text):
	return text.replace("\r\n","<br/>").replace("\n","<br/>").replace("\r","<br>")
def htmlspace(text):
	return text.replace(" ","&nbsp;");
if __name__=="__main__":
	print linebreaksbr("a\r\nb")
	print htmlspace("   ab  ")
