class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Issued")


class Library(Book):

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        print("\n===== LIBRARY BOOKS =====")

        if len(self.books) == 0:
            print("No books available.")
        else:
            for book in self.books:
                print()
                book.display()

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == 2:
            library.display_books()

        elif choice == 3:
            book_id = input("Enter book ID to issue: ")
            library.issue_book(book_id)

        elif choice == 4:
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)

        elif choice == 5:
            print("Exiting Library Management System!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid menu number.")
