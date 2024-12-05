from tkinter import *  

top = Tk()
top.title("Checkbox Demo")

CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(top, text="Music", variable=CheckVar1, 
                 onvalue=1, offvalue=0, height=2, width=20)
C1.pack()


C2 = Checkbutton(top, text="Video", variable=CheckVar2, 
                 onvalue=1, offvalue=0, height=2, width=20)
C2.pack()


top.mainloop()
