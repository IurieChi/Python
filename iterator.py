for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("files/a.txt", encoding="UTF-8"):
    print(line, end='')

# Outputs: [range, tuple, set]
print("\n",list(map(type, (range(5), (0, 1, 2, 3, 4), {0, 1, 2, 3, 4}))) )

print(hasattr(range(5), "__iter__"), hasattr(tuple(), "__iter__"), hasattr(set(), "__iter__"))

iterator = range(5).__iter__() # let's iterate over object's iterator
while True:
    try:
        i = iterator.__next__() # call __next__() method explicitly
        print(i, end=" ") # Outputs: 0 1 2 3 4
    except StopIteration: # handle StopIteration exception explicitly
        break
    
# Here are two classes to create iterable objects and their iterators:
from collections import namedtuple
from typing import Iterator 

Page = namedtuple("Page", ["text", "number"]) 

class Book:
    def __init__(self) -> None:
        self.pages = []
    def add_page(self, text: str) -> None:
        self.pages.append( Page(text, number=len(self.pages) + 1) )
    def __iter__(self) -> Iterator[Page]:   # objects of class Book are iterable
        return BookIter(self)

class BookIter: 
    def __init__(self, book: Book) -> None: 
        self.pages = book.pages 
        self.book = book 
        self._cursor = 0        # keep the state of our iterator 
    def __iter__(self) -> "BookIter": 
        return self        # iterator should return the iterator object itself 
    def __next__(self) -> Page: 
        if len(self.pages) > self._cursor: 
            result = self.pages[self._cursor] 
            self._cursor += 1 
            return result       # iterator should return next item from the iterator 
        raise StopIteration # iterator should raise S

# Class LazyBook is inherited from Book and has __iter__() method that returns iterator of self.pages, or list iterator:
class LazyBook(Book):
    def __iter__(self) -> Iterator[Page]:
        return iter(self.pages)# list iterator may be used instead of BookIter

# Class Book has __iter__() method so objects of this class are iterable objects. __iter__() 
# returns an object of class BookIter. Class BookIter has __iter__() method that returns itself, __next__()
# method that returns next item from pages list, raise StopIteration when pages list is exhausted. So, 
# objects of class BookIter follow iterator protocol and are iterator objects.
# Let’s create a Book object and see that we can iterate over it:

book = Book()
for i in range(1, 5):
    book.add_page(f"page_{i}")
for page in book:
    print(page)

bookiter = iter(book)
print(next(bookiter))
print(next(bookiter))
print(next(bookiter))
print(next(bookiter))
# print(next(bookiter))

# Let’s create LazyBook object and iterate over it. The result is the same as in the previous example:
lazy_book = LazyBook()

for i in range(1, 5):
    lazy_book.add_page(f"page_{i}")

for page in lazy_book:
    print(page)

# Outputs: Page(text='page_1', number=1)
#                    Page(text='page_2', number=2)
#                    Page(text='page_3', number=3)
#                    Page(text='page_4', number=4)

print(type(iter(lazy_book)))   # Outputs: list_iterator

# sum function calls __next__() method of an iterable object and increase the resulting sum
# by received value until StopIteration is raised. So, the second attempt to call sum with an
# iterator object as an argument StopIteration is raised immediately and we have 0 as a result.
iterator = iter([1, 2, 3, 4])
print(sum(iterator))

# search the iterator
# When using in operator __contains__() method is being called first.
# If the object doesn't have __contains__() method but is iterable object __next__()
# method of its iterator is being called until the received value is equal to desired value or
# StopIteration exception is raised. So, the second attempt to find page_2 in iterator started from page_3 and failed.

print(list(book)) # Outputs: [Page(text='page_1', number=1), Page(text='page_2', number=2), Page(text='page_3', number=3), Page(text='page_4', number=4)] 

print(Page("page_2", 2) in book) # Outputs: True
print(Page("page_5", 5) in book) # Outputs: False

iterator = iter(book)
print(Page("page_2", 2) in iterator) # Outputs: True
print(Page("page_2", 2) in iterator) # Outputs: False
# there is only one page_2 in the book

