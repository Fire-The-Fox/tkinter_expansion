# Tkinter expansion

**`python framework that expands tkinter with a bunch of cool stuff.`**

### welcome to Tkinker expansion


Tkinter expansion is heavily inspired by JavaFX.

please visit [docs](https://fire-the-fox.github.io/tkinter_expansion_docs/) for better usage and explanation

### quick example
```py
import tkinter as tk
import tkinter_expansion as tke

# App base

root = tk.Tk()
root.configure(width=700, height=700)

# Initializing Designer

# share_locals and share_globals free!
designer = tke.Designer(master=root)

# App widgets, please add name or just dont add it
window = tk.Button(root, name="window")
window.place(relx=0, rely=0, relheight=1, relwidth=1)

# Designer.show is set True by default.
# When you are done with designing just put show=False in tke.Designer()

designer.bind(window)

root.mainloop()
```
