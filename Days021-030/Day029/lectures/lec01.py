from tkinter import *

window = Tk()

red = Label(bg="red", width=20, height=5)
red.grid(row=0, column=0)

green = Label(bg="green", width=20, height=5)
green.grid(row=1, column=1)

blue = Label(bg="blue", width=20, height=5)
blue.grid(row=2, column=0)


window.mainloop()
