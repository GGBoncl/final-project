import os
class store():
    def __init__(self):
        self.name = "Jason"
        self.title = ""
        self.price = 0 
        self.book = {}
        
    def Add(self):
        self.title = input("enter the name of the book you want to add\n")
        self.author = input("enter the author of the book you want to add\n")
        self.price = float(input("Enter the listing price if the book\n"))
        print("You have added", self.title)
        print("Please correct number")
        self.book[self.title] = {"author" : self.author, "price":self.price}
        print(self.book)
    
    def remove(self):
        self.title = input("enter the name of the book you want to remove\n")
        try:
            str(self.title)
            if self.title in self.book:
                del self.book[self.title]       
                print(self.book)
        except:
            print("please check the book name")
        
    def show(self):
        for x in self.book:
            print(x)
            print(self.book[x]["author"])
            print(self.book[x]["price"])
            print("")
    
    def save(self):
        name = input("Enter the name for you file\n")
        try:
            with open (name, "w") as f:
                for x in self.book: 
                    self.author = self.book [x]["author"]
                    self.price = self.book [x]["price"]
                    f.write(f"Book name: {x}\nAuthor: {self.author}\nPrice: {self.price}\n\n")
            print("It's done")
        except:
            print("error")

    def load(self):
        ask = input("Whic file do you want to find\n")
        try:
            f = open(ask)
            print(f.read())
        except:
            print("error")

    def delete(self):
        wen = input("What file you want to delete\n")
        if os.path.exists(wen):
            os.remove(wen)
        else:
            print("The file does not exist\n")
        