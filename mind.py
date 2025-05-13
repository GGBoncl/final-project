import os
class store():
    def __init__(self):
        self.name = "Jason"
        self.title = ""
        self.author = ""
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
        for self.title in self.book.items():
            print(f"Titile:{self.title},author : {self.author}, price:{self.price}")
    
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
        ask = input("Which file do you want to find\n")
        with open(ask, "r") as f:
            lines = f.readlines()
            for i in range(0,len(lines),4):
                self.title = lines[i].strip().replace("Title:","")
                self.author = lines[i+1].strip().replace("Author:","")
                self.price =float(lines[i+2].strip().replace("Price:",""))
                self.book[self.title] = {"author" : self.author, "price":self.price}
                

    def delete(self):
        wen = input("What file you want to delete\n")
        if os.path.exists(wen):
            os.remove(wen)
        else:
            print("The file does not exist\n")
        