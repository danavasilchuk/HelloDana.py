#import class library so that everytime its called, you can call it as tk
import tkinter as tk

#define a function to implement print function
def button_click():
    print("Button clicked!")

#create root window object
root = tk.Tk()
root.title("Button Example")

#create button object
#three arguments in parameter; put button in root window, set the txt, 
#set function in which button will click for 
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#keep root window open; call root object
root.mainloop()
                       



