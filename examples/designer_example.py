import tkinter as tk
import tkinter_expansion as tke

# basic tkinter application

root = tk.Tk()
root.configure(width=700, height=700)

# designer

designer = tke.Designer(master=root, share_locals=locals(), share_globals=globals())
designer.set_theme_name()

# usage of tke.rgb_to_hex(red, green, blue)
window = tk.Button(root, background=tke.rgb_to_hex(167, 245, 0))
window.place(relx=0, rely=0, relheight=0.5, relwidth=0.5)
if designer.show:
    window.bind("<Button-3>", lambda event: designer.select_widget(event))
    window.bind_all("<Escape>", lambda event: designer.un_select())

window2 = tk.Label(root, background=tke.rgb_to_hex(70, 245, 66))
window2.place(relx=0.5, y=0, relheight=0.5, relwidth=0.5)
if designer.show:
    window2.bind("<Button-3>", lambda event: designer.select_widget(event))
    window2.bind_all("<Escape>", lambda event: designer.un_select())

window3 = tk.Label(root, background=tke.rgb_to_hex(250, 200, 51))
window3.place(x=0, rely=0.5, relheight=0.5, relwidth=0.5)
if designer.show:
    window3.bind("<Button-3>", lambda event: designer.select_widget(event))
    window3.bind_all("<Escape>", lambda event: designer.un_select())

window4 = tk.Label(root, background=tke.rgb_to_hex(0, 0, 0))
window4.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)
if designer.show:
    window4.bind("<Button-3>", lambda event: designer.select_widget(event))
    window4.bind_all("<Escape>", lambda event: designer.un_select())

for i in designer.load():
    try:
        exec(i)
    except NameError:
        continue

if __name__ == '__main__':
    root.mainloop()
