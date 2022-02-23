import random 
number = random.randint(1, 1000)
attempts = 0

while True:
    input_num = int(input("Guess the number (between 1 and 1000): "))
    attempts += 1

    if input_num == number:
        print("yes, your guess is correct!")
        break
    if input_num > number:
        print("Incorrect! Please try to guess smaller number")
    else:
        print("Incorrect! Please try to guess a larger number")
print("you tried",attempts,"times to find the correct number")

