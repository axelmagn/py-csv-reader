import Tkinter as tk


class StatusPane(tk.Frame):
    """
    A StatusPane displays a collection of information.
    """
    def __init__(self, master=None, data={}):
        tk.Frame.__init__(self, master)
        self._data = data
        self._view = tk.Label(self, justify="left")
        self._view.pack(fill="x")
        self.update()

    def update(self):
        self._view["text"] = "\n".join(["%s:\t%s" % (k, self._data[k]) for k in
                                       self._data])

    def __setitem__(self, key, value):
        self._data[key] = value
        self.update()

    def __getitem__(self, key):
        self._data[key]

    def __delitem__(self, key):
        del self._data[key]
