from typing import Dict

import ttkbootstrap as ttk

from app.view.fields import TextField


class DefaultBookForm(ttk.Toplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry('500x500+0+0')

        # header.
        self.header = ttk.Frame(self)
        self.header.config(padding=5)
        self.header.pack(side=ttk.TOP, fill=ttk.X)

        self.title_label = ttk.Label(self.header)
        self.title_label.config(text='Book Formulary')
        self.title_label.config(anchor=ttk.CENTER)
        self.title_label.pack(side=ttk.TOP, fill=ttk.X)

        # body.
        self.body = ttk.Frame(self)
        self.body.config(padding=5)
        self.body.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.book_id_field = TextField(self.body, 'ID *')
        self.book_id_field.pack(side=ttk.TOP, fill=ttk.X)

        self.book_title_field = TextField(self.body, 'Title *')
        self.book_title_field.pack(side=ttk.TOP, fill=ttk.X)

        self.author_name_field = TextField(self.body, 'Author')
        self.author_name_field.pack(side=ttk.TOP, fill=ttk.X)

        self.book_edition_field = TextField(self.body, 'Edition')
        self.book_edition_field.pack(side=ttk.TOP, fill=ttk.X)

        # footer.
        self.footer = ttk.Frame(self)
        self.footer.config(padding=5)
        self.footer.pack(side=ttk.BOTTOM, fill=ttk.X)

    def get_values(self) -> Dict[str, str]:
        return {
            'book_id': self.get_book_id_value(),
            'book_title': self.get_book_title_value(),
            'book_edition': self.get_book_edition_value(),
            'author_name': self.get_author_name_value(),
        }

    def set_values(self, values: Dict[str, str]) -> None:
        self.set_book_id_value(values.get('book_id', ''))
        self.set_book_title_value(values.get('book_title', ''))
        self.set_book_edition_value(values.get('book_edition', ''))
        self.set_author_name_value(values.get('author_name', ''))

    def clear_feedbacks(self) -> None:
        self.book_id_field.set_feedback_value('')
        self.book_title_field.set_feedback_value('')
        self.book_edition_field.set_feedback_value('')
        self.author_name_field.set_feedback_value('')

    def get_book_id_value(self) -> str:
        return self.book_id_field.get_entry_value()

    def get_book_title_value(self) -> str:
        return self.book_title_field.get_entry_value()

    def get_author_name_value(self) -> str:
        return self.author_name_field.get_entry_value()

    def get_book_edition_value(self) -> str:
        return self.book_edition_field.get_entry_value()

    def set_book_id_value(self, value: str) -> None:
        self.book_id_field.set_entry_value(value)

    def set_book_title_value(self, value: str) -> None:
        self.book_title_field.set_entry_value(value)

    def set_author_name_value(self, value: str) -> None:
        self.author_name_field.set_entry_value(value)

    def set_book_edition_value(self, value: str) -> None:
        self.book_edition_field.set_entry_value(value)

    def set_feedback_value(self, field: str, message: str) -> None:
        fields: Dict[str, TextField] = {
            'book_id': self.book_id_field,
            'book_title': self.book_title_field,
            'book_edition': self.book_edition_field,
            'author_name': self.author_name_field,
        }

        if field in fields.keys():
            fields[field].set_feedback_value(message)
            fields[field].field_entry.focus()
