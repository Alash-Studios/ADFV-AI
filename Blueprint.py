from tkinter import *

from netaddr.strategy.ipv6 import width

# Code Formalities
root = Tk()  # create the root window
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # size of the window
root.config(bg="dimgray")  # to change the background colour of the window
root.title('Blueprint')

text = Text(root, height=2, width=10, bg="black", fg="white", font=("Ariel", 12), padx=10, pady=10)
text.insert(END, "how are you")
text.config(state= DISABLED)
text.pack(pady=20)

mainloop()




