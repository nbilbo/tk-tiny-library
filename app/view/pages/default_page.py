import ttkbootstrap as ttk

from app import constants, utils


class DefaultPage(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config(padding=5)

        # images.
        self.calendar_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'calendar.png', (25, 25)
        )

        self.database_icon = utils.load_image_tk(
            constants.ICONS_DIR / 'database.png', (25, 25)
        )

        # header.
        self.header_container = ttk.Frame(self)
        self.header_container.pack(side=ttk.TOP, fill=ttk.X)

        # body.
        self.body_container = ttk.Frame(self)
        self.body_container.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        # footer.
        self.footer_container = ttk.Frame(self)
        self.footer_container.pack(side=ttk.TOP, fill=ttk.X)

        self.datetime_label = ttk.Label(self.footer_container)
        self.datetime_label.config(image=self.calendar_icon, compound=ttk.LEFT)
        self.datetime_label.config(text=utils.get_system_datetime())
        self.datetime_label.pack(side=ttk.RIGHT)
        self.__update_datetime_label()

        ttk.Frame(self.footer_container).pack(side=ttk.RIGHT, padx=10)

        self.database_label = ttk.Label(self.footer_container)
        self.database_label.config(image=self.database_icon, compound=ttk.LEFT)
        self.database_label.pack(side=ttk.RIGHT)

    def __update_datetime_label(self) -> None:
        self.datetime_label.config(text=utils.get_system_datetime())
        self.master.after(1000, lambda: self.__update_datetime_label())
