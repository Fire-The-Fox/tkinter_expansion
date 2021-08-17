import xml.etree.ElementTree as Xml


class Gui:
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        self._all_available_kwargs = ["xml_file", "css_file"]
        self._kwargs_fix = {"xml_file": None, "css_file": None}
        for i in self._all_available_kwargs:
            try:
                self.kwargs[i]
            except KeyError:
                self.kwargs[i] = self._kwargs_fix[i]

    def load_xml(self):
        if self.kwargs["xml_file"] is not None:
            tree = Xml.parse(self.kwargs["xml_file"])
            root = tree.getroot()
            guis = {}
            mains = []
            mains_data = []
            for i in root:
                gui_object = list(i.attrib.items())[0][1]
                guis[f"{i.tag} = tk.{gui_object}"] = []
                for ii in i:
                    ii.text = ii.text.replace("-", "<")
                    ii.text = ii.text.replace("_", ">")
                    if ii.tag == "bind" or ii.tag == "bind_all":
                        test = eval(f"{ii.text}")
                        test = test.replace(">", "_")
                        test = f"'<{list(ii.attrib.items())[0][1]}>', {test}"
                    else:
                        test = eval(ii.text)
                    guis[f"{i.tag} = tk.{gui_object}"].append(f"{i.tag}.{ii.tag}({test})")
            for i in list(guis.items()):
                mains.append(i[0])
                for ii in i[1]:
                    mains_data.append(ii)
            return mains, mains_data
