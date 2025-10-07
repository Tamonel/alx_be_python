class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"'{self.title}' was not checked out.")

    def is_available(self):
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

