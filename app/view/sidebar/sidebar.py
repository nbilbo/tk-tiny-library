import ttkbootstrap as ttk

from app import constants, utils


class SideBar(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config(padding=5)

        self.navigation_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'navigation.png', (25, 25)
        )

        self.home_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'index.png', (50, 50)
        )

        self.book_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'book.png', (50, 50)
        )

        self.title_label = ttk.Label(self)
        self.title_label.config(text='Navigation')
        self.title_label.config(anchor=ttk.CENTER)
        self.title_label.config(image=self.navigation_icon, compound=ttk.RIGHT)
        self.title_label.pack(side=ttk.TOP, fill=ttk.X, pady=10)

        self.home_button = ttk.Button(self)
        self.home_button.config(text='Home')
        self.home_button.config(cursor='hand2')
        self.home_button.config(image=self.home_icon)
        self.home_button.config(compound=ttk.TOP)
        # noinspection PyArgumentList
        self.home_button.config(bootstyle='primary-outline')
        self.home_button.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.books_button = ttk.Button(self)
        self.books_button.config(text='Books')
        self.books_button.config(cursor='hand2')
        self.books_button.config(image=self.book_icon, compound=ttk.TOP)
        # noinspection PyArgumentList
        self.books_button.config(bootstyle='primary-outline')
        self.books_button.pack(
            side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES, pady=5
        )
