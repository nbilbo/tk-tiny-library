from typing import Optional

import ttkbootstrap as ttk
from PIL import Image

from app import constants


class Filter(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.search_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'search.png').resize((25, 25))
        )

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=ttk.YES)

        ttk.Frame(self).pack(side=ttk.LEFT, padx=5)

        self.search_button = ttk.Button(self)
        self.search_button.config(text='Search')
        self.search_button.config(cursor='hand2')
        self.search_button.config(image=self.search_icon, compound=ttk.RIGHT)
        # noinspection PyArgumentList
        self.search_button.config(bootstyle='primary-outline')
        self.search_button.pack(side=ttk.LEFT)

    def get_values(self) -> Optional[str]:
        values = self.search_entry.get().strip()
        return values if len(values) else None
