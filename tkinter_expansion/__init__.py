import tkinter as tk
import tkinter.messagebox as tkm
from os import mkdir
import json
from . import GuiStyle
from .dropdown import Dropdown

tmp_top_label = None
tmp_top = None


class DesignerThemeNotFound(Exception):
    """ This exception is raised when Designer didn't find specific theme. """

    def __init__(self):
        super().__init__()


class Designer:
    """

    With Designer class you are able to change color values and widget behaviour  while
    your app is running.

    when you are done you can set show to False

    You can also use Designer as theme manager.
    """
    def __init__(self, *args, **kwargs) -> None:
        """

        :param args: Any
        :param kwargs: available kwargs:
            master, width, height, title, show, share_locals, share_globals
        """
        self.selected = ""
        self.changed_widgets = {"": {"": ""}}
        self.changed_widgets = {}
        self.rgb_value = [0, 0, 0]
        self.var_data = ""
        self.name = "default"
        self.var_name_data = ""
        self.args = args
        self.apply_text = ""
        self.check_var = tk.StringVar()
        self.behaviour = tk.StringVar()
        self.red_color = tk.StringVar()
        self.green_color = tk.StringVar()
        self.blue_color = tk.StringVar()
        self._term_i = None
        self.__color_data = ["activebackground",
                             "activeforeground",
                             "background",
                             "disabledforeground",
                             "disabledbackground",
                             "foreground",
                             "highlightbackground",
                             "highlightcolor",
                             "selectbackground",
                             "selectforeground",
                             "selectcolor",
                             "troughcolor"]
        self.__behaviour_data = ["relief",
                                 "justify",
                                 "underline",
                                 "overrelief",
                                 "state",
                                 "cursor",
                                 "title",
                                 "orient"]

        self._all_available_kwargs = ["width", "height", "title", "show"]
        self.kwargs = {"width": 400,
                       "height": 500,
                       "title": "Tkinter expansion designer",
                       "show": True}

        self.kwargs.update(kwargs)
        self.window = tk.Toplevel(bg="#333333")
        self.window.resizable(False, False)
        self.window.title(self.kwargs["title"])
        self.window.configure(width=self.kwargs["width"], height=self.kwargs["height"])

        self.EditDropdown = Dropdown(master=self.window, data=self.__color_data,
                                     variable=self.check_var,
                                     font=("Ubuntu", 11), maximum=9, bg="#333333",
                                     fg="#ffffff",
                                     activebackground="#ffffff",
                                     activeforeground="#000000")
        self.EditDropdown.place(x=15, rely=0.32, width=175)

        self.ColorChoicePanel = tk.Label(self.window, background="#444444")
        self.ColorChoicePanel.place(x=0, y=0, relheight=0.25,
                                    width=int(self.kwargs["width"]))
        self.ColorRedText = tk.Label(self.ColorChoicePanel, text="Red",
                                     background="#444444", fg="#ffffff")
        self.ColorRedText.place(anchor="ne", x=275, y=25)
        self.ColorRedInput = tk.Entry(self.ColorChoicePanel, background="#555555", bd=0,
                                      fg="#ffffff", textvariable=self.red_color,
                                      selectbackground="#ffffff",
                                      disabledbackground="#111111",
                                      disabledforeground="#ffffff")
        self.ColorRedInput.place(x=275, y=20, height=20, width=120)
        self.ColorGreenText = tk.Label(self.ColorChoicePanel, text="Green",
                                       background="#444444", fg="#ffffff")
        self.ColorGreenText.place(anchor="ne", x=275, y=60)
        self.ColorGreenInput = tk.Entry(self.ColorChoicePanel, background="#555555",
                                        bd=0, fg="#ffffff",
                                        textvariable=self.green_color,
                                        selectbackground="#ffffff",
                                        disabledbackground="#111111",
                                        disabledforeground="#ffffff")
        self.ColorGreenInput.place(x=275, y=55, height=20, width=120)
        self.ColorBlueText = tk.Label(self.ColorChoicePanel, text="Blue",
                                      background="#444444", fg="#ffffff")
        self.ColorBlueText.place(anchor="ne", x=275, y=95)
        self.ColorBlueInput = tk.Entry(self.ColorChoicePanel, background="#555555",
                                       bd=0, fg="#ffffff",
                                       textvariable=self.blue_color,
                                       selectbackground="#ffffff",
                                       disabledbackground="#111111",
                                       disabledforeground="#ffffff")
        self.ColorBlueInput.place(x=275, y=90, height=20, width=120)
        self.Color = tk.Label(self.ColorChoicePanel, background="black",
                              highlightbackground="white",
                              highlightthickness=2)
        self.Color.place(x=12.5, y=12.5, height=100, width=100)

        self.ColorRedInput.insert(0, "0")
        self.ColorGreenInput.insert(0, "0")
        self.ColorBlueInput.insert(0, "0")

        self.red_color.trace("w", lambda *_: self.__change_color_example())
        self.green_color.trace("w", lambda *_: self.__change_color_example())
        self.blue_color.trace("w", lambda *_: self.__change_color_example())

        self.Name = tk.Label(self.window, text="Name: ", bg="#333333", fg="#ffffff")
        self.Name.place(x=15, rely=0.26)

        self.EditDropdownText = tk.Label(self.window, text="Change color data of "
                                                           "selected widget",
                                         bg="#333333", fg="#ffffff")
        self.EditDropdownText.place(x=15, rely=0.285)

        self.BehaviourDropdown = Dropdown(master=self.window,
                                          data=self.__behaviour_data,
                                          variable=self.behaviour,
                                          font=("Ubuntu", 11), maximum=7, bg="#333333",
                                          fg="#ffffff",
                                          activebackground="#ffffff",
                                          activeforeground="#000000")
        self.BehaviourDropdown.place(x=15, rely=0.42, width=100)

        self.EditDropdownText = tk.Label(self.window, text="Change behaviour data of"
                                                           " selected widget",
                                         bg="#333333", fg="#ffffff")
        self.EditDropdownText.place(x=15, rely=0.385)

        self.ApplyButton = tk.Button(self.window, text="Apply", bg="#333333",
                                     fg="#ffffff", bd=0,
                                     activebackground="#ffffff",
                                     activeforeground="#000000", relief="sunken")
        self.ApplyButton.place(x=265, y=455)

        self.SaveButton = tk.Button(self.window, text="Save", bg="#333333",
                                    fg="#ffffff", bd=0,
                                    activebackground="#ffffff",
                                    activeforeground="#000000", relief="sunken")
        self.SaveButton.place(x=325, y=455)

        self.ManualValue = tk.Entry(self.window, background="#555555", bd=0,
                                    fg="#ffffff",
                                    selectbackground="#ffffff", font=("Ubuntu", 12))
        self.ManualValue.place(x=15, y=455)

        self.ManualValue.bind("<KeyRelease>", lambda _: self.__manual_color_change())

        if self.kwargs["show"]:
            pass
        else:
            self.window.destroy()

        self.show = self.kwargs["show"]

    def __change_color_example(self):
        """

        This private function is used to change example color background.
        :return: rgb values
        """
        self.Color["bg"] = \
            self.__get_rgb(self.ColorRedInput, self.ColorGreenInput,
                           self.ColorBlueInput)

    def __manual_color_change(self):
        """This private function is setting example color from ManualValue entry."""
        try:
            self.Color.configure(background=self.ManualValue.get())
        except tk.TclError:
            pass

    def __get_rgb(self, *args: tk.Entry):
        """

        This private function is getting values from entries and converting them to hex.

        :param args: Entry from which to get RGB value
        :return: hex color returned from rgb values
        """
        final_values = []
        for i in args:
            self._term_i = i.get()
            try:
                final_values.append(int(self._term_i))
            except ValueError:
                final_values.append(0)
        return rgb_to_hex(final_values[0], final_values[1], final_values[2])

    def __select_widget(self, part: tk.Event):
        """

        This private function is used to configure Designer to work with widget that
        is going to be selected.

        :param part: widget which is going to be selected
        """
        if self.__un_select():
            return
        self.EditDropdown.kw["pack_cmd"] = \
            lambda: self.__color_parts(part, self.check_var.get())
        self.BehaviourDropdown.kw["pack_cmd"] = \
            lambda: self.__modify_parts(part, self.behaviour.get())
        if "dropdown" in str(part.widget).split('.')[-1].lower():
            self.Name.configure(text=f"Name: {part.widget.kw['name']}")
            self.var_data = part.widget.kw['name']
            self.var_name_data = part.widget.kw['name']
        else:
            self.Name.configure(text=f"Name: {str(part.widget).split('.')[-1]}")
            self.var_data = str(part.widget).split(".")[-1]
            self.var_name_data = str(part.widget).split(".")[-1]
        finder = 0
        for i in list(self.changed_widgets.items()):
            finder += i.count(self.var_name_data)
        try:
            if finder > 0:
                pass
            else:
                self.changed_widgets[self.var_name_data] = {}
        except IndexError:
            self.changed_widgets[self.var_name_data] = {}

    def __color_parts(self, part: tk.Event, value: str):
        """
        This private function will change colors values of selected widget.

        :param part: widget to change color data
        :param value: selected widget
        :return:
        """
        self.selected = value
        try:
            self.rgb_value = hex_to_rgb(part.widget.cget(value).replace("#", ""))
        except tk.TclError:
            return
        self.ColorRedInput["state"] = "normal"
        self.ColorGreenInput["state"] = "normal"
        self.ColorBlueInput["state"] = "normal"
        self.ColorRedInput.delete(0, tk.END)
        self.ColorRedInput.insert(0, self.rgb_value[0])
        self.ColorGreenInput.delete(0, tk.END)
        self.ColorGreenInput.insert(0, self.rgb_value[1])
        self.ColorBlueInput.delete(0, tk.END)
        self.ColorBlueInput.insert(0, self.rgb_value[2])
        self.Color.configure(background=part.widget[value])
        self.ApplyButton.configure(command=lambda: self.__apply_values(part))
        self.SaveButton.configure(command=lambda: self.__save(self.name))

    def __modify_parts(self, part: tk.Event, value: str):
        """

        This private function will change some specific values of selected widget.

        :param part: widget to change behaviour
        :param value: selected widget
        :return:
        """
        self.selected = value
        self.ColorRedInput["state"] = "disabled"
        self.ColorGreenInput["state"] = "disabled"
        self.ColorBlueInput["state"] = "disabled"
        self.ApplyButton.configure(command=lambda: self.__apply_values(part))
        self.SaveButton.configure(command=lambda: self.__save(self.name))

    def __apply_values(self, part: tk.Event):
        """

        This private function applies modified values to theme and also to widget

        :param part: widget that is being configured
        :return:
        """
        if len(self.ManualValue.get()) == 0:
            rgb_values = self.__get_rgb(self.ColorRedInput, self.ColorGreenInput,
                                        self.ColorBlueInput)
            self.apply_text = f"'{rgb_values}'"
            try:
                part.widget.configure({self.selected: self.apply_text.replace("'", "")})
                self.changed_widgets[self.var_name_data][self.selected] = \
                    str(part.widget[self.selected])
            except tk.TclError:
                tkm.showwarning("Designer", f"it looks like {self.selected} "
                                            f"cannot be set for this widget")
        else:
            self.apply_text = self.ManualValue.get()
            try:
                try:
                    part.widget[self.selected] = self.ManualValue.get()
                except IndexError:
                    pass
                self.changed_widgets[self.var_name_data][self.selected] = \
                    str(part.widget[self.selected])
            except tk.TclError:
                tkm.showwarning("Designer", f"it looks like {self.selected} "
                                            f"cannot be set for this widget or"
                                            f" \'{self.ManualValue.get()}\' "
                                            f"cannot be set for {self.selected}")

    def __un_select(self):
        """

        This private function takes everything to the defaults.
        :return:
        """
        try:
            self.Color.configure(background="black")
        except tk.TclError:
            return True
        self.Name.configure(text="Name: ")
        self.ColorRedInput.delete(0, tk.END)
        self.ColorRedInput.insert(0, "0")
        self.ColorGreenInput.delete(0, tk.END)
        self.ColorGreenInput.insert(0, "0")
        self.ColorBlueInput.delete(0, tk.END)
        self.ColorBlueInput.insert(0, "0")
        self.ApplyButton.configure(command=None)
        self.selected = ""
        return None

    def __save(self, name="default"):
        """

        This private function saves current theme into themes folder.

        :param name: name of the theme
        """
        try:
            mkdir("themes")
        except FileExistsError:
            pass
        with open(f"themes/{name}.json", "w") as file:
            json.dump(self.changed_widgets, file, indent=4)
        tkm.showinfo("Designer", "your theme was saved!")

    def load(self, variables_to_change: dict, path=".", customWidgets=None):
        """
        Load theme to widgets

        :param customWidgets: which widget is custom widget
        :param path: full path of folder
        :param variables_to_change: widgets you want to apply style to them
        :return:
        """
        if customWidgets is None:
            customWidgets = []
        give = False
        try:
            with open(f"{path}/themes/{self.name}.json") as file:
                data = json.load(file)
            for x, y in data.items():
                self.changed_widgets[x] = {}
                for a, b in y.items():
                    self.changed_widgets[x][a] = str(b)
            for value in variables_to_change:
                if value in customWidgets:
                    for i in data[value]:
                        try:
                            variables_to_change[value][i] = data[value][i]
                            variables_to_change[value].kwd[i] = data[value][i]
                        except tk.TclError:
                            continue
                if isinstance(variables_to_change[value], list):
                    for _, val in enumerate(variables_to_change[value]):
                        try:
                            val.configure(data[value])
                        except tk.TclError:
                            pass
                else:
                    try:
                        variables_to_change[value].configure(data[value])
                    except tk.TclError:
                        for i in data[value]:
                            try:
                                variables_to_change[value][i] = data[value][i]
                            except tk.TclError:
                                continue
        except FileNotFoundError:
            give = True
        if give:
            raise DesignerThemeNotFound(f"Theme with name {self.name} was not found in"
                                        f" themes folder!")

    def set_theme_name(self, name="default"):
        """

        :param name: put name of theme you want to load
        """
        self.name = name

    def bind(self, widget):
        """

        :param widget: widget you want to bind to designer
        """
        if self.show:
            widget.bind("<Button-3>", self.__select_widget)
            widget.bind_all("<Escape>", lambda event: self.__un_select())

    def bind_to(self, widgets: list):
        """

        :param widgets: input widgets in list you want to bind to designer
        """
        for i in widgets:
            if self.show:
                i.bind("<Button-3>", self.__select_widget)
                i.bind_all("<Escape>", lambda event: self.__un_select())


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """
    :param red: Red color value
    :param green: Green color value
    :param blue: Blue color value
    :return: converts red, green, blue into hex color format for tkinter
    """
    red = min(red, 255)
    green = min(green, 255)
    blue = min(blue, 255)
    red = max(red, 0)
    green = max(green, 0)
    blue = max(blue, 0)
    return '#%02x%02x%02x' % (red, green, blue)


def hex_to_rgb(hex_color: str) -> list:
    """

    :param hex_color: hex color value
    :return: rgb value from hex color
    """
    try:
        return_list = [int(hex_color[i:i + 2], 16) for i in (0, 2, 4)]
        return return_list
    except ValueError:
        tkm.showwarning("Designer", f"It's not possible for me to convert {hex_color} "
                                    f"to RGB")
        return [0, 0, 0]
