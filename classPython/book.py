
class Book:
    def __init__(self, title, author, year) :
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self) :
        if self.available :
            """
            Marks the book as borrowed
            """
            self.available = False
            return f"'{self.available}' is currently NOT available."

        def return_book(self) :
            """
            Marks the book as returned
            """
            self.available = True
            return f"'{self.title}' has been returned."

        def get_details(self) :
            """
            Returns formatted book info
            """
            return f"{self.title} by {self.author} {self.year}"
