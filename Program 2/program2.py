import tkinter as tk
from tkinter import messagebox


top = tk.Tk()
top.title("First GUI Program Audry")  
top.configure(bg="#8B0000") 

def helloCallBack():
    messagebox.showwarning(":)", "Audry Nabila NIM 1223009")

B = tk.Button(top, text="DARURAT", command=helloCallBack, bg="black", fg="red")
B.pack(pady=20)  

top.mainloop()
