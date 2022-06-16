
class Library:
    
    # constructor
    def __init__(self, list, name):
        # instance variables
        self.booklist = list
        self.name = name
        self.lendict = {}
        
    # instance method
    def displaybook(self):
        """
        Displays the books
        """
        
        print()
        print(f'We have following books in a library : \n{self.name} \n')
        for book in self.booklist:
            print(book)
    
    # instance method       
    def lendbook(self, user, book):
        """
        Lends the book in the library
        """
        
        if book not in self.lendict.keys():
            self.lendict.update({book : user})
            print("Lender-Book DataBase has been updated. You can take the book now.")
        else :
            print(f"Book is already being used by {self.lendict[book]}")
            
            
    def addbook(self, book):
        """
        Adds new book in the libarry
        """
        
        self.booklist.append(book)
        print('The book has been added to the book list.')
    
    def returnbook(self, book):
        """
        Returns the book in the library 
        """
        
        self.lendict.pop(book)
    
    
# object of the class
library = Library(['Python', 'Rich daddy poor daddy', 'library Potter', 'C++ basics', 'Algorithms by CLRS'], 'its-kind-of')


while(True):
    print()
    print(f'Welcome to the {library.name} library. Enter your choice to continue: ')
    print('1. Display Book')
    print('2. Lend a Book')    
    print('3. Add a Book')    
    print('4. Return a Book')
    print()
    user_choice = input()
    if user_choice not in ['1', '2', '3', '4']:
        print('Please enter a valid option :')
        continue
    else :
        user_choice = int(user_choice)
    
    if user_choice == 1:
        library.displaybook()
        print()
        
    elif user_choice == 2:
        book = input('Enter the name of the book you want to lend: ')
        user = input('Enter your name :')
        library.lendbook(user, book)
    
    elif user_choice == 3:
        book = input('Enter the name of the book you want to add: ')
        library.addbook(book)
    
    elif user_choice == 4:
        library.returnBook(book)
    
    else :
        print('invalid Choice :')
            
    print('Press q to quite and c to contine : ')
    user_choice2 = ''
    while(user_choice2 != 'c' and user_choice2 != 'q'):
        user_choice2 = input()
        if user_choice2 == 'q':
            break

        elif user_choice2 == 'c':
            continue
