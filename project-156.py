# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:36:58 2022

@author: User
"""

from tkinter import*
from PIL import ImageTk, Image
root=Tk()

root.title("Endless Pokemon card Game 1")
root.geometry("600x700")
root.configure(background="chocolate1")

img = ImageTk.PhotoImage(Image.open("persion.jpg"))

player1_label = Label(root,text="Player 1",bg="red",fg="white")
player1_label.place(relx=0.1,rely =0.3, anchor=CENTER)

player2_label = Label(root,text="Player 2",bg="red",fg="white")
player2_label.place(relx=0.9,rely =0.3, anchor=CENTER)

player1_score_label = Label(root, bg="royal blue", fg="white")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score_label = Label(root, bg="royal blue", fg="white")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

label_image = Label(root)
label_image.place(relx=0.5, rely=0.5)

root.mainloop()