from tkinter import *
from PIL import Image, ImageTk, ImageSequence

# Inisialisasi root
root = Tk()
root.title("Sekian dan Terimakasih")
root.geometry("800x550")
root.config(background='white')

# Path ke file GIF
gif_path = r"C:\Users\dicky\OneDrive\Documents\TugasPemrograman3_TugasKE-5\Program 10\dog.gif"

# Fungsi untuk memutar animasi GIF
def animate(index):
    try:
        # Menampilkan frame GIF
        frame = frames[index]
        gif_label.configure(image=frame)
        
        # Update index untuk frame berikutnya
        index = (index + 1) % len(frames)
        
        # Timer untuk memutar animasi (50 ms per frame)
        root.after(50, animate, index)
    except Exception as e:
        print(f"Error in animation: {e}")

# Load GIF menggunakan PIL
try:
    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]
except FileNotFoundError:
    print("GIF file not found. Please check the path.")
    frames = []

# Label untuk menampilkan GIF
gif_label = Label(root, bg="white")
gif_label.place(x=155, y=20, width=450, height=500)

# Memulai animasi jika frames berhasil dimuat
if frames:
    animate(0)
else:
    gif_label.config(text="GIF not found or failed to load.", font=("Arial", 16), fg="white")

# Loop utama Tkinter
root.mainloop()
