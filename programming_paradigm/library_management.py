class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()  # يرجع True عند النجاح
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()  # يرجع True عند النجاح
        return False

    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        for line in available_books:
            print(line)
