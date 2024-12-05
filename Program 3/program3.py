import tkinter as tk

top = tk.Tk()
top.title("stickman menyapa")
top.geometry("400x400")

C = tk.Canvas(top, bg="white", height=400, width=400)

C.create_oval(150, 50, 200, 100, fill="white", outline="black", width=2)

C.create_line(175, 100, 175, 200, fill="black", width=2)


C.create_line(175, 120, 125, 150, fill="black", width=2)

C.create_line(175, 120, 225, 90, fill="black", width=2)  
C.create_line(225, 90, 250, 60, fill="black", width=2)   

C.create_line(175, 200, 150, 250, fill="black", width=2)

C.create_line(175, 200, 200, 250, fill="black", width=2)

C.create_text(250, 50, text="Haloo", font=("Arial", 16, "bold"), fill="black")

C.pack()

top.mainloop()

