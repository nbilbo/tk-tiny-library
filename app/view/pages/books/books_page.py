import ttkbootstrap as ttk

from ..default_page import DefaultPage
from .details import Details
from .filter import Filter
from .table import Table


class BooksPage(DefaultPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        paned_window = ttk.PanedWindow(
            self.body_container, orient=ttk.HORIZONTAL
        )
        paned_window.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        # left content.
        left_container = ttk.Frame(paned_window)
        left_container.config(padding=5)
        paned_window.add(left_container, weight=3)

        self.filter = Filter(left_container)
        self.filter.pack(side=ttk.TOP, fill=ttk.X)

        self.table = Table(left_container)
        self.table.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES, pady=5)

        buttons_container = ttk.Frame(left_container)
        buttons_container.pack(side=ttk.TOP, fill=ttk.X)

        self.open_register_form_button = ttk.Button(buttons_container)
        self.open_register_form_button.config(text='Open Register Formulary')
        self.open_register_form_button.config(cursor='hand2')
        # noinspection PyArgumentList
        self.open_register_form_button.config(bootstyle='info-outline')
        self.open_register_form_button.pack(
            side=ttk.LEFT, fill=ttk.X, expand=ttk.YES
        )

        # right content.
        right_container = ttk.Frame(paned_window)
        right_container.config(padding=5)
        paned_window.add(right_container, weight=1)

        self.details = Details(right_container)
        self.details.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)
