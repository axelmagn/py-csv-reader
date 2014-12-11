import Tkinter as tk
# from tkinter.font import Font


class DataPane(tk.Frame):
    def __init__(self, master=None, data=[]):
        tk.Frame.__init__(self, master)
        self.data = data
        self.data_view = tk.Label(self, text="",font=("courier"))
        self.data_view.pack(fill="both")
        self.refresh()

    def refresh(self):
        self.refresh_data()

    def refresh_data(self):
        data_text = "\n".join(["\t".join([str(val) for val in row]) for row in
                               self.data])
        self.data_view["text"] = data_text
