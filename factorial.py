
def factorial(num):
    total = num
    if num == 0 and num == 1:
        return 1
    while num > 1:
        num = num - 1
        total = num * num
    return total

num = int(input("Number please: "))
print(factorial(num))
