def factorial(n):
    result = 1
    if n == 0:
        return 1
    elif n % 2 == 0:
        for i in range(1, int(n/2)+1):
            result *= 2*i
            result %= 10010101
    else:
        for i in range(1, int((n+1)/2)+1):
            result *= (2*i-1)
            result %= 10010101

    return result


if __name__ == '__main__':
    while True:
        try:
            a = int(input("Please, enter integer number between 1 and 100000: "))
        except ValueError:
            print("That aint no integer Nigga!")
            break

        if 0 <= a <= 100000:
            print(factorial(a))
            continue
        else:
            print("Number is not in requested range.")
            break

    pass
