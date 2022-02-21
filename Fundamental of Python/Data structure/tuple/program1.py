x = (1,2,3,4)
print(type(x))
y = 1,3,5
print(type(y))

#empty tuple
z = ()
print(type(z))
a = 1
print(type(a)) #int 
b = 1,
print(type(b)) #tuple

# get tuple item by indexing
tpl = (1,2,3,4,5)
print(tpl[0])
print(tpl[2])

#tuple is not mutable . thats means immutable , so its value never change
# but list is mutable

# list
li = [1,2,3,4]
print(li)
li[0] = 10
print(li)

#tuple
tpl = (1,2,3,4)
print(tpl)
tpl[0] = 10 #Exception has occurred: TypeError
print(tpl)  #'tuple' object does not support item assignment





