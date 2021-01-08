#parent class or base class
#child class or derived class

# object class is the parent class for all the classes

class Dummy:
    """
    This is a class
    By default it inherits object class
    """
    pass

d1 = Dummy()

class Book:

    def __init__(self, author, book_name, price):
        self.author_name = author
        self.book_name = book_name
        self.price = price

    def get_details(self):
        return f"""author : {self.author_name}
book: {self.book_name}
cost: {self.price}"""

    def search_by_author(self, author_name):
       pass

    def read(self):
        print("I can read")

book1 = Book("Charles Dickinson", "Tale of Two Cities", "$20")
print(book1.get_details())

class FictionBook(Book): #simple or single inheritance
    def fiction_series(self):
        pass

fb = FictionBook("Martin", "Return of Xavier", "$10")
print(fb.get_details())

class NoteBook:
    def __init__(self, pages, isRuled = True):
        self.pages = pages
        self.isRuled = isRuled

    def write(self):
        print("I can write")

class ExerciseBook(Book, NoteBook): # multiple inheritance
    pass


#Method Resolution Order(MRO)


eb = ExerciseBook()


class ScienceFiction(FictionBook): # multi level
    pass

sf = ScienceFiction("author", "name", "$10")
sf.fiction_series()
sf.get_details()




