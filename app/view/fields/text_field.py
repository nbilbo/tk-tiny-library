import tkinter as tk

import ttkbootstrap as ttk


class TextField(ttk.Frame):
    def __init__(self, master: tk.Misc, label: str) -> None:
        super().__init__(master)

        self.field_label = ttk.Label(self)
        self.field_label.config(text=label)
        self.field_label.config(anchor=ttk.CENTER)
        self.field_label.pack(side=ttk.TOP, fill=ttk.X)

        self.field_entry = ttk.Entry(self)
        self.field_entry.config(justify=ttk.CENTER)
        self.field_entry.pack(side=ttk.TOP, fill=ttk.X, expand=ttk.YES)

        self.field_feedback = ttk.Label(self)
        self.field_feedback.config(anchor=ttk.CENTER)
        self.field_feedback.config(foreground='red')
        self.field_feedback.pack(side=ttk.TOP, fill=ttk.X)

    def get_entry_value(self) -> str:
        return self.field_entry.get()

    def set_entry_value(self, value: str) -> None:
        self.field_entry.delete(0, ttk.END)
        self.field_entry.insert(ttk.END, value)

    def set_feedback_value(self, value: str) -> None:
        self.field_feedback.config(text=value)
