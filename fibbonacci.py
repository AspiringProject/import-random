while True:
    amount = int(input("Enter the number of terms: "))

    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib = fibonacci()
    for i in range(amount):
        print(next(fib))