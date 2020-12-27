import tkinter as tk
import os
def open_www():
    os.system("start \"\" https://www.wikipedia.org/")

root= tk.Tk()
color=""
color=input("Enter a color and open at full screan ")
lb1=tk.Label(root,text="wow you chose " + color,bg=color)
btn1=tk.Button(root, text='Exit', command=exit)
btn2=tk.Button(root, text="Open wikipedia.org/",command=open_www)

btn1.place(x=0,y=0)
btn2.pack(anchor="ne")
lb1.pack(side="top",expand="YES",fill="both")

root.mainloop()