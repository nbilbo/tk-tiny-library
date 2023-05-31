import ttkbootstrap as ttk

from app import constants, utils

from .default_book_form import DefaultBookForm


class DeleteBookForm(DefaultBookForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title_label.config(text='Delete Book Formulary')

        self.delete_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'delete.png', (25, 25)
        )

        self.delete_button = ttk.Button(self.footer)
        self.delete_button.config(text='Confirm Delete')
        self.delete_button.config(image=self.delete_icon, compound=ttk.RIGHT)
        # noinspection PyArgumentList
        self.delete_button.config(bootstyle='danger-outline')
        self.delete_button.pack(side=ttk.TOP, fill=ttk.X)
