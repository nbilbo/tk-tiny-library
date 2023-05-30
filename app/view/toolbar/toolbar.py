import ttkbootstrap as ttk
from PIL import Image

from app import constants


class Toolbar(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config(padding=5)

        self.zoom_in_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'zoom-in.png').resize((25, 25))
        )
        self.zoom_out_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'zoom-out.png').resize((25, 25))
        )
        self.toggle_theme_icon = ttk.ImageTk.PhotoImage(
            Image.open(constants.ICONS_DIR / 'toggle-theme.png').resize(
                (25, 25)
            )
        )

        self.toggle_theme_button = ttk.Button(self)
        # self.toggle_theme_button.config(text='Toggle Theme')
        self.toggle_theme_button.config(cursor='hand2')
        self.toggle_theme_button.config(image=self.toggle_theme_icon)
        self.toggle_theme_button.pack(side=ttk.RIGHT)

        self.zoom_in_button = ttk.Button(self)
        # self.zoom_in_button.config(text='Zoom in')
        self.zoom_in_button.config(cursor='hand2')
        self.zoom_in_button.config(image=self.zoom_in_icon)
        self.zoom_in_button.pack(side=ttk.RIGHT, padx=5)

        self.zoom_out_button = ttk.Button(self)
        # self.zoom_out_button.config(text='Zoom out')
        self.zoom_out_button.config(image=self.zoom_out_icon)
        self.zoom_out_button.config(cursor='hand2')
        self.zoom_out_button.pack(side=ttk.RIGHT)

        for button in (
            self.zoom_in_button,
            self.zoom_out_button,
            self.toggle_theme_button,
        ):
            # noinspection PyArgumentList
            button.config(bootstyle='primary-link')
