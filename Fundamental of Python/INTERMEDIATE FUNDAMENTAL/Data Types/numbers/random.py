import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

print(random.choice(x))
random.shuffle(x)
print(x)
print(random.random())