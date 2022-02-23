def is_prime2(n):
    if n < 2:
        return False
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n,"is divisible by", x)
            prime = False
            return prime
        return prime
while True:
    number = int(input("Input(0 to exit):"))
    if number == 0:
        break
    prime = is_prime2(number)
    if prime is True:
        print(number,"is a prime number")
    else:
        print(number, "is not a prime nuber")

