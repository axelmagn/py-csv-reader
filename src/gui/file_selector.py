import tkinter as tk


class FileSelector(tk.Frame):
    """
    A Tk File Selector frame consisting of an input box and an open button.

    If a command handler is specified via the constructor or self.command, it
    will be called with the currently specified path as its first argument.

    """
    def __init__(self, master=None, open_text="Open", command=None):
        tk.Frame.__init__(self, master)
        self.file_input = tk.Entry(self)
        self.open_button = tk.Button(self, text=open_text,
                                     command=self.open_path)
        self.open_button.pack(side="right")
        self.file_input.pack(fill="x")
        if command is not None:
            self.command = command

    def open_path(self):
        self.command(self.file_input.get())
