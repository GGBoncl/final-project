from mind import Store
game = True
a = Store()
print(a.name)
print("Welcome to the book store.")
while game:
    c = input("Would you like to input the book or you want to do other thing?\n1.Yes\n2.move\n3.show\n4.save\n5.load\n6.delete\n")
    if c == "1":         
        d = a.Add()
    elif c == "2":
        e = a.Remove()
    elif c == "3":
        b = a.Show()
    elif c == "4":
        f = a.Save()
    elif c == "5":
        g = a.Load()
    elif c == "6":
        h = a.Delete()
    else:
        print("Please input the correct option")

