while True:
    n = int(input("num: "))
    if n < 0:
        print("Want Positive")
        continue
    if n == 0:
        break

    print("square of", n, "is", n*n)
