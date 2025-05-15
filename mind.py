import os

class Store():
    def __init__(self):
        self.name = "Jason"
        self.book = {}  

    def Add(self):
        title = input("Enter the name of the book you want to add:\n")
        author = input("Enter the author of the book:\n")
        try:
            price = float(input("Enter the listing price of the book:\n"))
        except ValueError:
            print("Invalid price format.")
            return

        self.book[title] = {"author": author, "price": price}
        print(f"You have added: {title}")

    def Remove(self):
        title = input("Enter the name of the book you want to remove:\n")
        if title in self.book:
            del self.book[title]
            print(f"{title} has been removed.")
        else:
            print(f"No such book: {title}")

    def Show(self):
        if not self.book:
            print("No books in store.")
            return
        for title, info in self.book.items():
            print(f"Book name: {title}, author: {info['author']}, price: {info['price']}")

    def Save(self):
        name = input("Enter the name for your file:\n")
        try:
            with open(name, "w") as f:
                for title, info in self.book.items(): 
                    f.write(f"Book name: {title}\nAuthor: {info['author']}\nPrice: {info['price']}\n\n")
            print("Books saved successfully.")
        except Exception as e:
            print("Error saving file:", e)

    def Load(self):
        ask = input("Which file do you want to load:\n")
        if not os.path.exists(ask):
            print("The file does not exist.")
            return
        try:
            with open(ask, "r") as f:
                lines = f.readlines()
                for i in range(0, len(lines), 4):
                    title = lines[i].strip().replace("Book name: ", "")
                    author = lines[i+1].strip().replace("Author: ", "")
                    price = float(lines[i+2].strip().replace("Price: ", ""))
                    self.book[title] = {"author": author, "price": price}
            print("Books loaded successfully.")
        except Exception as e:
            print("Error loading file:", e)

    def Delete(self):
        filename = input("What file do you want to delete:\n")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} has been deleted.")
        else:
            print("The file does not exist.")