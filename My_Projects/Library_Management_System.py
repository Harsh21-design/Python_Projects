# StudentLibraryManagement

class Library:
    def __init__(self, allbooks):
      self.books = allbooks

    def showAvailablebooks(self):
        print("Number of books available in libary are:")
        for book in self.books:
            print("        "+book)

    def borrowbook(self):
        take = input("Enter the book name you want to take or borrow: ")
        # self.take = take
        if  take in self.books: 
            self.books.remove(take)
            print(f"You have been issued '{take}'. Pls keep it safe and return in 15 days!!")
        else:
            print("This book is not available right now!! Thanks")
    
    def addorreturnbook(self):
        give = input("Enter the book name you want to add or return to library: ")
        self.give = give
        self.books.append(self.give)
        print("Thank you for adding/returning the book.")
    

if __name__ == "__main__":
    piemrlibrary = Library(["Python","C","C++","Mathematics 2","AI/ML","Data Science"])
    # piemrlibrary.showAvailablebooks()
    while(True):
        welcomemsg = '''
              ***** WELCOME TO THE CENTRAL LIBRARY OF PIEMR COLLEGE *****

              Please select an option 
              1. List all the books
              2. Request or Borrow a book
              3. Add or Return a book
              4. Exit the library
              '''
        print(welcomemsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            piemrlibrary.showAvailablebooks()
        elif a == 2:
            piemrlibrary.borrowbook()
        elif a == 3:
            piemrlibrary.addorreturnbook()
        elif a == 4:
            print("Thanks of using CENTRAL LIBRARY OF PIEMR COLLEGE. Good day Ahead!!")
            exit()
        else:
            print("Please select the valid options (1-4)!!")
