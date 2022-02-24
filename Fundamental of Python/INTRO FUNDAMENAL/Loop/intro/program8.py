import re


result = 0
for num in range(101):
    if num % 5 == 0:
        print(num)
        result += num
    
print("Total = ",result)