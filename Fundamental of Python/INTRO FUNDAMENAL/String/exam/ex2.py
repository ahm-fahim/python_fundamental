str = input("String :")
result = ''.join([ str[x:x+2][::-1] for x in range(0, len(str), 2) ])
print(result)

