#import class library so that everytime its called, you can call it as tk
import tkinter as tk
from tkinter import ttk

#function that handles the event
def on_select(event):
    #get the item that the end user has chosen on the combo box
    selected_item = event.widget.get()
    print ("Selected item", selected_item)

#object for root window
root = tk.Tk()
root.title("Combobox Example")

#Create static array of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#Tie it to combobox object we created
combo_box = ttk.Combobox(root, values=items)

#Bind combobox event to objects and tie it to method created earlier
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

root.mainloop()

