# li = [1,2,3,4]
# print("old list =",li)
# new_li = []
# for x in li:
#     new_li.append(2 * x)

# print("new list =",new_li)

#now try it with list comprehensions
li = [1,2,3,4]
new_li = [2 * x for x in li]
print(new_li)