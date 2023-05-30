from typing import List

import ttkbootstrap as ttk
from tinydb.table import Document


class Table(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        columns = ('ID', 'Title', 'Author')
        self.treeview = ttk.Treeview(self)
        self.treeview.config(columns=columns)
        self.treeview.column('#0', width=0, minwidth=0, stretch=False)
        for column in columns:
            self.treeview.heading(column, text=column)
            self.treeview.column(
                column, minwidth=50, width=50, stretch=True, anchor=ttk.CENTER
            )
        self.treeview.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

    def set_values(self, values: List[Document]) -> None:
        self.treeview.delete(*self.treeview.get_children())

        for value in values:
            book_id = value.get('book_id')
            book_title = value.get('book_title')
            author_name = value.get('author_name')
            self.treeview.insert(
                '', 'end', values=(book_id, book_title, author_name)
            )
