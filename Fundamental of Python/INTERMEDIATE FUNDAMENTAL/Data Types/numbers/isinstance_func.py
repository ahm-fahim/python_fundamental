import decimal
a = 5
print(type(a))
print(type(5.0))
c = 5 + 4j
print(isinstance(c,complex))
print(0b1101011)
print(0xFB + 0b10)
print(0o15)

#type conversion
a = 1+4.0
print(a)
print(type(a))
print(int(a))

#Decimal

a = 2.2 + 2.2
b = 4.4
print(a==b)
print(decimal.Decimal(b))