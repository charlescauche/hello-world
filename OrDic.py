class OrDic():
	def __init__(self, *dic, **args):
		self.keys = []
		self.values = []
		if len(dic)==1 and type(dic[0])==dict : #the *dic is a dictionary
			dic = dic[0]
			for i,j in dic.items():
				self.keys.append(i)
				self.values.append(j)
			print("New object created from a dictionary")
		else : #the arg is not a dictionary
			for i,j in args.items():
				self.keys.append(i)
				self.values.append(j)
			print("New object created from key/value")

	def __repr__(self):
		text_list = []
		for i in range(len(self.keys)) :
			text_list += ["{}: {}".format(self.keys[i],self.values[i])]
		text = "{" + ", ".join(text_list) + "}"
		return text
		

	def __getattr__(self, key) :
		if key in self.keys:
			index = self.keys.index(key)
			return self.values[index]
		else :
			return "sorry, this value does not exist in the OrDic"

	# def __setattr__(self,key, value)
	# 	if key in self.keys:
	
	def __getitem__(self,key) :
		if key in self.keys:
			index = self.keys.index(key)
			return self.values[index]
		else :
			return "sorry, this value does not exist in the OrDic"

	def __setitem__(self,key,value) :
		if key in self.keys: # if key already exist, then i update the existing value
			index = self.keys.index(key)
			self.values[index] = value
			print("Value updated for key :", key)
		else : # if key does not exist, then i add the value to the OrDic
			self.keys.append(key)
			self.values.append(value)
			print("New key/value created :", key, " / ",value)

	def __delitem__(self, key):
		if key in self.keys: 
			index = self.keys.index(key)
			del self.keys[index] 
			del self.values[index]
			print("Key/value deleted")
		else : 
			print("This key does not existe in this dictionnary")

	def __contains__(self, key):
		if key in self.keys :
			return True
		else :
			return False

	def __len__(self):
		return len(self.keys)

	def sort(self):
		new_keys = sorted(self.keys)
		new_values = []
		for i in new_keys:
			new_values += [self[i]]
		self.keys = new_keys
		self.values = new_values

	def reverse(self):
		new_keys = sorted(self.keys, reverse=True)
		new_values = []
		for i in new_keys:
			new_values += [self[i]]
		self.keys = new_keys
		self.values = new_values

	def keys(self):
		return 1



		


#Testins my class

print("-----------------")
print("Test 1")
a = OrDic()
#a["a"]=2
print(a)
print("-----------------")

print("-----------------")
print("Test 2")
d={"a":1,"b":2,"c":3,"d":4}
d.items()
b= OrDic(d)
print(b)
print("-----------------")

print("-----------------")
print("Test 3")
c = OrDic(a=1,b=2,c=3,d=4)
print(c)
print(c.c)
print(c["c"])
print("-----------------")

print("-----------------")
print("Test 4")
c = OrDic(a=1,b=2,c=3,d=4)
print(c)
print(c.c)
print(c["c"])
print("-----------------")

print("-----------------")
print("Test 4")
print("The object c has a length of :",len(c))
c["b"]=20
c["e"]=5
c["w"] =7
c["j"] =9 
print("The object c has a length of :",len(c))
del c["b"]
del c["f"]
print(c)
print("a" in c)
print("b" in c)
print("The object c has a length of :",len(c))
print(c)

print("-----------------")
print("Test 5")
c.sort()
print(c)
c.reverse()
print(c)
