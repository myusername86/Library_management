#Library management system
class Book:
    def __init__(self, title, author, ISBN, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Available Copies: {self.available_copies}\n")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_info()


# Creating book objects
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", 10)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 5)
book3 = Book("1984", "George Orwell", "978-0-452-28423-4", 15)

# Creating library object
library = Library()

# Adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying information about books in the library
library.display_books()


