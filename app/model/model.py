from pathlib import Path
from re import IGNORECASE
from typing import Dict, List, Optional

from tinydb import Query, TinyDB
from tinydb.table import Document

from .exceptions import RequiredFieldException


class Model:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.books_table_name = 'books'

    @staticmethod
    def __check_book_values(values: Dict[str, str]) -> None:
        book_id = values.get('book_id', '')
        book_title = values.get('book_title', '')

        if not len(book_id):
            raise RequiredFieldException('book_id')
        elif not len(book_title):
            raise RequiredFieldException('book_title')

    def insert_book(self, values: Dict[str, str]) -> None:
        self.__check_book_values(values)
        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            books_table.insert(values)

    def get_books(self) -> List[Document]:
        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            return books_table.all()

    def get_book_by_id(self, book_id: str) -> Optional[Document]:
        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            query = Query()

            return books_table.get(query.book_id == book_id)

    def update_book(self, values: Dict[str, str], book_id: str) -> None:
        self.__check_book_values(values)
        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            query = Query()
            books_table.update(values, query.book_id == book_id)

    def delete_book(self, book_id: str) -> None:
        if not len(book_id):
            raise RequiredFieldException('book_id')

        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            query = Query()
            books_table.remove(query.book_id == book_id)

    def search_books(self, filter_values: str) -> Optional[List[Document]]:
        with TinyDB(self.db_path) as db:
            books_table = db.table(self.books_table_name)
            query = Query()
            return books_table.search(
                query.book_title.matches(f'{filter_values}+', flags=IGNORECASE)
                | query.book_id.matches(f'{filter_values}+', flags=IGNORECASE)
                | query.author_name.matches(
                    f'{filter_values}+', flags=IGNORECASE
                )
            )
