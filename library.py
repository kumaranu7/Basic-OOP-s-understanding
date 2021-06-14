class Library:
    def __init__(self, listofbooks):
        self.available_books= listofbooks
    def Displaybooks(self):
        print()
        print('Avaiable books:')
        for i in self.available_books:
            print(i)
    def Lendbooks(self, requestedBook):
        if requestedBook in self.available_books:
            print("You have borrowed the book")
            self.available_books.remove(requestedBook)
        else:
            print("Please enter the correct bookname")
        
    def Update_books(self, returnedbook):
        self.available_books.append(returnedbook)
        print("You have returned the book")
    
class Customer:
    def Borrow_book(self):
        print('Enter the book you would like to borrow')
        self.book = input()
        return self.book

    def Return_book(self):
        print("Enter the book you would like to return")
        self.book = input()
        return self.book
        
library = Library(['Intelligent Investor', 'One Up on Wall Street', 'CPR and Pivot Points'])
customer = Customer()
while True:     
    print("\n")     
    print('Enter 1 to display books')
    print('Enter 2 to lend books')
    print('Enter 3 to return books')
    print('Enter 4 to exit')

    userchoice = int(input())

    if userchoice is 1:
        library.Displaybooks()
    elif userchoice is 2:
        requestedbook = customer.Borrow_book()
        library.Lendbooks(requestedbook)
    elif userchoice is 3:
        returnedbooks = customer.Return_book()
        library.Update_books(returnedbooks)
    elif userchoice is 4:
        quit()