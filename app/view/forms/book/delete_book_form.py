import ttkbootstrap as ttk
from PIL import Image

from app import constants

from .default_book_form import DefaultBookForm


class DeleteBookForm(DefaultBookForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title_label.config(text='Delete Book Formulary')

        self.delete_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'delete.png').resize((25, 25))
        )

        self.delete_button = ttk.Button(self.footer)
        self.delete_button.config(text='Confirm Delete')
        self.delete_button.config(image=self.delete_icon, compound=ttk.RIGHT)
        # noinspection PyArgumentList
        self.delete_button.config(bootstyle='danger-outline')
        self.delete_button.pack(side=ttk.TOP, fill=ttk.X)
