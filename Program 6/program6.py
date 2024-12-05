from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Daftar Makanan Enak :)")
top.geometry("300x300")  

title_label = Label(top, text="Pilihlah Makanan Yang Lezat", font=("Arial", 14, "bold"))
title_label.pack(pady=10)  

frame = Frame(top)
frame.pack(pady=10)

Lb1 = Listbox(frame, width=20, height=10, font=("Arial", 12), bg="#f0f8ff", selectbackground="#87cefa")
Lb1.insert(1, "Ayam Geprek")
Lb1.insert(2, "Nasi Padang")
Lb1.insert(3, "Telur Balado")
Lb1.insert(4, "Cumi Asin Pedas")
Lb1.insert(5, "Gulai Kambing")
Lb1.insert(6, "Bebek Goreng")
Lb1.pack(side=LEFT, padx=5)


def show_selection():
    selected = Lb1.get(ACTIVE)
    messagebox.showinfo("Uww Lezatt", f"Anda memilih: {selected}")

button = Button(top, text="Accept", command=show_selection, bg="white", font=("Arial", 12))
button.pack(pady=10)

top.mainloop()
