import tkinter_expansion.experimental as tkx
import tkinter_expansion as tke
import tkinter as tk

gui = tkx.Gui(xml_file="gui.xaml")
gui_data = gui.load_xml()

for i in gui_data[0]:
    exec(i)
for i in gui_data[1]:
    exec(i)

designer = tke.Designer(master=root, share_locals=locals(), share_globals=globals())
root.mainloop()
