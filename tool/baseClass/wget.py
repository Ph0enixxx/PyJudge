import requests as req
import sys
import io
import fun
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# def getShort(string):
#     text = req.head("http://t.cn/" + str(string))
#     head = text.headers
#     #print(head)
#     try:
#         if head['location'] == 'http://weibo.com/sorry':
#             return None
#         return head['location']
#     except:
#         return None
class Wget(object):
	__slots__ = ('__session')
	def __init__(self):
		try:
			self.__session = req.session()
		except:
			fun.msg("Construct Wget object failed..",1)
			sys.exit(1)
	@fun.log
	def get(self,url,**args):
		rq = self.__session
		res = rq.get(url,**args)
		return res.text
	def post(self,url,headers=None,data=None):
		rq = self.__session
		res = rq.get(url,headers=headers,data=data)
		return res.text
		pass
	pass

if __name__ == '__main__':
	w = Wget()
	print(w.get("http://baidu.com"))
#w.y = 1
#w.x = 1