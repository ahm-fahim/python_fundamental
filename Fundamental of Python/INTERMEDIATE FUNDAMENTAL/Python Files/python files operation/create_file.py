with open("create.txt", "r") as c: #w,r,a
    # c.write("I wanna write something here\n")
    # c.write("Above this line was written by me.")

    # c.write("\nThis line is also written by Me")

    lines = c.readlines()
    print(lines)