from mind import store
game = True
a = store()
print(a.name)
while game:
    c = input("Would you like to input the book or you want to do other thing?\n1.Yes\n2.move\n3.Show\n4.save\n5.load\n")
    if c == "1":         
        d = a.Add()
    elif c == "2":
        e = a.remove()
    elif c == "3":
        b = a.show()
    elif c == "4":
        f = a.save()
    elif c == "5":
        g = a.load()
    else:
        print("Please input the correct option")

