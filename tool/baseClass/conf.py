from data import Data
def C(key,value="__SETT__"):
	d = Data(hashName="conf")
	if value == "__SETT__":
		return d.get(key)
	else:
		return d.set(key,value)

if __name__ == '__main__':
	C("111","222")
	print(C("111"))