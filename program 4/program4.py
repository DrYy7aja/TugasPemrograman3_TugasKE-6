from tkinter import *


top = Tk()
top.title("Form User Input")
top.geometry("300x200")  
top.configure(bg="#135021")  

frame = Frame(top, bg="#135021", padx=10, pady=10)
frame.pack(pady=20)

L1 = Label(frame, text="USERNAME:", font=("Fantasy", 10, "bold"), bg="#45CB0C", fg="black")
L1.grid(row=0, column=0, padx=10, pady=10, sticky=W)

E1 = Entry(frame, bd=2, font=("Fantasy", 10), width=20)
E1.grid(row=0, column=1, padx=10, pady=10)

def on_submit():
    user_name = E1.get()
    if user_name:
        Label(top, text=f"Wassap, {user_name}!", font=("Arial", 10, "italic"), bg="#45CB0C").pack(pady=5)
    else:
        Label(top, text="Masukkin Dulu Username nya :)!", font=("Fantasy", 10, "bold"), bg="black", fg="red").pack(pady=5)

submit_button = Button(frame, text="Submit", font=("Arial", 10), command=on_submit, bg="green", fg="white", padx=10, pady=5)
submit_button.grid(row=1, column=1, padx=10, pady=10, sticky=E)

top.mainloop()
