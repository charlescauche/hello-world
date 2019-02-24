class OrDic():
	def __init__(self, *dic, **args):
		self.keys_list = []
		self.values_list = []
		if len(dic)==1 and type(dic[0])==dict : #the *dic is a dictionary
			dic = dic[0]
			for i,j in dic.items():
				self.keys_list.append(i)
				self.values_list.append(j)
			print("New object created from a dictionary")
		else : #the arg is not a dictionary
			for i,j in args.items():
				self.keys_list.append(i)
				self.values_list.append(j)
			print("New object created from key/value")

	def __repr__(self):
		text_list = []
		for i in range(len(self.keys_list)) :
			text_list += ["{}: {}".format(self.keys_list[i],self.values_list[i])]
		text = "{" + ", ".join(text_list) + "}"
		return text
		

	def __getattr__(self, key) :
		if key in self.keys_list:
			index = self.keys_list.index(key)
			return self.values_list[index]
		else :
			return "sorry, this value does not exist in the OrDic"

	# def __setattr__(self,key, value)
	# 	if key in self.keys_list:
	
	def __getitem__(self,key) :
		if key in self.keys_list:
			index = self.keys_list.index(key)
			return self.values_list[index]
		else :
			return "sorry, this value does not exist in the OrDic"

	def __setitem__(self,key,value) :
		if key in self.keys_list: # if key already exist, then i update the existing value
			index = self.keys_list.index(key)
			self.values_list[index] = value
			print("Value updated for key :", key)
		else : # if key does not exist, then i add the value to the OrDic
			self.keys_list.append(key)
			self.values_list.append(value)
			print("New key/value created :", key, " / ",value)

	def __delitem__(self, key):
		if key in self.keys_list: 
			index = self.keys_list.index(key)
			del self.keys_list[index] 
			del self.values_list[index]
			print("Key/value deleted")
		else : 
			print("This key does not existe in this dictionnary")

	def __contains__(self, key):
		if key in self.keys_list :
			return True
		else :
			return False

	def __len__(self):
		return len(self.keys_list)

	def sort(self):
		new_keys = sorted(self.keys_list)
		new_values = []
		for i in new_keys:
			new_values += [self[i]]
		self.keys_list = new_keys
		self.values_list = new_values

	def reverse(self):
		new_keys = sorted(self.keys_list, reverse=True)
		new_values = []
		for i in new_keys:
			new_values += [self[i]]
		self.keys_list = new_keys
		self.values_list = new_values

	def keys(self):
		for i in self.keys_list:
			yield i

	def values(self):
		for i in self.values_list:
			yield i

	def items(self):
		for i in self.keys_list:
			yield i,self[i]





	#def __iter__





		


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


print("-----------------")
print("Test 6")
for i in c.keys():
	print(i)
for i in c.values():
	print(i)
c.sort()
for i in c.items():
	print(i)
