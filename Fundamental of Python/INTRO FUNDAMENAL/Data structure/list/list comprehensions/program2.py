li = [1,2,3,4,5,6,7,8,9,10]
even_number = []
for x in li:
    if x%2 == 0:
        even_number.append(x)

print(even_number)

#lets try it list comprehensions
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even_number = [x for x in range(1,16) if x % 2 == 0]
print(even_number)


