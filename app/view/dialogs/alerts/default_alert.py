import ttkbootstrap as ttk


class DefaultAlert(ttk.Toplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # body.
        body_container = ttk.Frame(self)
        body_container.config(padding=10)
        body_container.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.image_label = ttk.Label(body_container)
        self.image_label.pack(side=ttk.LEFT)

        self.message_label = ttk.Label(body_container)
        self.message_label.config(anchor=ttk.CENTER)
        self.message_label.pack(side=ttk.LEFT, fill=ttk.X, expand=ttk.YES)

        # footer.
        footer_container = ttk.Frame(self)
        footer_container.config(padding=10)
        footer_container.pack(side=ttk.BOTTOM, fill=ttk.X)

        self.ok_button = ttk.Button(footer_container)
        self.ok_button.config(text='Ok')
        # noinspection PyArgumentList
        self.ok_button.config(bootstyle='success-outline')
        self.ok_button.config(command=lambda: self.destroy())
        self.ok_button.pack(side=ttk.BOTTOM, anchor=ttk.SE)
        self.ok_button.focus()
