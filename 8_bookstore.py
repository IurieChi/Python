

# Using composition to build complex objects
class Author():
    def __init__(self, fname,lname):
       self.fname = fname
       self.lname = lname

    # The __str__ function is used to return a user-friendly string
    def __str__(self) -> str:
       return f'author "{self.fname} {self.lname}"'


class Book():
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # double-underscore properties are hidden from other classes
    __booklist = None

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
            # for title in Book.__booklist():
            #     if title == book:
            #         print('Book already exist in a list')
        return Book.__booklist
    
    # the __eq__ method checks for equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to non-book type")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    # the "init" function is called when the instance is
    # created and ready to be initialized  
    def __init__(self, title, pages,price, booktype, author = None):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    
    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}, costs {self.price}$"
    
    # The __repr__ function is used to return a developer-friendly string
    # representation of the object
    def __repr__(self):
        return f"title={self.title}, {self.author},price={self.price}$"

    def setDiscount(self, amount):
        self._discount = amount

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

#  access the class attribute
print("Book types: ", Book.getbooktypes())

# create author instance
aut1 = Author('Leo','Tolstoy')
aut2 = Author('JD','Salinger')
aut3 = Author('Harper', 'Lee')
#  Create some book instances
b1 = Book("War and Peace", 1225, 39.95,"HARDCOVER",aut1)
b2 = Book("The Catcher in the Rye", 234, 29.95, "PAPERBACK",aut2)
b3 = Book("To Kill a Mockingbird", 400, 24.95, "PAPERBACK",aut3)


# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1.title)
thebooks.append(b2.title)
thebooks.append(b3.title)


#print(type(thebooks))
print('Available books')
for book in thebooks:
    print("  ",book)


print(b1)
# try setting the discount
#print(b2)
b2.setDiscount(0.25)
#print(f'Price for "{b2}"  -25% discount price is {round(b2.getPrice(),2)}$')


# # call function to __repr__
# print(repr(b2))