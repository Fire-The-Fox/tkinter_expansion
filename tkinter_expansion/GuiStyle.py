from os import mkdir
import json


class CssWrapperMissingFile(Exception):
    pass


class CssWrapperMissingChar(Exception):
    pass


class StyleManager:
    def __init__(self, *args, **kwargs):
        self.kwargs = {"css_file": None}
        self.kwargs.update(kwargs)

    def load_css(self):
        if self.kwargs["css_file"] is not None:
            raise_file = False
            try:
                with open(self.kwargs["css_file"]) as css:
                    css_data = css.read().split("\n")
            except FileNotFoundError:
                raise_file = True

            if raise_file:
                raise CssWrapperMissingFile(f"File named {self.kwargs['css_file']} was "
                                            f"not found!")
            self.json_data = {}
            new_i = ""
            line = 0
            for i in css_data:
                line += 1
                raise_error = False
                if "{" in i or "}" in i:
                    if i == "}":
                        continue
                    if "#" not in i and "." not in i:
                        print(f"Warning: Missing #/. in line {line}")
                    new_i = i.replace(".", "").replace("#", "").replace("{", "")\
                        .strip(" ")
                    self.json_data[new_i] = {}
                else:
                    if len(i.strip()) == 0:
                        raise CssWrapperMissingChar("isn't } missing?")
                    new_a = i.split(":")[0].strip(" ")
                    try:
                        if ";" not in i.split(":")[1]:
                            print(f"Warning: Missing ; in line {line}")
                        new_b = i.split(":")[1].strip(" ").replace(";", "")
                        self.json_data[new_i][new_a] = new_b
                    except IndexError:
                        raise_error = True
                    if raise_error:
                        raise CssWrapperMissingChar("isn't } missing?")
            return self.json_data
        else:
            raise CssWrapperMissingFile(f"Css file is missing!")

    def css_to_theme(self, name="css_theme"):
        try:
            mkdir("themes")
        except FileExistsError:
            pass
        with open(f"themes/{name}.json", "w") as file:
            json.dump(self.json_data, file)
