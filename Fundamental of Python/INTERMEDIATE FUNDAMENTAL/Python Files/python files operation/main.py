# f = open("massage.txt","r")
# content = f.read()
# print(content)

# more_content = f.read(10)
# print(more_content)
# f.close()

# try:
#     f = open("massage.txt","r")
#     content = f.read()
#     print(content)

#     more_content = f.read(10)
#     print(more_content)
# finally:
#     f.close()

with open("massage.txt","r") as f:
    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)

