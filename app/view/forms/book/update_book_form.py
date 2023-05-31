import ttkbootstrap as ttk

from app import constants, utils

from .default_book_form import DefaultBookForm


class UpdateBookForm(DefaultBookForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.old_book_id = ''
        self.title_label.config(text='Update Book Formulary')

        self.update_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'update.png', (25, 25)
        )

        self.update_button = ttk.Button(self.footer)
        self.update_button.config(text='Update')
        self.update_button.config(image=self.update_icon, compound=ttk.RIGHT)
        # noinspection PyArgumentList
        self.update_button.config(bootstyle='warning-outline')
        self.update_button.pack(side=ttk.TOP, fill=ttk.X)
