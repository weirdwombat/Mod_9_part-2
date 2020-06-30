"""
Program : first_gui.py
Author : Olivia Kennedy
Date Last Modified : 06/30/2020
This program creates a GUI called Favorite Meal that allows the user to select checkbuttons.
Once a checkbutton has been selected, the message 'Cool!' is triggered.
There is a built in button that allows the user to exit the interface.
"""
import tkinter
def pick_meal():
    label.config(text="Cool!")


m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_meal).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_meal).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_meal).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_meal).grid(row=4)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen
