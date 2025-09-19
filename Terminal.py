import tkinter as tk #GUI
from tkinter import ttk #виджеты
from tkinter import scrolledtext #полоска-слайдер

window = tk.Tk() #создание окна
window.geometry("1600x900")
window.title("Terminal Emulator")

user = tk.Label(window, text="Mikhail@hostname:~$",font=("Courier", 12)) #имя пользователя
user.pack(anchor="nw") #якорь местоположения на левый верхний угол

entry = tk.Entry(window) #поле ввода
entry.pack(fill="both")

enter_btn = tk.Button(text="Enter") #кнопка ввод, только почему-то не по центру
enter_btn.pack(anchor="ne", pady=0)

label = tk.Label(window, text="Тестовое Окно") #тестовый текст
label.pack(pady=20)

window.mainloop()

