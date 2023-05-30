import ttkbootstrap as ttk
from PIL import Image

from app import constants

from .default_book_form import DefaultBookForm


class RegisterBookForm(DefaultBookForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title_label.config(text='Register Book Formulary')

        self.save_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'save.png').resize((25, 25))
        )

        self.save_button = ttk.Button(self.footer)
        self.save_button.config(text='Save')
        self.save_button.config(image=self.save_icon, compound=ttk.RIGHT)
        # noinspection PyArgumentList
        self.save_button.config(bootstyle='success-outline')
        self.save_button.pack(side=ttk.TOP, fill=ttk.X)
