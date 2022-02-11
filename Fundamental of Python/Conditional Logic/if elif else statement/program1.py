my_friends_list = ["Sadik", "Babu", "Afifa", "Akaid", "Tamjid", "Shakil"]

check = input("Name: ")

if check in my_friends_list:
    print(check, "is a my friend")
#👆 thats call indentation
# if we dont't indent , this show an error
# IndentationError: expected an indented block
else:
    print(check, "is not on my friend list")

print("Program terminated")