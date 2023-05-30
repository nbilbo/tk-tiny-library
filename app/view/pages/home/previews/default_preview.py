from typing import Optional

import ttkbootstrap as ttk


class DefaultPreview(ttk.Button):
    text: Optional[str] = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config(cursor='hand2')

        if self.text is not None:
            self.config(text=self.text)
