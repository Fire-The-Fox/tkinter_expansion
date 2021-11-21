import tkinter as tk
import tkinter_expansion as tke

# basic tkinter application

root = tk.Tk()
root.configure(width=700, height=700)

# designer

designer = tke.Designer(master=root, share_locals=locals(), share_globals=globals(),
                        show=True)
designer.set_theme_name()

window = tk.Button(root)
window.place(relx=0, rely=0, relheight=1, relwidth=1)
designer.bind(window)

designer.load({"window": window})

if __name__ == '__main__':
    root.mainloop()
