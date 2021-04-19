A = []

for i in range(0,100,1):
    A.append(i)
    i = i + 1
    if (i % 2 == 0):
        print(str(i) + "no")
    else:
        print(str(i) + "yes")
