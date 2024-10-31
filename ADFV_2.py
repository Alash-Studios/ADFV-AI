from logging import shutdown
from tkinter import *
import sys
import webbrowser
import time

# Code Formalities
root = Tk()  # create the root window
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")  # size of the window
root.config(bg="black")  # to change the background colour of the window
root.title('ADFV 2.Ai')

# Text Area for displaying input
TextField2 = Text(root, height=20, width=43, bg="black", fg="white")  # added one textbox to read
TextField2.pack(side=TOP, fill=BOTH, expand=True)  # location on the window

# Bottom Frame for input field and send button
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X, padx=5, pady=5)

# Input Field
TextField = Text(root, height=1.5, width=120, bg="pink")  # added one textbox to read
TextField.pack(side=LEFT, pady=22, expand=True, padx=(165, 5))  # location on the window


# Converstionn Flow
def inserted_text():
    user_input = TextField.get("1.0", END).lower().strip()  # get from the input field
    if "hello" in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, "Hello, User" + '\n')  # input the response
        TextField.delete("1.0", END)  # clear the input field

    elif "tell me about digital marketing" in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END,
                          "This is a form of using technology to create awareness on a particular product." + '\n')  # input the response
        TextField.delete("1.0", END)  # clear the input field

    elif "quit" in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, "Quitting" + '\n')  # input the response
        TextField.delete("1.0", END)
        time.sleep(1)
        root.destroy()

    elif "shutdown" in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, "Shutting Down" + '\n')  # input the response
        TextField.delete("1.0", END)
        time.sleep(1)
        root.destroy()

    elif "close" in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, "Closing" + '\n')  # input the response
        TextField.delete("1.0", END)
        time.sleep(1)
        root.destroy()

    elif " " in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, " " + '\n')  # input the response
        TextField.delete("1.0", END)


    elif " " in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, " " + '\n')  # input the response
        TextField.delete("1.0", END)

    elif " " in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, " " + '\n')  # input the response
        TextField.delete("1.0", END)

    elif " " in user_input:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n', "right")
        TextField2.insert(END, " " + '\n')  # input the response
        TextField.delete("1.0", END)



    else:
        TextField2.tag_config("right", justify="right")
        TextField2.insert(END, '\n' + user_input + '\n' + '\n' + '\n', "right")
        TextField2.insert(END, "That Question Has Not Been Inputed in my Database, sorry but i can't help you in that area." + '\n')  # input the response
        TextField.delete("1.0", END)  # clear the input field


# Send button code
send = Button(root, height=1, width=3, text="^", command=lambda: inserted_text(), bg="pink")  # create a text box
send.pack(side=RIGHT, pady=22, padx=(0, 140))  # location on the window

root.mainloop()
