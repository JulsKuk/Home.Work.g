def square(x):
    return (4 * x, x ** 2, (2 * x ** 2) ** .5)


result = square(int(input("Введите сторону квадрата: ")))

print(result)