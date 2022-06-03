import tkinter as tk
from PIL import Image, ImageTk
import re
from tkinter import END
import ass2 as bi


def my_upd(my_widget):  # On selection of option
    my_w = my_widget.widget
    index = int(my_w.curselection()[0])  # position of selection
    value = my_w.get(index)  # selected value
    e1_str.set(value)  # set value for string variable of Entry
    l1.delete(0, END)  # Delete all elements of Listbox


def my_down(my_widget):  # down arrow is clicked
    l1.focus()  # move focus to Listbox
    l1.selection_set(0)  # select the first option


def get_data(*args):  # populate the Listbox with matching options
    search_str = e1.get()  # user entered string
    l1.delete(0, END)  # Delete all elements of Listbox
    try:
        s = bi.sortDic(bi.finDicFreqRef[search_str], bi.ref)
        my_list = bi.finList(search_str, s)
        for element in my_list:
            if re.match(search_str, element, re.IGNORECASE):
                print(element)
                ee = element.split(" ")
                eef = ee[0] + " " + ee[-1]
                l1.insert(tk.END, eef)  # add matching options to Listbox
    except KeyError:
        pass


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=100)
canvas.pack()
# canvas.grid(columnspan=3, rowspan=7)

logo = Image.open("index.png")
logo = logo.resize((250, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
# logo_label.grid(column=1, row=2)
logo_label.pack(pady=20)

instructions = tk.Label(root, text="Enter your search", font="Helvetica 12")
# instructions.grid(column=1, row=5)
instructions.pack(pady=20)

e1_str = tk.StringVar()  # string variable
e1 = tk.Entry(root, font="Helvetica 12", textvariable=e1_str, width=30)  # entry
e1.pack()
# e1.grid(row=6, column=1, padx=10, pady=0)

# listbox
l1 = tk.Listbox(root, height=6, width=45, relief='flat',
                bg='SystemButtonFace', highlightcolor='SystemButtonFace')
l1.pack(pady=3)
# l1.grid(row=2, column=1)

# l1.bind('<<ListboxSelect>>', my_upd)
e1.bind('<Down>', my_down)  # down arrow key is pressed
l1.bind('<Right>', my_upd)  # right arrow key is pressed
l1.bind('<Return>', my_upd)  # return key is pressed
e1_str.trace('w', get_data)  #
# print(root['bg']) # reading background colour of window

canvas = tk.Canvas(root, width=600, height=50)
canvas.pack()
root.mainloop()  # Keep the window open

