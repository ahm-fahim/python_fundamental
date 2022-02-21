items = (1,2,5.5,["A","B","c"],("apple","banana"))
print(items[3])
print(items[3][1])
print(items[4])
print(items[4][0])


print("All items in items tuple")
for item in items:
    print(item," || ", type(item))

# we also make list from tuple items
tpl = (1,2,3)
print(tpl)
li = list(tpl)
print(li)