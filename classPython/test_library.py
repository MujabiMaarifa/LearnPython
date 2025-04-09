from book import Book
from library import Library

lib = Library("Test Library")
lib.add_books(Book("Atomic Physics", "Kendric lamar", 2005))
lib.add_books(Book("Azure AI machine learning", "Microsoft", 2017))
print(lib)

print("Library catalog")
for book in lib.list_books() :
    print("\n", book)

found = lib.find_book("Deep work")
print(found.borrow()) if found else print("Woi hakuna kitabu kwa sasa")
