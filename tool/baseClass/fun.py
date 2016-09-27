import time
debug	= True
file	= False
def msg(msg,t=0):
	if debug == False:
		return
	_type = ['[OK]','[ERR]','[INFO]']
	try:
		print(_type[t] + str(msg))
	except:
		print("Info format wrong!")

def log(fun):
	def f(*args,**kargs):
		print("-------------------------")
		msg(fun.__name__ + "is Calling",2)
		t1 = time.time()
		fun(*args,**kargs)
		print("Used time:" + str(time.time() - t1))
		print("-------------------------")
	return f