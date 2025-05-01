from mind import store
game = True
a = store()
print(a.name)
while game:
    c = input("Would you like to input the book? (yes or no)\n")
    if c == "yes":         
        d = a.Add()
    elif c == "no":
        x = input("Do you want to remove the book?(yes or no)")
        if x ==  "yes":
            e = a.remove()
        elif x == "no":
            print("Ok, bye")
            game = False
        else:
            print("please input yes or no")
    elif c == "show":
        b = a.show()
    else:
        print("please input yes or no")

