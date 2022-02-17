str_value = input("String: ")

up_str = ''
low_str = ''
digit = ''
others = ''

for i in str_value:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        up_str += i
    if i in "abcdefghijklmnopqrstuvwxyz":
        low_str += i
    if i in "0123456789":
        digit += i
    else:
        total_str = (up_str + low_str + digit) 
        if i not in total_str:
            others += i
        
print(up_str)
print(low_str)
print(digit)
print(others)