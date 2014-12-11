import Tkinter as tk


class PrintHTML(tk.Frame):
    """
    A Tk File Selector frame consisting of an button.

    If a command handler is specified via the constructor or self.command, it
    will be called
    """
    def __init__(self, master=None, btext_text="PrintHTML", command=None):
        tk.Frame.__init__(self, master)
        self.print_button = tk.Button(self, text=btext_text, command=command)
        self.print_button.pack(side="right")

