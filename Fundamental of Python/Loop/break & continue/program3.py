from ast import operator


terminate_program = False
while not terminate_program:
    number1 = int(input("Num1: "))
    number2 = int(input("Num2: "))

    while True:
        operation = input("add/sub (0 to exit):")
        
        if operation == "quit":
            terminate_program = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown operation")
            continue
        if operation == "add":
            print("Result is", number1 + number2)
            break 
        if operation == "sub":
            print("Result is", number1 - number2)
            break