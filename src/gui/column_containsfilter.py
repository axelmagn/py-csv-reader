import Tkinter as tk


class ColumnContainsFilter(tk.Frame):
    """
    A Tk File Selector frame consisting of an two input boxes and a filter button.

    """
    def __init__(self, master=None, btext_text="ColumnContainsFilter", command=None):
        tk.Frame.__init__(self, master)
        self.file_input = tk.Entry(self)
	self.file_input2 = tk.Entry(self)
        self.print_button = tk.Button(self, text=btext_text,
                                     command=self.display)
        self.print_button.pack(side="left")
        self.file_input.pack(fill="x")
        self.file_input2.pack(fill="x")
        
        if command is not None:
            self.command = command

    def display(self):
        self.command(self.file_input.get(),self.file_input2.get())
