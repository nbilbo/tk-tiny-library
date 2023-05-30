import tkinter as tk
from typing import List, Optional, Tuple

import ttkbootstrap as ttk
from tinydb.table import Document

from .dialogs.alerts import DangerAlert, SuccessAlert
from .forms.book import DeleteBookForm, RegisterBookForm, UpdateBookForm
from .pages import BooksPage, HomePage
from .sidebar import SideBar
from .toolbar import Toolbar


class Application(ttk.Window):
    def __init__(self) -> None:
        super().__init__()

        # widgets.
        self.toolbar = Toolbar()
        self.toolbar.pack(side=ttk.TOP, fill=ttk.X)

        paned_window = ttk.PanedWindow(self, orient=ttk.HORIZONTAL)
        paned_window.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.sidebar = SideBar(paned_window)
        paned_window.add(self.sidebar, weight=1)

        self.pages_container = ttk.Frame(paned_window)
        paned_window.add(self.pages_container, weight=1)

        self.home_page = HomePage(self.pages_container)
        self.books_page = BooksPage(self.pages_container)

        # binding.
        self.__bind()

        # styles.
        self.dark_theme = 'superhero'
        self.light_theme = 'cosmo'
        self.theme = self.dark_theme

        self.min_font_size = 12
        self.max_font_size = 16
        self.font_size = self.min_font_size

        # initial state.
        self.apply_style()
        self.show_home_page()
        self.geometry('1000x650+0+0')

    def __bind(self) -> None:
        self.zoom_in_button.config(command=self.zoom_in)
        self.zoom_out_button.config(command=self.zoom_out)
        self.toggle_theme_button.config(command=self.toggle_theme)

        self.home_sidebar_button.config(command=self.show_home_page)
        self.books_sidebar_button.config(command=self.show_books_page)

    def __clear_pages_container(self) -> None:
        for children in self.pages_container.winfo_children():
            children.pack_forget()

    def __disable_children(self, widget: tk.Misc) -> None:
        if 'state' in widget.keys():
            # noinspection PyArgumentList
            widget.configure(state='disable')
        for children in widget.winfo_children():
            self.__disable_children(children)

    def __enable_children(self, widget: tk.Misc) -> None:
        if 'state' in widget.keys():
            # noinspection PyArgumentList
            widget.configure(state='normal')
        for children in widget.winfo_children():
            self.__enable_children(children)

    def disable_book_details(self) -> None:
        self.__disable_children(self.books_page.details)

    def enable_book_details(self) -> None:
        self.__enable_children(self.books_page.details)

    def apply_style(self) -> None:
        def inner_apply_style(widget: tk.Misc) -> None:
            if isinstance(widget, ttk.Entry):
                widget.config(font=(None, self.font_size, ttk.NORMAL))
            else:
                for children in widget.winfo_children():
                    inner_apply_style(children)

        style = ttk.Style(theme=self.theme)
        style.configure('.', font=(None, self.font_size, ttk.NORMAL))
        style.configure('Treeview', rowheight=40)
        inner_apply_style(self)

    def show_home_page(self) -> None:
        self.__clear_pages_container()
        self.home_page.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

    def show_books_page(self) -> None:
        self.__clear_pages_container()
        self.books_page.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

    def display_success_alert(self, title: str, message: str) -> None:
        alert = SuccessAlert(master=self, title=title)
        alert.message_label.config(text=message)
        alert.grab_set()

    def display_danger_alert(self, title: str, message: str) -> None:
        alert = DangerAlert(master=self, title=title)
        alert.message_label.config(text=message)
        alert.grab_set()

    def toggle_theme(self) -> None:
        self.theme = (
            self.light_theme
            if self.theme == self.dark_theme
            else self.dark_theme
        )
        self.apply_style()

    def zoom_in(self) -> None:
        if (self.font_size + 2) <= self.max_font_size:
            self.font_size += 2
            self.apply_style()

    def zoom_out(self) -> None:
        if (self.font_size - 2) >= self.min_font_size:
            self.font_size -= 2
            self.apply_style()

    def clear_book_details(self) -> None:
        self.books_page.details.clear()

    def get_register_book_form(self) -> RegisterBookForm:
        form = RegisterBookForm(master=self, title='Register Book Formulary')
        form.book_id_field.field_entry.focus()
        self.apply_style()
        return form

    def get_update_book_form(self) -> UpdateBookForm:
        form = UpdateBookForm(master=self, title='Update Book Formulary')
        form.book_id_field.field_entry.focus()
        self.apply_style()
        return form

    def get_delete_book_form(self) -> DeleteBookForm:
        form = DeleteBookForm(master=self, title='Delete Book Formulary')
        form.delete_button.focus()
        self.apply_style()
        return form

    def get_filter_book_values(self) -> Optional[str]:
        return self.books_page.filter.get_values()

    def get_books_table_selection(self) -> Optional[Tuple[str, str, str]]:
        selections = self.books_treeview.selection()
        if selections:
            selection = selections[0]
            values = self.books_treeview.item(selection)['values']
            book_id = values[0]
            book_title = values[1]
            author_name = values[2]

            return book_id, book_title, author_name

        return None

    def set_books_table_values(self, values: List[Document]) -> None:
        self.books_page.table.set_values(values)

    def set_book_details(self, book: Document):
        details = self.books_page.details
        details.insert_book_id(book.get('book_id'))
        details.insert_book_title(book.get('book_title'))
        details.insert_book_edition(book.get('book_edition'))
        details.insert_author_name(book.get('author_name'))

    @property
    def zoom_in_button(self) -> ttk.Button:
        return self.toolbar.zoom_in_button

    @property
    def zoom_out_button(self) -> ttk.Button:
        return self.toolbar.zoom_out_button

    @property
    def toggle_theme_button(self) -> ttk.Button:
        return self.toolbar.toggle_theme_button

    @property
    def home_sidebar_button(self) -> ttk.Button:
        return self.sidebar.home_button

    @property
    def books_sidebar_button(self) -> ttk.Button:
        return self.sidebar.books_button

    @property
    def open_register_book_form_button(self) -> ttk.Button:
        return self.books_page.open_register_form_button

    @property
    def open_update_book_form_button(self) -> ttk.Button:
        return self.books_page.details.open_update_form_button

    @property
    def open_delete_book_form_button(self) -> ttk.Button:
        return self.books_page.details.open_delete_form_button

    @property
    def search_book_button(self) -> ttk.Button:
        return self.books_page.filter.search_button

    @property
    def search_book_entry(self) -> ttk.Entry:
        return self.books_page.filter.search_entry

    @property
    def books_treeview(self) -> ttk.Treeview:
        return self.books_page.table.treeview
