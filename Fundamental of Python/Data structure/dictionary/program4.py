dict = {"a":"A","b":"B", "c":"C"}
dict[(1,2,3)] = "tuple"
print(dict)

li = [1,2,4]
dict[li] = "list" #unhashable type: 'list'

s = {1,2,3,4}
dict[s] = "set" #unhashable type: 'set'