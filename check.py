from tkinter import *
import os
def open_www():

    os.system("start \"\" http://ynet.co.il")

root = Tk()
btn1=Button(root, text='Open ynet.co.il', command=open_www)
btn1.pack(side=TOP)
root.mainloop()