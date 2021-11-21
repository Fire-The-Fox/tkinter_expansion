import tkinter as tk


class Dropdown(tk.Button):
    def __init__(self, **kwargs):

        self.kw = {"master": None, "text": kwargs["data"][0], "data": [], "font": ("Ubuntu", 12), "relief": "sunken",
                   "variable": None, "bd": 0,
                   "command": self.unpack, "maximum": 0, "pack_cmd": None}
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
            if not self.kw["maximum"] == 0:
                maximum += 1
                if maximum == self.kw["maximum"]:
                    y = self.winfo_y() + self.winfo_height()
                    maximum = 0
                    x += data.winfo_width()

    def pack_data(self):
        self["command"] = self.unpack
        self["text"] = self.kw["text"] + " ▼"
        for i in self.labels:
            i.place_forget()
        if not self.kw["pack_cmd"] is None:
            self.kw["pack_cmd"]()

    def set_value(self, value: str):
        if isinstance(self.kw["variable"], tk.StringVar):
            self.kw["variable"].set(value)
            self.pack_data()
            self.kw["text"] = self.kw["variable"].get()
            self["text"] = self.kw["variable"].get() + " ▼"

    def redraw_top(self):
        self.kw["text"] = self.kw["data"][0]
        self["text"] = self.kw["text"] + " ▼"
        self.kw["variable"].set(self.kw["data"][0])

    def configure_values(self, **kwargs):
        self.kw.update(kwargs)
        for i in self.kw:
            if i in ["variable", "data", "master", "maximum", "pack_cmd", "name"]:
                continue
            self.kwd[i] = self.kw[i]
        self.redraw_top()
