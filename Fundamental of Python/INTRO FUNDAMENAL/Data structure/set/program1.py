a = set() #empty set
print(a) 
print(type(a))

items = {"pen", "laptop","cellphone"}
print(items)
print(type(items))

#we can make a set from tuple and list

li = [1,2,3,4]
tpl = (2,4,6)

new_set1 = set(li)
print(new_set1)
new_set2 = set(tpl)
print(new_set2)

#str to set
a = "bangladesh"
print(a)
b = set(a)
print(b)
print(type(b))

num = {1,2,3,4}
print(1 in num)
print(5 in num)

