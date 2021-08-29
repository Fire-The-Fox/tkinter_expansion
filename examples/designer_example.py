import tkinter as tk
import tkinter_expansion as tke

# basic tkinter application

root = tk.Tk()
root.configure(width=700, height=700)

# designer

designer = tke.Designer(master=root, share_locals=locals(), share_globals=globals(), show=True)
designer.set_theme_name()
theme_data = designer.load()

window = tk.Button(root, bg=theme_data["window"]["background"],
                   activeforeground=theme_data["window"]["activeforeground"],
                   activebackground=theme_data["window"]["activebackground"],
                   highlightcolor=theme_data["window"]["highlightcolor"],
                   highlightbackground=theme_data["window"]["highlightbackground"])
window.place(relx=0, rely=0, relheight=1, relwidth=1)
if designer.show:
    window.bind("<Button-3>", lambda event: designer.select_widget(event))
    window.bind_all("<Escape>", lambda event: designer.un_select())

if __name__ == '__main__':
    root.mainloop()
    print()
