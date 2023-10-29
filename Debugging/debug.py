def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        # changing this line to include the last number
        for i in range(1, n-10+1):
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        # changing the below line to calculate the correct formula for sum of n natural number
        out = out + lim
        # it will always result in int so using int divition
        out = out // 2
    print(out)


n = int(input("Enter an integer: "))
compute(n)