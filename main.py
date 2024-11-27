#
# # https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# import tkinter as tk
#
# window = tk.Tk()
#
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# # Label
# my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "italic"))
# my_label.pack()
#
# my_label["text"] = "new text"
# my_label.config(text="new text")
#
# # Button
#
# def button_clicked():
#     print("I git clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
# button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
#
# #
# input = tk.Entry(width=10)
# input.pack()
# print(input.get())



# window.mainloop()


from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


