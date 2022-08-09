dic={1:"me",2:"you",3:"she"}
print(dic[1])
print(dic[2])
print(dic[3])
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get(1))
print(dic.get(2))

dic.update({4:"he"})
print(dic)
dic["5"]="I"
print(dic)
dic.pop(1)
print(dic)
dic.popitem() #remove last item
print(dic)
del dic[2]
print(dic)
dic.clear()
print(dic)
