from mind import store
game = True
a = store()
print(a.name)
print("Welcome to the book store.")
while game:
    c = input("Would you like to input the book or you want to do other thing?\n1.Yes\n2.move\n3.show\n4.save\n5.load\n6.delete\n")
    if c == "1":         
        d = a.Add()
    elif c == "2""move":
        e = a.remove()
    elif c == "3":
        b = a.show()
    elif c == "4":
        f = a.save()
    elif c == "5":
        g = a.load()
    elif c == "6":
        h = a.delete()
    else:
        print("Please input the correct option")

