def iseven(x):
    if x > 10:
        iseven(x - 10)
    elif x == 2 or x == 4 or x == 6 or x == 8 or x == 10:
        print("Number is even!")
    else:
        print("Number is odd!")


iseven(9780)

