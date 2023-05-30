import tkinter as tk

import ttkbootstrap as ttk
from PIL import Image

from app import constants


class Details(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.details_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'details.png').resize((25, 25))
        )

        # header.
        header_container = ttk.Frame(self)
        header_container.pack(side=ttk.TOP, fill=ttk.X)

        title_label = ttk.Label(header_container)
        title_label.config(text='Details')
        title_label.config(anchor=ttk.CENTER)
        title_label.config(image=self.details_icon, compound=ttk.RIGHT)
        title_label.pack(side=ttk.TOP)

        # body.
        body_container = ttk.Frame(self)
        body_container.config(padding=15)
        body_container.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.book_id_frame = ttk.LabelFrame(body_container)
        self.book_id_frame.config(text='ID')
        self.book_id_frame.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.book_title_frame = ttk.LabelFrame(body_container)
        self.book_title_frame.config(text='Title')
        self.book_title_frame.pack(
            side=ttk.TOP, fill=ttk.BOTH, expand=True, pady=5
        )

        self.author_name_frame = ttk.LabelFrame(body_container)
        self.author_name_frame.config(text='Author')
        self.author_name_frame.pack(
            side=ttk.TOP, fill=ttk.BOTH, expand=True, pady=5
        )

        self.book_edition_frame = ttk.LabelFrame(body_container)
        self.book_edition_frame.config(text='Edition')
        self.book_edition_frame.pack(
            side=ttk.TOP, fill=ttk.BOTH, expand=True, pady=5
        )

        # footer.
        footer_container = ttk.Frame(self)
        footer_container.pack(side=ttk.TOP, fill=ttk.X)

        self.open_update_form_button = ttk.Button(footer_container)
        self.open_update_form_button.config(text='Open Update Formulary')
        self.open_update_form_button.config(cursor='hand2')
        # noinspection PyArgumentList
        self.open_update_form_button.config(bootstyle='warning-outline')
        self.open_update_form_button.pack(side=ttk.TOP, fill=ttk.X)

        ttk.Frame(footer_container).pack(pady=5)

        self.open_delete_form_button = ttk.Button(footer_container)
        self.open_delete_form_button.config(text='Open Delete Formulary')
        self.open_delete_form_button.config(cursor='hand2')
        # noinspection PyArgumentList
        self.open_delete_form_button.config(bootstyle='danger-outline')
        self.open_delete_form_button.pack(side=ttk.TOP, fill=ttk.X)

    @staticmethod
    def __insert(master: tk.Misc, value: str) -> None:
        label = ttk.Label(master)
        label.config(text=value)
        label.config(anchor=ttk.CENTER)
        label.pack(side=ttk.TOP, fill=ttk.X)

    @staticmethod
    def __clear(master: tk.Misc) -> None:
        for children in master.winfo_children():
            children.destroy()

    def insert_book_id(self, value: str) -> None:
        self.__insert(self.book_id_frame, value)

    def insert_book_title(self, value: str) -> None:
        self.__insert(self.book_title_frame, value)

    def insert_book_edition(self, value: str) -> None:
        self.__insert(self.book_edition_frame, value)

    def insert_author_name(self, value: str) -> None:
        self.__insert(self.author_name_frame, value)

    def clear(self) -> None:
        self.__clear(self.book_id_frame)
        self.__clear(self.book_title_frame)
        self.__clear(self.book_edition_frame)
        self.__clear(self.author_name_frame)
