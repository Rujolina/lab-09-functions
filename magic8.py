userinput = input("Give me a number (1 - 10) and i'll give you a fortune!  ")
usernum = (int(userinput))
i = 0
if i in usernum > 10:
    print("You'll have a super day today!")

elif i in usernum > 7:
    print("Something interesting will happen today!")
else:
    for i in usernum:
        if i < 4:
            i = i - 1
    print("Watch out! I sense some clumsiness!")
