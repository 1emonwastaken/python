from tkinter import *
'''Window configuration'''
root = Tk()
root.geometry("600x400+660+340") #("<Width> x <Length> + <dist from top> + <dist from left">)
root.title("My Window") #("<Title>")
root.resizable(False, False) #(Width, Height) => Specify whether window can be resized in any direction
root.minsize(<min_width>, <min_height>) #If resizable, enter min width, height
root.maxsize(<max_width>,<max_height>) #If resizable, enter max width, height
root.attributes("-alpha", 1.0) #Transparency, 0.0(transparent) - 1.0(opaque)
root.attributes("-topmost", 1) #Priority if window should be on top, 0/1
root.iconbitmap(r"<path on computer>") #icon for program

'''Widgets'''
labels = Label(root) #labels = Label(root, text = " ")
labels['text'] = " "
labels.config(text = " ")
root.mainloop()