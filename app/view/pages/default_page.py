import ttkbootstrap as ttk


class DefaultPage(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config(padding=5)

        self.header_container = ttk.Frame(self)
        self.header_container.pack(side=ttk.TOP, fill=ttk.X)

        self.body_container = ttk.Frame(self)
        self.body_container.pack(side=ttk.TOP, fill=ttk.BOTH, expand=ttk.YES)

        self.footer_container = ttk.Frame(self)
        self.footer_container.pack(side=ttk.TOP, fill=ttk.X)
