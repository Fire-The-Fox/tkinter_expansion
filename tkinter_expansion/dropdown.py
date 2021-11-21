import tkinter as tk


class Dropdown(tk.Button):
    """

    Tkinker's OptionMenu class is sometimes really weird and can't be customized

    With this class you can easily manipulate look of every element of Dropdown menu.
    """
    def __init__(self, **kwargs):

        self.kw = {"master": None, "text": kwargs["data"][0], "data": [],
                   "font": ("Ubuntu", 12), "relief": "sunken",
                   "variable": None, "bd": 0,
                   "command": self.unpack, "maximum": 0, "pack_cmd": lambda: None}
        self.kw.update(kwargs)
        self.kwd = {}
        for i in self.kw:
            if i in ["variable", "data", "master", "maximum", "pack_cmd", "name"]:
                continue
            self.kwd[i] = self.kw[i]

        self.labels = []

        super().__init__(self.kw["master"], **self.kwd)
        self["text"] = self.kwd["text"] + " ▼"
        self.kw["variable"].set(self.kw["data"][0])

    def unpack(self):
        """
        Function unpack generates elements and it also gives functionality of Dropdown
        """
        self["text"] = self.kw["text"] + " ▲"
        self["command"] = self.pack_data
        y = self.winfo_y() + self.winfo_height()
        index = 0
        data = self
        x = data.winfo_x()
        maximum = 0
        for i in self.kw["data"]:
            self.labels.append(tk.Button(self.kw["master"], **self.kwd))
            self.labels[index]["command"] = lambda j=i: self.set_value(j)
            self.labels[index]["text"] = i
            self.labels[index].place(x=x, y=y, width=self.winfo_width())
            y += self.winfo_height()
            index += 1
            if self.kw["maximum"] != 0:
                maximum += 1
                if maximum == self.kw["maximum"]:
                    y = self.winfo_y() + self.winfo_height()
                    maximum = 0
                    x += data.winfo_width()

    def pack_data(self):
        """Hides every other elements of Dropdown."""
        self["command"] = self.unpack
        self["text"] = self.kw["text"] + " ▼"
        for i in self.labels:
            i.place_forget()
        if callable(self.kw["pack_cmd"]):
            self.kw["pack_cmd"]()

    def set_value(self, value: str):
        """

        Function set_value sets value of specific StringVar variable

        :param value: Which value to set for variable
        """
        if isinstance(self.kw["variable"], tk.StringVar):
            self.kw["variable"].set(value)
            self.pack_data()
            self.kw["text"] = self.kw["variable"].get()
            self["text"] = self.kw["variable"].get() + " ▼"

    def redraw_top(self):
        """ This function will redraw top part of Dropdown widget. """
        self.kw["text"] = self.kw["data"][0]
        self["text"] = self.kw["text"] + " ▼"
        self.kw["variable"].set(self.kw["data"][0])

    def configure_values(self, **kwargs):
        """

        With this function it's easier to modify Dropdown widget.

        :param kwargs:  things to be configured
        """
        self.kw.update(kwargs)
        for i in self.kw:
            if i in ["variable", "data", "master", "maximum", "pack_cmd", "name"]:
                continue
            self.kwd[i] = self.kw[i]
        self.redraw_top()
