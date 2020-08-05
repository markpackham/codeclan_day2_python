import sqlite3
from collections import namedtuple
connection = sqlite3.connect("library.db")
cursor = connection.cursor()

Book = namedtuple("Book", ['id', 'title', 'author',
                           'published_year', 'is_loaned'])


def set_up_table():
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            published_year INTEGER,
            is_loaned BOOLEAN )
    """)
    connection.commit()

# SQLite doesn't have Boolean so we have to make do with 0 or 1
def insert_book(title, author, year):
    sql = """
        INSERT INTO books (title, author, published_year, is_loaned)
        VALUES ('{}', '{}', {}, 0)
    """.format(title, author, year)
    cursor.execute(sql)
    connection.commit()


def get_all_books():
    sql = "SELECT * FROM books"
    rows = cursor.execute(sql)
    return [Book(*book) for book in rows.fetchall()]


def search_for_book(title):
    sql = "SELECT * FROM books WHERE title='{}'".format(title)
    row = cursor.execute(sql)
    return Book(*row.fetchone())


def update_book_loan_status(title):
    book = search_for_book(title)
    if book.is_loaned == 0:
        new_loan_status = 1
    else:
        new_loan_status = 0
    sql = "UPDATE books SET is_loaned = {} WHERE id = {}".format(
        new_loan_status, book.id)
    cursor.execute(sql)
    connection.commit()


set_up_table()
insert_book("BookA", "AuthorA", 1800)
insert_book("BookA2", "AuthorA", 1801)
insert_book("BookB", "AuthorB", 1805)
insert_book("BookC", "AuthorC", 1806)
insert_book("BookD", "AuthorD", 1807)
insert_book("BookE", "AuthorD", 1808)
insert_book("BookE2", "AuthorD", 1809)

# Triple speech marks, """ lets your print entire paragraphs in tidy a formatted text style with line spacing - it is called a doc string (it explains what it does)
# You can make it a comment or an actual string simular to /* */ in JavaScript
while True:
    print("""
    Select an option:
    1. Display all books
    2. Search for a book by title
    3. Update book loan status
    """)

    choice = input()

    if choice == "1":
        all_books = get_all_books()
        for book in all_books:
            print("Book: {} by {}, {}".format(
                book.title, book.author, book.published_year))

    elif choice == "2":
        print("What book would you like to find?")
        title = input()
        book = search_for_book(title)
        print("Book: {} by {}, {}".format(
            book.title, book.author, book.published_year))
    else:
        print("What book would you like to update?")
        title = input()
        update_book_loan_status(title)
        book = search_for_book(title)
        print("Book: {} by {}, {}. Loan status: {}".format(
            book.title, book.author, book.published_year, book.is_loaned))

connection.close()
