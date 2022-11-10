stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]

stringlist = []
intlist =[]
boollist = []
floatlist = []

for x in stuff:
    if type(x) is str: 
        stringlist.append(x)
    if type(x) is int: 
        intlist.append(x)
    if type(x) is bool:
        boollist.append(x)
    if type(x) is float:
        floatlist.append(x)

print(stringlist)
print(intlist)
print(boollist)
print(floatlist)
