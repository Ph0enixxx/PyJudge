import redis
import sys
import io
import fun
import json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


class Data(object):
	"""Data Middle class for Redis"""
	__slots__ = ('hashName','redis','status')
	def __init__(self,domain="127.0.0.1",secret="",db=0,port=6379,hashName="judge"):
		try:
			self.hashName = hashName
			self.redis = redis.Redis(host=domain,port=port, db=db,decode_responses=True)
		except:
			fun.msg("Data init error",1)
	def set(self,key,value):
		status = self.redis.hset(self.hashName,key,value)
		return status
	def get(self,key):
		try:
			return self.redis.hget(self.hashName,key).decode('ascii')
		except:
			try:
				return self.redis.hget(self.hashName,key).decode('utf-8')
			except:
				return self.redis.hget(self.hashName,key)
	def getAll(self):
		try:
			return self.redis.hgetall(self.hashName)
		except:
			fun.msg(getAll.__name__ + "error",1)
			return None
	def json_decode(self,code):
		return json.loads(code)
		pass

	def json_encode(self,obj):
		return json.dumps(obj)
		pass

	def test(self):
		#self.redis.set('aaa','123')
		self.set('aaa','213')
		print(self.get('aaa'))
		print(self.get('aa'))
		print(self.set('bbb','啊啊啊'))
		print(self.get('bbb'))
		print(self.getAll())
		s = self.json_encode(self.getAll())
		print(s)
		print(self.json_decode(s))
if __name__ == '__main__':
	a = Data()
	a.test()