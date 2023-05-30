from __future__ import annotations

from typing import TYPE_CHECKING

from app.model.exceptions import RequiredFieldException

if TYPE_CHECKING:
    from app.model import Model
    from app.view import Application
    from app.view.forms.book import (
        DeleteBookForm,
        RegisterBookForm,
        UpdateBookForm,
    )


class Controller:
    def __init__(self, application: Application, model: Model) -> None:
        self.model = model
        self.application = application
        self.__bind_books_page()
        self.refresh_application()

    def __bind_books_page(self) -> None:
        open_register_form = self.application.open_register_book_form_button
        open_register_form.config(command=self.open_register_book_form_click)

        open_update_form = self.application.open_update_book_form_button
        open_update_form.config(command=self.open_update_book_form_click)

        open_delete_form = self.application.open_delete_book_form_button
        open_delete_form.config(command=self.open_delete_book_form_click)

        search_button = self.application.search_book_button
        search_button.config(command=self.search_book_click)

        search_entry = self.application.search_book_entry
        search_entry.bind('<Return>', lambda _event: self.search_book_click())

        books_treeview = self.application.books_treeview
        books_treeview.bind(
            '<<TreeviewSelect>>', lambda _event: self.books_treeview_click()
        )

    def __bind_register_book_form(self, form: RegisterBookForm) -> None:
        save_button = form.save_button
        save_button.config(command=lambda: self.save_book_click(form))

    def __bind_update_book_form(self, form: UpdateBookForm) -> None:
        update_button = form.update_button
        update_button.config(command=lambda: self.update_book_click(form))

    def __bind_delete_book_form(self, form: DeleteBookForm) -> None:
        delete_button = form.delete_button
        delete_button.config(command=lambda: self.delete_book_click(form))

    def __refresh_books_table(self) -> None:
        filter_values = self.application.get_filter_book_values()
        self.application.clear_book_details()
        self.application.disable_book_details()

        if filter_values is None:
            books = self.model.get_books()
        else:
            books = self.model.search_books(filter_values)

        self.application.set_books_table_values(books)

    def refresh_application(self) -> None:
        self.__refresh_books_table()
        self.application.clear_book_details()
        self.application.disable_book_details()

    def open_register_book_form_click(self) -> None:
        form = self.application.get_register_book_form()
        self.__bind_register_book_form(form)
        form.grab_set()

    def open_update_book_form_click(self) -> None:
        selection = self.application.get_books_table_selection()
        if selection is not None:
            book_id = str(selection[0])
            book = self.model.get_book_by_id(book_id)

            if book is not None:
                form = self.application.get_update_book_form()
                form.old_book_id = book.get('book_id')
                form.set_book_id_value(book.get('book_id'))
                form.set_book_title_value(book.get('book_title'))
                form.set_book_edition_value(book.get('book_edition'))
                form.set_author_name_value(book.get('author_name'))
                self.__bind_update_book_form(form)
                form.grab_set()

    def open_delete_book_form_click(self) -> None:
        selection = self.application.get_books_table_selection()
        if selection is not None:
            book_id = str(selection[0])
            book = self.model.get_book_by_id(book_id)
            if book is not None:
                form = self.application.get_delete_book_form()
                form.set_book_id_value(book.get('book_id'))
                form.set_book_title_value(book.get('book_title'))
                form.set_book_edition_value(book.get('book_edition'))
                form.set_author_name_value(book.get('author_name'))
                self.__bind_delete_book_form(form)
                form.grab_set()

    def save_book_click(self, form: RegisterBookForm) -> None:
        values = form.get_values()
        form.clear_feedbacks()

        try:
            self.model.insert_book(values)

        except RequiredFieldException as error:
            form.set_feedback_value(error.field, 'Required')

        except Exception as error:
            print(error)
            self.application.display_danger_alert('Danger', str(error))

        else:
            self.application.display_success_alert(
                'Success', 'Book successfully Created.'
            )
            self.refresh_application()
            form.destroy()

    def update_book_click(self, form: UpdateBookForm) -> None:
        values = form.get_values()
        form.clear_feedbacks()

        try:
            self.model.update_book(values, form.old_book_id)

        except RequiredFieldException as error:
            form.set_feedback_value(error.field, 'Required')

        except Exception as error:
            print(error)
            self.application.display_danger_alert('Danger', str(error))

        else:
            self.application.display_success_alert(
                'Success', 'Book successfully Updated.'
            )
            self.refresh_application()
            form.destroy()

    def delete_book_click(self, form: DeleteBookForm) -> None:
        values = form.get_values()
        book_id = values.get('book_id')

        try:
            self.model.delete_book(book_id)

        except RequiredFieldException as error:
            form.set_feedback_value(error.field, 'Required')

        except Exception as error:
            print(error)
            self.application.display_danger_alert('Danger', str(error))

        else:
            self.application.display_success_alert(
                'Success', 'Book successfully Deleted.'
            )
            self.refresh_application()
            form.destroy()

    def search_book_click(self) -> None:
        self.__refresh_books_table()

    def books_treeview_click(self) -> None:
        selection = self.application.get_books_table_selection()
        if selection is not None:
            self.application.enable_book_details()
            book_id = str(selection[0])
            book = self.model.get_book_by_id(book_id)
            if book is not None:
                self.application.clear_book_details()
                self.application.set_book_details(book)
