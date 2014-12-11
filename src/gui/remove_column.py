import Tkinter as tk


class RemoveColumn(tk.Frame):
    """
    A Tk frame consisting of an input box and a RemoveColumn# button.

    """
    def __init__(self, master=None, btext_text="RemoveColumn#", command=None):
        tk.Frame.__init__(self, master)
        self.file_input = tk.Entry(self)
        self.print_button = tk.Button(self, text=btext_text,
                                     command=self.display)
        self.print_button.pack(side="left")
        self.file_input.pack(fill="x")
        if command is not None:
            self.command = command

    def display(self):
        self.command(self.file_input.get())
