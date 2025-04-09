from book import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book) :
        self.books.append(book)
    def list_books(self):
        return (book.get_details() for book in self.books)

    def find_book(self, title) :
        for book in self.books :
            if book.title.lower() == title.lower():
                return book
            return None
