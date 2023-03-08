# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # double-underscore properties are hidden from other classes
    __booklist = None

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or
    # class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

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
    def __init__(self, title, pages, author, price,booktype):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    def setDiscount(self, amount):
        self._discount = amount

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

#  access the class attribute
print("Book types: ", Book.getbooktypes())

#  Create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95,"HARDCOVER")
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95, "PAPERBACK")



# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1.title)
thebooks.append(b2.title)
#print(type(thebooks))
print('Available books')
for book in thebooks:
    print("  ",book)

print(f'Price for "{b1.title}" is {b1.getPrice()}$')
# try setting the discount
#print(f'Price for {b2.title} is {b2.getPrice()}$')
b2.setDiscount(0.25)
print(f'Price for "{b2.title}" is {round(b2.getPrice(),2)}$ with 25% discount')
