a = "global"

def foo():
    print("a inside:",a)


foo()
print("a outside:", a)

x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()