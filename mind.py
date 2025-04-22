class store():
    def __init__(self):
        self.name = "Jason"
        self.title = ""
    def Add(self):
        self.title = input("What book would you like to add\n")
        print("You have added", self.title)