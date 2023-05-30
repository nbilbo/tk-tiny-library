import ttkbootstrap as ttk
from PIL import Image

from app import constants

from ..default_page import DefaultPage


class HomePage(DefaultPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.banner_image = ttk.ImageTk.PhotoImage(
            Image.open(constants.IMAGES_DIR / 'banner.jpg')
        )

        banner_label = ttk.Label(self.body_container)
        banner_label.config(image=self.banner_image)
        banner_label.config(relief=ttk.SUNKEN, borderwidth=10)
        banner_label.pack(side=ttk.TOP, expand=True)
