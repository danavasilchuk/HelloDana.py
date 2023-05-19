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

