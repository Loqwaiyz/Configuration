import tkinter as tk #GUI
from tkinter import scrolledtext #полоска-слайдер

window = tk.Tk() #создание окна
window.geometry("1600x900")
window.title("Terminal Emulator")

label = tk.Label(window, text="Тестовое Окно")
label.pack(pady=20)

window.mainloop()

