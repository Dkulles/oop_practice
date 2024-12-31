# import sqlite3 as db
from enum import member


class Library:
    def __init__(self, book: str, member: str) -> None:
        self.book = book
        self.member = member

    def user_authentification(self, ):
        pass

    def add_member(self):
        pass

    def add_book(self):
        pass

    def display_books():
        pass

    def display_members(self):
        pass

    def search_book(self):
        pass

    def update_in_db():
        pass

class Book(Library):
    def __init__(self) -> None:
        super().__init__()

    def borrow_book(self):
        pass

    def return_book(self):
        pass

class Member(Library):
    def __init__(self, member_id: int, borrowed_books: str) -> None:
        super().__init__()

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def __str__(self) -> str:
        pass


def books_table():    #should create table in db with books
    pass

def members_table():         #should create members table in db
    pass

def main():
    books_table()
    members_table()

    pass


if __name__ == "__main__":
    main()
