
def factorial(num):
    total = 1
    for i in range(0, num , 1):
        total = total * (num - i)
        print("Current i is " + str(i))
        print("The current value of total is " + str(total))

    return total

userstring = input("Number please: ")
usernum = int(userstring)
print(factorial(usernum))
