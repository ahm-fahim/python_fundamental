s = "fahim"
print(len(s))
s = ''
print(len(s))
s = "fahim's garden"
print(s)
s = 'fahim\'s diary'
print(s)
s = "Fahim"
print(s[0])
print(s[1])
print(s[2])
print(s[4])

print("\nloop\n")
for i in s:
    print(i)


li = ['P','Y','T','H','O','N']
print(li)
li[0] = 'p'
print(li)

#but we can't change string item by indexing
#for this reasons string is a immutable / non-mutable value

first_name = "fahim"
last_name = " morshed"

full_name = first_name + last_name
print(full_name)

num1 = "10"
num2 = "10"
sum = num1 + num2
print(sum)

